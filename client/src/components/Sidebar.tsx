import { PiTreeStructureFill } from "react-icons/pi";
import { RiStackFill } from "react-icons/ri";
import { HiMiniQueueList } from "react-icons/hi2";
import { FaLink } from "react-icons/fa6";
import { TbBinaryTree } from "react-icons/tb";
import { PiGraphFill } from "react-icons/pi";
import { FaHashtag } from "react-icons/fa6";


const Sidebar = () => {
  const dataStructures = [
    {
      name: "Stack",
      icon: RiStackFill,
      completed: false,
      code: "",
      solution: "",
    },
    {
      name: "Queue",
      icon: HiMiniQueueList,
      completed: false,
      code: "",
      solution: "",
    },
    {
      name: "Linked List",
      icon: FaLink,
      completed: false,
      code: "",
      solution: "",
    },
    {
      name: "Binary Tree",
      icon: TbBinaryTree,
      completed: false,
      code: "",
      solution: "",
    },
    {
      name: "Binary Search Tree",
      icon: PiTreeStructureFill,
      completed: false,
      code: "",
      solution: "",
    },
    {
      name: "Graph",
      icon: PiGraphFill,
      completed: false,
      code: "",
      solution: "",
    },
    {
      name: "Hash Table",
      icon: FaHashtag,
      completed: false,
      code: "",
      solution: "",
    },
  ];

  return (
    <div className="bg-primary col-span-2 rounded-lg overflow-hidden">
      <h3 className="text-gray-300 text-sm font-semibold px-4 flex items-center bg-secondary py-2">
        <PiTreeStructureFill className="inline-block mr-2 text-accent" />
        Data Structures
      </h3>

      <div className="flex flex-col gap-2 my-4 mx-2">
        {dataStructures.map((dataStructure) => (
          <div
            key={dataStructure.name}
            className="flex items-center gap-2 px-2 py-3 rounded-lg hover:bg-secondary cursor-pointer"
          >
            <dataStructure.icon className="text-accent" />
            <p className="text-gray-300 text-sm font-semibold px-1">
              {dataStructure.name}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Sidebar;
