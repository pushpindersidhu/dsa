import express, { Express, Request, Response } from "express";
import cors from "cors";
import bodyParser from "body-parser";
import DSA from "./data/dsa";
import readFile from "./utils/readFile";
import executeCode from "./utils/exec";

const app: Express = express();

app.use(cors());
app.use(bodyParser.json());
const port = 3000;

app.get("/", (req: Request, res: Response) => {
  res.send("Sidhu");
});

app.get("/dsa", (req: Request, res: Response) => {
  const data = DSA.map((dsa) => {
    const description = readFile(dsa.description);
    const code = readFile(dsa.code);
    const solution = readFile(dsa.solution);
    return {
      ...dsa,
      description,
      code,
      solution,
    };
  });

  res.send(data);
});

app.post("/test/:id", (req: Request, res: Response) => {
  const id = parseInt(req.params.id);
  const code = req.body.code;

  const dsa = DSA.find((dsa) => dsa.id === id);

  if (!dsa) {
    res.send("DSA not found");
    return;
  }

  console.log(dsa.test);

  const result = executeCode(code, dsa.test);

  res.send(result);
});

app.listen(port, () => {
  console.log(`⚡️[server]: Server is running at http://localhost:${port}`);
});
