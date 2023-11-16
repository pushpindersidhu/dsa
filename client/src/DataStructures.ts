import Stack from "./descriptions/stack";
import IDataStructure from "./interfaces/IDataStructure";

const DataStructures: IDataStructure[] = [
  {
    id: 1,
    name: "Stack",
    description: Stack,
    code: `class Stack {
  constructor() {
  }

  // Adds an element to the stack
  push(element) {
    // Implementation goes here
  }

  // Removes and returns the top element from the stack
  pop() {
    // Implementation goes here
  }

  // Returns the top element of the stack without removing it
  peek() {
    // Implementation goes here
  }

  // Returns true if the stack is empty, false otherwise
  isEmpty() {
    // Implementation goes here
  }

  // Returns true if the stack is full, false otherwise
  isFull() {
    // Implementation goes here
  }

  // Add any other methods or properties as needed
}

export default Stack;
`,
    solution: "",
    completed: false,
  },
];

export default DataStructures;
