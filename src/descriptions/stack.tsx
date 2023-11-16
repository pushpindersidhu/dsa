const Stack = () => {
  return (
    <div className="my-2">
      <h1 className="text-lg font-semibold mb-2 text-gray-200">Stack</h1>

      <p className="text-gray-100 mb-4 text-sm">
        A stack is a linear data structure that follows the LIFO (Last In First
        Out) principle.
      </p>

      <div className="mb-4">
        <h2 className="text-md font-semibold mb-2">Operations</h2>
        <ul className="list-disc pl-4 text-sm">
          <li>
            <strong>Push:</strong> Adds an element to the collection.
          </li>
          <li>
            <strong>Pop:</strong> Removes the top element from the collection.
          </li>
          <li>
            <strong>Peek:</strong> Returns the top element of the stack.
          </li>
          <li>
            <strong>isEmpty:</strong> Returns true if the stack is empty.
          </li>
          <li>
            <strong>isFull:</strong> Returns true if the stack is full.
          </li>
        </ul>
      </div>

      <div className="mb-4">
        <h2 className="text-md font-semibold mb-2">Example</h2>
        <p className="text-gray-100 mb-2 text-sm">Consider a stack of books:</p>
        <ol className="list-decimal pl-4 text-sm">
          <li>Book A was placed on the stack first.</li>
          <li>Book B was placed on the stack second.</li>
          <li>Book C was placed on the stack last.</li>
        </ol>
        <p className="text-gray-100 mt-2 text-sm">
          When you start removing books, you'll first remove Book C, then Book
          B, and finally Book A.
        </p>
      </div>

      <div>
        <h2 className="text-md font-semibold mb-2">Use Cases</h2>
        <ul className="list-disc pl-4 text-sm text-gray-100">
          <li>In function calls/recursive calls.</li>
          <li>To reverse a word.</li>
          <li>In undo operations in text editors.</li>
        </ul>
      </div>
    </div>
  );
};

export default Stack;
