// src/App.js
import React, { useState } from 'react';
import DataLoader from './components/DataLoader';
import PlotComponent from './components/PlotComponent';
import './App.css'

const App = () => {
  const [plotData, setPlotData] = useState([]);
  const [plotHeaders, setPlotHeaders] = useState([]);

  const handleDataLoad = (data, headers) => {
    setPlotData(data);
    setPlotHeaders(headers);
  };

  return (
    <div>
      <div>
      <h1 className="title">Analyzer</h1>
      </div>
      <DataLoader onDataLoad={handleDataLoad} />
      <PlotComponent data={plotData} headers={plotHeaders} />
    </div>
  );
};
export default App;
