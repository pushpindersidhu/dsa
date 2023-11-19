import { FaHubspot } from "react-icons/fa6";

const Navbar: React.FC<{ onSubmit: () => void }> = ({ onSubmit }) => {
  return (
    <nav className="w-full h-10 flex justify-between col-span-12">
      <div className="px-4 flex items-center">
        <FaHubspot className="text-accent-500 text-lg" />
        <div className="text-sm font-semibold text-accent-500 px-2">Sidhu</div>
      </div>

      <div className="px-4 flex items-center">
        <button
          className="bg-accent-500 text-white px-4 py-2 rounded-md text-sm font-semibold"
          onClick={onSubmit}
        >
          Submit
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
