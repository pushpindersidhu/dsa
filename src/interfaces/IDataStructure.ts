import React from "react";

export default interface IDataStructure {
  id: number;
  name: string;
  description: React.FC;
  code: string;
  solution: string;
  completed: boolean;
}
