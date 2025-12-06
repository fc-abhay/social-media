"use client"
import Link from "next/link"
import Name from "./Name"
import { usePathname } from "next/navigation"
import Auth from "./Auth"
import { RiMenu3Line, RiCloseLine } from "react-icons/ri"
import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"

const navLinks = [
  { id: 1, name: "Home", link: "/" },
  { id: 2, name: "Trending Topics", link: "/trending" },
  { id: 3, name: "About", link: "/about" }
]

const NavNormal = () => {
  const pathname = usePathname()
  const [openNavMenu, setOpenNavMenu] = useState(false)

  return (
    <header className="w-full border-b sticky top-0 z-50 ">
      <div className="p-4 flex items-center justify-between max-w-full">
        {/* Logo */}
        <Name />

        {/* Desktop Nav */}
        <nav className="hidden md:flex">
          <ul className="flex items-center gap-8">
            {navLinks.map((item) => (
              <Link
                key={item.id}
                href={item.link}
                className={`transition font-medium tracking-wide hover:text-black/80 ${
                  pathname === item.link
                    ? "text-black font-semibold border-b-2 border-black pb-1"
                    : "text-gray-500"
                }`}
              >
                {item.name}
              </Link>
            ))}
          </ul>
        </nav>

        {/* Auth + Mobile Toggle */}
        <div className="flex items-center gap-4">
          <Auth />

          {/* Mobile Menu Icon */}
          <button
            onClick={() => setOpenNavMenu(!openNavMenu)}
            className="md:hidden p-2 rounded-lg hover:bg-gray-100 transition"
          >
            {openNavMenu ? <RiCloseLine size={28} /> : <RiMenu3Line size={28} />}
          </button>
        </div>
      </div>

      {/* Mobile Menu */}
      <AnimatePresence>
        {openNavMenu && (
          <motion.nav
            initial={{ opacity: 0, y: -15 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            transition={{ duration: 0.25 }}
            className="md:hidden border-t bg-white px-4 py-3"
          >
            <ul className="flex flex-col gap-4">
              {navLinks.map((item) => (
                <Link
                  key={item.id}
                  href={item.link}
                  onClick={() => setOpenNavMenu(false)}
                  className={`text-lg tracking-wide transition hover:text-black/80 ${
                    pathname === item.link ? "font-semibold text-black" : "text-gray-600"
                  }`}
                >
                  {item.name}
                </Link>
              ))}
            </ul>
          </motion.nav>
        )}
      </AnimatePresence>
    </header>
  )
}

export default NavNormal
