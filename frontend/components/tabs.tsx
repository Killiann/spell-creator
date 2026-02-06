"use client";

import { useState } from "react";

type Tab = {
    label: string;
    content: React.ReactNode;
}

export default function Tabs({ tabs }: { tabs: Tab[] }) {
    const[activeIndex, setActiveIndex] = useState(0);

  return (
    <div className="flex flex-col h-full">
      {/* Tab buttons */}
      <div className="flex border-b shrink-0">
        {tabs.map((tab, index) => (
          <button
            key={index}
            onClick={() => setActiveIndex(index)}
            className={`px-4 py-2 transition ${
              activeIndex === index
                ? "border-b-2 border-black font-semibold"
                : "text-gray-500"
            }`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Tab content */}
      <div className="flex-1 min-h-0 overflow-auto p-4">
        {tabs[activeIndex].content}
      </div>
    </div>
  );
}