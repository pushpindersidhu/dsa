import { FaHubspot } from "react-icons/fa6";

const Navbar = () => {
  return (
    <nav className="w-full h-10 flex justify-between col-span-12">
      <div className="px-4 flex items-center">
        <FaHubspot className="text-accent-500 text-lg" />
        <div className="text-sm font-semibold text-accent-500 px-2">Sidhu</div>
      </div>
    </nav>
  );
};

export default Navbar;
