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
    xaxis: { title: selectedX, titlepad: 30},
    yaxis: { title: selectedY, titlepad: 30 },
    width: 1200, // Ajusta el ancho del gráfico
    height: 600, // Ajusta la altura del gráfico
    autosize: true, // Activa el ajuste automático del tamaño
  };

  const handleXChange = (e) => {
    setSelectedX(e.target.value);
  };

  const handleYChange = (e) => {
    setSelectedY(e.target.value);
  };

  return (
    <div className="plot-container">
      <div className="plot-controls">
        <label className='plot-axis'>X-axis:</label>
        <select value={selectedX} onChange={handleXChange}>
          {headers.map((header) => (
            <option key={header} value={header}>
              {header}
            </option>
          ))}
        </select>

        <label className='plot-axis'>Y-axis:</label>
        <select value={selectedY} onChange={handleYChange}>
          {headers.map((header) => (
            <option key={header} value={header}>
              {header}
            </option>
          ))}
        </select>
      </div>

      <div className="plot-graph">
        <Plot data={[trace]} layout={layout} />
      </div>
    </div>
  );
};


export default PlotComponent;
