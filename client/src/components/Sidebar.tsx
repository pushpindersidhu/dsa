import { PiTreeStructureFill } from "react-icons/pi";
import { RiStackFill } from "react-icons/ri";
import { HiMiniQueueList } from "react-icons/hi2";
import { FaLink } from "react-icons/fa6";
import { TbBinaryTree } from "react-icons/tb";
import { PiGraphFill } from "react-icons/pi";
import { FaHashtag } from "react-icons/fa6";
import IDSA from "../../interfaces/IDSA";
import React from "react";
import { IconType } from "react-icons";

const Sidebar: React.FC<{
  dsa: IDSA[];
  selectedDsa: IDSA | undefined;
  setSelectedDsa: (dsa: IDSA) => void;
}> = ({ dsa, selectedDsa, setSelectedDsa }) => {
  const icons: { [key: string]: IconType } = {
    Stack: RiStackFill,
    Queue: HiMiniQueueList,
    "Linked List": FaLink,
    "Doubly Linked List": FaLink,
    "Binary Tree": TbBinaryTree,
    "Binary Search Tree": PiTreeStructureFill,
    Graph: PiGraphFill,
    "Hash Table": FaHashtag,
  };

  return (
    <div className="bg-primary col-span-2 rounded-lg overflow-hidden">
      <h3 className="text-gray-300 text-sm font-semibold px-4 flex items-center bg-secondary py-2">
        <PiTreeStructureFill className="inline-block mr-2 text-accent" />
        Data Structures
      </h3>

      <div className="flex flex-col gap-2 my-4 mx-2">
        {dsa.map((d) => (
          <div
            key={d.id}
            onClick={() => setSelectedDsa(d)}
            className={
              "flex items-center gap-2 px-2 py-3 rounded-lg hover:bg-secondary cursor-pointer" +
              (selectedDsa?.id === d.id ? " bg-secondary" : "")
            }
          >
            {React.createElement(icons[d.name], {
              className: "text-accent",
            })}

            <p className="text-gray-300 text-sm font-semibold px-1">{d.name}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Sidebar;
