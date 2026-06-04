import React from "react";

const QTajwid = () => {
  return (
    <div style={{ position: "fixed", inset: 0, width: "100vw", height: "100vh", zIndex: 0 }}>
      <iframe
        src="/qtajwid/index.html"
        title="Q Tajwid — Belajar Huruf Hijaiyah"
        style={{ width: "100%", height: "100%", border: "none", display: "block" }}
        allow="autoplay"
      />
    </div>
  );
};

export default QTajwid;
