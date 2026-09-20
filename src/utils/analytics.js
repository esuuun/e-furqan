// Google Analytics 4 (GA4) Utility for e-Furqan
export const GA_MEASUREMENT_ID = import.meta.env.VITE_GA_MEASUREMENT_ID || "";

/**
 * Inisialisasi Google Analytics 4
 * Memuat skrip gtag.js secara dinamis jika VITE_GA_MEASUREMENT_ID tersedia
 */
export const initGA = () => {
  if (!GA_MEASUREMENT_ID || GA_MEASUREMENT_ID === "G-XXXXXXXXXX") {
    return;
  }

  if (!document.getElementById("ga-gtag-script")) {
    const script = document.createElement("script");
    script.id = "ga-gtag-script";
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${GA_MEASUREMENT_ID}`;
    document.head.appendChild(script);

    window.dataLayer = window.dataLayer || [];
    window.gtag = function () {
      window.dataLayer.push(arguments);
    };
    window.gtag("js", new Date());
    window.gtag("config", GA_MEASUREMENT_ID, {
      send_page_view: false, // Kita kirim pageview manual via Router
    });
  }
};

/**
 * Melacak perpindahan halaman (SPA Page View)
 * @param {string} path - pathname + search + hash
 * @param {string} title - document.title
 */
export const trackPageView = (path, title = document.title) => {
  if (typeof window.gtag === "function" && GA_MEASUREMENT_ID && GA_MEASUREMENT_ID !== "G-XXXXXXXXXX") {
    window.gtag("event", "page_view", {
      page_path: path,
      page_title: title,
      page_location: window.location.href,
    });
  }
};

/**
 * Melacak event interaksi kustom (opsional)
 */
export const trackEvent = (action, category, label, value) => {
  if (typeof window.gtag === "function" && GA_MEASUREMENT_ID && GA_MEASUREMENT_ID !== "G-XXXXXXXXXX") {
    window.gtag("event", action, {
      event_category: category,
      event_label: label,
      value: value,
    });
  }
};
