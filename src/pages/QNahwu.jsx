import React, { useState, useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import { menuData } from "../data/nahwuMenuData";
import Navbar from "../components/Navbar";

const QNahwu = () => {
  const { category, filename } = useParams();
  const [expandedMenu, setExpandedMenu] = useState(category || null);
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  // Auto-expand menu if category is present
  useEffect(() => {
    if (category) {
      setExpandedMenu(category);
    }
  }, [category]);

  const toggleMenu = (menuId) => {
    setExpandedMenu(expandedMenu === menuId ? null : menuId);
  };

  const folderMap = {
    "harf-amil": "HARF AMIL",
    "jabatan-kata": "JABATAN KATA",
    "jamid-mabny": "JAMID MABNY",
    "jamid-murab": "JAMID MU_RAB",
    shorof: "SHOROF",
  };

  const currentFolder = category ? folderMap[category] : null;
  const currentHtmlPath =
    currentFolder && filename
      ? `/html-nahwu/${currentFolder}/${decodeURIComponent(filename)}`
      : null;

  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <div className="flex h-screen pt-20">
        {/* Sidebar Toggle Button (Mobile) */}
        <button
          className={`fixed left-4 top-24 z-30 p-2 bg-emerald-600 text-white rounded-md shadow-lg md:hidden transition-all duration-300 ${
            isSidebarOpen ? "left-[260px]" : "left-4"
          }`}
          onClick={() => setIsSidebarOpen(!isSidebarOpen)}
        >
          {isSidebarOpen ? "✕" : "☰"}
        </button>

        {/* Sidebar */}
        <aside
          className={`fixed md:static inset-y-0 left-0 z-20 w-64 bg-white border-r border-gray-200 transform transition-transform duration-300 ease-in-out ${
            isSidebarOpen ? "translate-x-0" : "-translate-x-full"
          } md:translate-x-0 pt-20 md:pt-0 overflow-y-auto h-full pb-20`}
        >
          <div className="p-4 border-b border-gray-100">
            <h2 className="text-xl font-bold text-emerald-800 flex items-center gap-2">
              <span className="text-2xl">📚</span> Nahwu
            </h2>
          </div>

          <nav className="p-4 space-y-2">
            <Link
              to="/qnahwu"
              className={`flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                !category
                  ? "bg-emerald-50 text-emerald-700 font-medium"
                  : "text-gray-600 hover:bg-gray-50"
              }`}
            >
              <span>🏠</span> Beranda
            </Link>

            {menuData.map((menu) => (
              <div key={menu.id} className="space-y-1">
                <button
                  className={`w-full flex items-center justify-between px-4 py-3 rounded-lg transition-colors ${
                    expandedMenu === menu.id
                      ? "bg-emerald-50 text-emerald-700 font-medium"
                      : "text-gray-600 hover:bg-gray-50"
                  }`}
                  onClick={() => toggleMenu(menu.id)}
                >
                  <span>{menu.title}</span>
                  <span
                    className={`transform transition-transform duration-200 ${
                      expandedMenu === menu.id ? "rotate-180" : ""
                    }`}
                  >
                    ▼
                  </span>
                </button>

                {expandedMenu === menu.id && (
                  <div className="pl-4 space-y-1 border-l-2 border-emerald-100 ml-4">
                    {menu.items.map((item, index) => {
                      const isActive =
                        category === menu.id &&
                        decodeURIComponent(filename || "") === item.path;
                      return (
                        <Link
                          key={index}
                          to={`/qnahwu/${menu.id}/${encodeURIComponent(
                            item.path
                          )}`}
                          className={`block px-4 py-2 text-sm rounded-md transition-colors ${
                            isActive
                              ? "text-emerald-600 font-medium bg-white shadow-sm"
                              : "text-gray-500 hover:text-emerald-600 hover:bg-gray-50"
                          }`}
                        >
                          {item.title}
                        </Link>
                      );
                    })}
                  </div>
                )}
              </div>
            ))}
          </nav>
        </aside>

        {/* Main Content */}
        <main className="flex-1 overflow-hidden relative w-full h-full">
          {currentHtmlPath ? (
            <iframe
              src={currentHtmlPath}
              title="Materi Nahwu"
              className="w-full h-full border-none bg-white"
            />
          ) : (
            <div className="h-full flex flex-col items-center justify-center text-center p-8 bg-emerald-50/30">
              <div className="w-24 h-24 bg-emerald-100 rounded-full flex items-center justify-center mb-6 text-4xl">
                📖
              </div>
              <h1 className="text-3xl font-bold text-gray-800 mb-4">
                Selamat Datang di QNahwu
              </h1>
              <p className="text-gray-600 max-w-md leading-relaxed">
                Silakan pilih materi pembelajaran Nahwu dari menu di sebelah
                kiri untuk mulai belajar.
              </p>
            </div>
          )}
        </main>
      </div>
    </div>
  );
};

export default QNahwu;
