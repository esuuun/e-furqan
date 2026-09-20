import React from "react";
import { BrowserRouter as Router, Routes, Route, useLocation } from "react-router-dom";
import { useEffect } from "react";
import { initGA, trackPageView } from "./utils/analytics";
import Home from "./pages/Home";
import QThematic from "./pages/QThematic";
import ThemeDetail from "./pages/ThemeDetail";
import LessonDetail from "./pages/LessonDetail";
import QTahfidz from "./pages/QTahfidz";
import QMushaf from "./pages/QMushaf";
import QKamus from "./pages/QKamus";
import QNahwu from "./pages/QNahwu";
import QTajwid from "./pages/QTajwid";

function ScrollToTop() {
  const location = useLocation();

  useEffect(() => {
    window.scrollTo(0, 0);
    const fullPath = location.pathname + location.search + location.hash;
    trackPageView(fullPath);
  }, [location]);

  return null;
}

function App() {
  useEffect(() => {
    initGA();
  }, []);

  return (
    <Router>
      <ScrollToTop />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/qthematic" element={<QThematic />} />
        <Route path="/qthematic/:slug" element={<ThemeDetail />} />
        <Route
          path="/qthematic/:themeSlug/:lessonSlug"
          element={<LessonDetail />}
        />
        <Route path="/qtahfidz" element={<QTahfidz />} />
        <Route path="/qmushaf" element={<QMushaf />} />
        <Route path="/qkamus" element={<QKamus />} />
        <Route path="/qtajwid" element={<QTajwid />} />
        <Route path="/qnahwu" element={<QNahwu />} />
        <Route path="/qnahwu/:category/:filename" element={<QNahwu />} />
      </Routes>
    </Router>
  );
}

export default App;
