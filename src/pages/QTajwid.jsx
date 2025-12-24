import React from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

const QTajwid = () => {
  return (
    <div className="min-h-screen flex flex-col bg-gray-50 dark:bg-gray-900 font-sans">
      <Navbar />
      <div className="flex-grow pt-20">
        <iframe
          src="/qtajwid/index.html"
          title="Interactive QTajwid"
          className="w-full h-[calc(100vh-80px)] border-0"
          style={{ display: "block" }}
        />
      </div>
      <Footer />
    </div>
  );
};

export default QTajwid;
