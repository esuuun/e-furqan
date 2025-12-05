import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import QThematic from "./pages/QThematic";
import ThemeDetail from "./pages/ThemeDetail";
import LessonDetail from "./pages/LessonDetail";
import QTahfidz from "./pages/QTahfidz";
import QMushaf from "./pages/QMushaf";

function App() {
  return (
    <Router>
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
      </Routes>
    </Router>
  );
}

export default App;
