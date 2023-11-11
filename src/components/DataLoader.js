// src/DataLoader.js
import React, { useRef, useState } from 'react';
import Select from 'react-select';
import * as XLSX from 'xlsx';

const DataLoader = ({ onDataLoad }) => {
  const fileInputRef = useRef(null);

  const fileOptions = [
    { value: 'modified_dataset.xlsx', label: 'Dataset 1' },
    { value: 'file2.xlsx', label: 'File 2' },
    { value: 'file3.xlsx', label: 'File 3' },
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
      <Select
        options={fileOptions}
        value={selectedFile}
        onChange={(value) => setSelectedFile(value)}
        isSearchable
        placeholder="Select a file"
      />
      <button onClick={loadFile}>Load Data</button>
    </div>
  );
};

export default DataLoader;
