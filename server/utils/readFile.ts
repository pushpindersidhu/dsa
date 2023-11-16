import fs from "fs";

export default function readFile(path: string): string {
  try {
    const fileContent: string = fs.readFileSync(path, "utf-8");
    return fileContent;
  } catch (error) {
    console.error(`Error reading file at path ${path}:`, error);
    return "";
  }
}
