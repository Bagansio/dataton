import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';

const PlotComponent = ({ data, headers }) => {
  const [selectedX, setSelectedX] = useState(headers[0]);
  const [selectedY, setSelectedY] = useState(headers[1]);
  const [selectedZ, setSelectedZ] = useState(headers.length > 2 ? headers[2][0] : null);
  const [indexZ, setIndexZ] = useState(headers.length > 2 ? headers[2] : null);
  const [thirdHeaderOptions, setThirdHeaderOptions] = useState([]);
  const [filteredData, setFilteredData] = useState(data);
  const [isZModeEnabled, setZModeEnabled] = useState(true); // Initial state: Z mode enabled
  const [selectedMode, setSelectedMode] = useState('markers'); // Initial state: scatter mode

  useEffect(() => {
    // Filter out selected headers from available headers to get the third header options
    const remainingHeaders = headers.filter(header => header !== selectedX && header !== selectedY);

    // Find the index of the remaining header in the headers array
    const remainingHeaderIndex = headers.indexOf(remainingHeaders[0]);

    // Use the index to get the corresponding data for the third header
    if (remainingHeaderIndex !== -1) {
      setIndexZ(remainingHeaderIndex)
      const distinctValues = new Set(data.map(row => row[remainingHeaderIndex]));
      setThirdHeaderOptions([...distinctValues]);
    }
  }, [selectedX, selectedY, headers, data, setIndexZ]);

  useEffect(() => {
    // Filter the data based on the selected occurrence in selectedZ
    if (isZModeEnabled && selectedZ) {
      const filtered = data.filter(row => row[indexZ] === selectedZ);
      setFilteredData(filtered);
    } else {
      // If no selection or Z mode is disabled, use the original data
      setFilteredData(data);
    }
  }, [isZModeEnabled, selectedZ, indexZ, data, headers, thirdHeaderOptions]);

  const traces = [];

  if (isZModeEnabled) {
    // Z mode is enabled, create a single trace
    const trace = {
      x: filteredData.map((row) => row[headers.indexOf(selectedX)]),
      y: filteredData.map((row) => row[headers.indexOf(selectedY)]),
      mode: selectedMode,
      type: 'scatter',
      name: selectedZ,
    };
    traces.push(trace);
  } else {
    // Z mode is disabled, create traces for each occurrence of the 3rd value
    thirdHeaderOptions.forEach((option) => {
      const subsetData = data.filter(row => row[indexZ] === option);
      const trace = {
        x: subsetData.map((row) => row[headers.indexOf(selectedX)]),
        y: subsetData.map((row) => row[headers.indexOf(selectedY)]),
        mode: selectedMode,
        type: 'scatter',
        name: option,
      };
      traces.push(trace);
    });
  }

  const layout = {
    xaxis: { title: selectedX, titlepad: 30 },
    yaxis: { title: selectedY, titlepad: 30 },
    width: 1200,
    height: 500,
    autosize: true,
    showlegend: true,
  };

  const handleXChange = (e) => {
    setSelectedX(e.target.value);
  };

  const handleYChange = (e) => {
    setSelectedY(e.target.value);
  };

  const handleZChange = (e) => {
    setSelectedZ(e.target.value);
  };

  const handleToggleZMode = () => {
    setZModeEnabled(!isZModeEnabled);
  };

  const handleModeChange = (e) => {
    setSelectedMode(e.target.value);
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

        {headers.length > 2 && (
          <>
            <label className='plot-axis'>{headers[indexZ]}</label>
            <select value={selectedZ} onChange={handleZChange} disabled={!isZModeEnabled}>
              {thirdHeaderOptions.map((option, index) => (
                <option key={index} value={option}>
                  {option}
                </option>
              ))}
            </select>
            <button onClick={handleToggleZMode} className='button'>
              {isZModeEnabled ? 'Disable Z Mode' : 'Enable Z Mode'}
            </button>
          </>
        )}

        <label className='plot-axis'>Mode:</label>
        <select value={selectedMode} onChange={handleModeChange}>
          <option value="markers">Markers</option>
          <option value="lines">Lines</option>
          <option value="lines+markers">Lines + Markers</option>
        </select>
      </div>

      <div className="plot-graph">
        <Plot data={traces} layout={layout} />
      </div>
    </div>
  );
};

export default PlotComponent;
