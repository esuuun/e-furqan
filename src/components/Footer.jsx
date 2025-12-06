import React from "react";
import logo from "../assets/logo.png";

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-gray-300 py-16 border-t border-gray-800">
      <div className="container mx-auto px-6">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12 mb-12">
          {/* Brand Column */}
          <div>
            <div className="flex items-center gap-2 mb-6">
              <img
                src={logo}
                alt="e-Furqan Logo"
                className="w-10 h-10 object-contain"
              />
              <span className="text-2xl font-bold text-white tracking-tight">
                e-Furqan
              </span>
            </div>
            <p className="text-gray-400 mb-6 leading-relaxed">
              Platform pembelajaran Al-Qur'an terintegrasi yang memudahkan umat
              untuk mempelajari, memahami, dan mengamalkan Al-Qur'an.
            </p>
            {/* <div className="flex space-x-4">
              {[1, 2, 3, 4].map((i) => (
                <a
                  key={i}
                  href="#"
                  className="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center hover:bg-emerald-600 transition text-white"
                >
                  <svg
                    className="w-5 h-5"
                    fill="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z" />
                  </svg>
                </a>
              ))}
            </div> */}
          </div>

          {/* Links Column 1 */}
          <div>
            <h4 className="text-white font-bold text-lg mb-6">Layanan</h4>
            <ul className="space-y-4">
              <li>
                <a href="#" className="hover:text-emerald-500 transition">
                  qThematic
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-emerald-500 transition">
                  qTajwid
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-emerald-500 transition">
                  qTahfidz
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-emerald-500 transition">
                  qNahwu
                </a>
              </li>
            </ul>
          </div>

          {/* Links Column 2 */}
          <div>
            <h4 className="text-white font-bold text-lg mb-6">Perusahaan</h4>
            <ul className="space-y-4">
              <li>
                <a href="#" className="hover:text-emerald-500 transition">
                  Tentang Kami
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-emerald-500 transition">
                  Karir
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-emerald-500 transition">
                  Blog
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-emerald-500 transition">
                  Kontak
                </a>
              </li>
            </ul>
          </div>

          {/* Newsletter Column */}
          {/* <div>
            <h4 className="text-white font-bold text-lg mb-6">Berlangganan</h4>
            <p className="text-gray-400 mb-4">
              Dapatkan update terbaru tentang fitur dan artikel islami.
            </p>
            <form className="flex flex-col gap-3">
              <input
                type="email"
                placeholder="Email Anda"
                className="bg-gray-800 text-white px-4 py-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-600 border border-gray-700"
              />
              <button className="bg-emerald-600 text-white px-4 py-3 rounded-lg font-semibold hover:bg-emerald-700 transition">
                Subscribe
              </button>
            </form>
          </div> */}
        </div>

        <div className="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center">
          <p className="text-gray-500 text-sm mb-4 md:mb-0">
            &copy; {new Date().getFullYear()} e-Furqan. All rights reserved.
          </p>
          <div className="flex space-x-6 text-sm text-gray-500">
            <a href="#" className="hover:text-white transition">
              Privacy Policy
            </a>
            <a href="#" className="hover:text-white transition">
              Terms of Service
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
