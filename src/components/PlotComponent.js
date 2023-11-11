import React, { useState } from 'react';
import Plot from 'react-plotly.js';

const PlotComponent = ({ data, headers }) => {
  const [selectedX, setSelectedX] = useState(headers[1]);
  const [selectedY, setSelectedY] = useState(headers[2]);

  const trace = {
    x: data.map((row) => row[headers.indexOf(selectedX)]),
    y: data.map((row) => row[headers.indexOf(selectedY)]),
    mode: 'markers',
    type: 'scatter',
    name: 'Scatter Plot',
  };

  const layout = {
    title: 'Scatter Plot',
    xaxis: { title: selectedX },
    yaxis: { title: selectedY },
  };

  const handleXChange = (e) => {
    setSelectedX(e.target.value);
  };

  const handleYChange = (e) => {
    setSelectedY(e.target.value);
  };

  return (
    <div>
      <label>X-axis:</label>
      <select value={selectedX} onChange={handleXChange}>
        {headers.map((header) => (
          <option key={header} value={header}>
            {header}
          </option>
        ))}
      </select>

      <label>Y-axis:</label>
      <select value={selectedY} onChange={handleYChange}>
        {headers.map((header) => (
          <option key={header} value={header}>
            {header}
          </option>
        ))}
      </select>

      <Plot data={[trace]} layout={layout} />
    </div>
  );
};

export default PlotComponent;
