import { execSync } from "child_process";
import { createWriteStream } from "fs";
import { resolve } from "path";
import readFile from "./readFile";
import e from "express";

function executeCode(code: string, test: string): string {
  const testFilePath = resolve(__dirname, "../temp.test.ts");

  const stream = createWriteStream(testFilePath);
  stream.write(code);

  stream.write(readFile(test));
  stream.end();

  while (!stream.writableEnded) {
    continue;
  }

  let result = "";
  try {
    result = execSync(`npx jest ${testFilePath}`, {
      encoding: "utf-8",
      stdio: "pipe",
      timeout: 10000,
    }); 

    console.log(result);
  } catch (error) {
    result = error.stderr.toString();
  }

  execSync(`rm ${testFilePath}`);

  return result;
} 

export default executeCode;
