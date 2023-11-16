import express, { Express, Request, Response } from "express";
import cors from "cors";
import DSA from "./data/dsa";
import readFile from "./utils/readFile";

const app: Express = express();

app.use(cors());
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
  console.log(req.params.id);
  res.send("Express + TypeScript Server");
});

app.listen(port, () => {
  console.log(`⚡️[server]: Server is running at http://localhost:${port}`);
});
