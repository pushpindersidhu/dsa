import { useState } from "react";
import Editor from "@monaco-editor/react";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import { FaCode } from "react-icons/fa6";
import Description from "./components/Description";

import DataStructures from "./DataStructures";

function App() {
  const [dataStructure, setDataStructure] = useState(DataStructures[0]);

  const handleEditorChange = (value: string | undefined) => {
    if (value) {
      setDataStructure((prev) => ({ ...prev, code: value }));
    }
  }

  return (
    <div className="w-full h-screen grid grid-cols-12 bg-[#161618] gap-2 p-2">
      <Navbar />
      <Sidebar />
      <div className="col-span-4 rounded-lg overflow-hidden bg-primary">
        <Description>
          <dataStructure.description />
        </Description>
      </div>
      <div className="col-span-6 rounded-lg overflow-hidden bg-primary">
        <h3 className="text-gray-300 text-sm font-semibold px-4 flex items-center bg-secondary py-2">
          <FaCode className="inline-block mr-2 text-accent" />
          Code
        </h3>
        <Editor
          height="100%"
          width="100%"
          defaultLanguage="typescript"
          defaultValue={dataStructure.code}
          onChange={handleEditorChange}
          className="my-4 mx-2"
          theme="vs-dark"
          options={{ lineNumbers: "on", minimap: { enabled: false } }}
        />
      </div>
    </div>
  );
}

export default App;
