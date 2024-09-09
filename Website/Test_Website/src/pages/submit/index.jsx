import React, { useState } from 'react';

function Submit() {
  const [file, setFile] = useState(null);
  const [statusMessage, setStatusMessage] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!file) {
      setStatusMessage('Please select a file to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);  // Append the selected file

    // Make a POST request to the backend with the form data
    fetch('/api/upload', {
      method: 'POST',
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        setStatusMessage('File uploaded successfully!');
        console.log('File successfully uploaded:', data);
      })
      .catch((error) => {
        setStatusMessage('Error uploading file');
        console.error('Error uploading file:', error);
      });
  };

  return (
    <div className="container">
      <header>
        <h1>Submit Your File</h1>
      </header>

      <main>
        <section className="submission-form">
          <h2>File Submission</h2>
          <p>Please upload your file using the form below.</p>
          
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="fileUpload">Upload Your File:</label>
              <input 
                type="file" 
                id="fileUpload" 
                name="fileUpload" 
                onChange={handleFileChange} 
                required 
              />
            </div>

            <button type="submit" className="submit-btn">Submit</button>
          </form>

          {/* Display success or error message */}
          {statusMessage && <p>{statusMessage}</p>}
        </section>
      </main>

      <footer>
        <p>&copy; QuantSoc </p>
      </footer>
    </div>
  );
}

export default Submit;
