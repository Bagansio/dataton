// src/DataLoader.js
import React, { useRef, useState } from 'react';
import Select from 'react-select';
import * as XLSX from 'xlsx';

const DataLoader = ({ onDataLoad }) => {
  const fileInputRef = useRef(null);

  const fileOptions = [
    { value: 'codigo_origen_df.xlsx', label: 'Code - Origin' },
    { value: 'hospital_year_purchases.xlsx', label: 'Hospital year - Purchases' },
    { value: 'year_money.xlsx', label: 'Year - Money' },
    { value: 'year_purchases.xlsx', label: 'Year - Purchase' },
    { value: 'year_tipo_average.xlsx', label: 'Year - Average type' },
    { value: 'year_tipo.xlsx', label: 'Year - Type' },

    // Add more files as needed
  ];

  const [selectedFile, setSelectedFile] = useState(null);

  const loadFile = () => {
    if (!selectedFile) {
      alert('Please select a file');
      return;
    }

    const reader = new FileReader();

    reader.onload = (event) => {
      const workbook = XLSX.read(event.target.result, { type: 'binary' });
      const sheetName = workbook.SheetNames[0];
      const sheet = workbook.Sheets[sheetName];
      const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });


      const headers = jsonData.shift();
      console.log(headers, jsonData)
      onDataLoad(jsonData, headers);
    };

    fetch(`/datasets/${selectedFile.value}`)
      .then((response) => response.blob())
      .then((blob) => {
        reader.readAsBinaryString(blob);
      });
  };

  return (
    <div>
      <div>
      <h1 className="title-load-dataset">Load your dataset</h1>
      </div>
      <Select
        className='file-selector'
        options={fileOptions}
        value={selectedFile}
        onChange={(value) => setSelectedFile(value)}
        isSearchable
        placeholder="Select a file"
      />
      <button 
      className='button-load-data'
      onClick={loadFile}>Load Data</button>
    </div>
  );
};

export default DataLoader;
