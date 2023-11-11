// src/App.js
import React, { useState } from 'react';
import DataLoader from './components/DataLoader';
import PlotComponent from './components/PlotComponent';

const App = () => {
  const [plotData, setPlotData] = useState([]);
  const [plotHeaders, setPlotHeaders] = useState([]);

  const handleDataLoad = (data, headers) => {
    setPlotData(data);
    setPlotHeaders(headers);
  };

  return (
    <div>
      <DataLoader onDataLoad={handleDataLoad} />
      <PlotComponent data={plotData} headers={plotHeaders} />
    </div>
  );
};
export default App;
