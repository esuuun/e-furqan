import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import logo from "../assets/logo.png";

const Navbar = () => {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <nav
      className={`fixed w-full top-0 z-50 transition-all duration-300 ${
        scrolled ? "bg-white/80 backdrop-blur-md shadow-sm" : "bg-transparent"
      }`}
    >
      <div className="container mx-auto px-6 py-4 flex justify-between items-center">
        <Link to="/" className="flex items-center gap-2">
          <img
            src={logo}
            alt="e-Furqan Logo"
            className="w-10 h-10 object-contain"
          />
          <span className="text-2xl font-bold text-gray-800 tracking-tight">
            e-Furqan
          </span>
        </Link>

        <div className="hidden md:flex items-center space-x-8">
          <Link
            to="/"
            className="text-gray-600 hover:text-emerald-600 font-medium transition"
          >
            Home
          </Link>
          <a
            href="/#services"
            className="text-gray-600 hover:text-emerald-600 font-medium transition"
          >
            Layanan
          </a>
          <a
            href="/#features"
            className="text-gray-600 hover:text-emerald-600 font-medium transition"
          >
            Fitur
          </a>
          <a
            href="/#contact"
            className="text-gray-600 hover:text-emerald-600 font-medium transition"
          >
            Kontak
          </a>
        </div>

        {/* <div className="hidden md:flex items-center space-x-4">
          <button className="text-gray-600 hover:text-emerald-600 font-medium transition">
            Masuk
          </button>
          <button className="bg-emerald-600 text-white px-5 py-2.5 rounded-full font-medium hover:bg-emerald-700 transition shadow-lg shadow-emerald-600/20">
            Daftar Sekarang
          </button>
        </div> */}

        <button className="md:hidden text-gray-600 focus:outline-none">
          <svg
            className="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M4 6h16M4 12h16m-7 6h7"
            ></path>
          </svg>
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
