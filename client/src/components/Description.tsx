import { MdDescription } from "react-icons/md";

const Description: React.FC<{ desc: string }> = ({ desc }) => {
  return (
    <div className="w-full h-full">
      <h3 className="text-gray-300 text-sm font-semibold px-4 flex items-center bg-secondary py-2">
        <MdDescription className="inline-block mr-2 text-accent" />
        Description
      </h3>

      <div className="px-4 py-2 text-gray-300">
        <div dangerouslySetInnerHTML={{ __html: desc }} />
      </div>
    </div>
  );
};

export default Description;
