import React from "react";

const ServiceCard = ({ title, description, link, icon }) => {
  return (
    <div className="group bg-white dark:bg-gray-800 rounded-2xl p-8 hover:shadow-2xl transition-all duration-300 border border-gray-100 dark:border-gray-700 hover:-translate-y-1 flex flex-col h-full relative overflow-hidden">
      <div className="absolute top-0 right-0 w-32 h-32 bg-yellow-50 dark:bg-yellow-900/20 rounded-bl-full -mr-10 -mt-10 transition-transform group-hover:scale-110"></div>

      <div className="relative z-10">
        <div className="w-14 h-14 bg-yellow-100 dark:bg-yellow-900/50 rounded-xl flex items-center justify-center text-yellow-600 dark:text-yellow-400 mb-6 group-hover:bg-yellow-500 group-hover:text-white transition-colors duration-300">
          {icon || (
            <svg
              className="w-7 h-7"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
              ></path>
            </svg>
          )}
        </div>

        <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-3 group-hover:text-yellow-600 dark:group-hover:text-yellow-400 transition-colors">
          {title}
        </h3>
        <p className="text-gray-500 dark:text-gray-400 mb-6 leading-relaxed grow">{description}</p>

        <a
          href={link}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center text-yellow-600 dark:text-yellow-400 font-semibold hover:text-yellow-700 dark:hover:text-yellow-300 transition group-hover:translate-x-1"
        >
          Kunjungi Website
          <svg
            className="w-4 h-4 ml-2"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M17 8l4 4m0 0l-4 4m4-4H3"
            ></path>
          </svg>
        </a>
      </div>
    </div>
  );
};

export default ServiceCard;
