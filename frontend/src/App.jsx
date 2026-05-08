import React from 'react';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-md max-w-md w-full">
        <h1 className="text-2xl font-bold mb-4 text-[#1B4F8A]">Tool-66: Operational Risk Event Collector</h1>
        <p className="text-gray-600 mb-6">
          This is the frontend for the capstone project. Use the dashboard to track risk events.
        </p>
        <div className="space-y-4">
          <button className="w-full bg-[#1B4F8A] text-white py-2 rounded hover:bg-[#153e6d] transition">
            View Dashboard
          </button>
          <button className="w-full border border-[#1B4F8A] text-[#1B4F8A] py-2 rounded hover:bg-blue-50 transition">
            Submit New Event
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
