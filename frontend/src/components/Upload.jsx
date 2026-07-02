import { useState } from "react";
import api from "../services/api";
import "../styles/Upload.css";

function Upload() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a PDF.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      setMessage("");

      const response = await api.post("/upload", formData);

      setMessage(response.data.message);
    } catch (error) {
      console.error(error);
      setMessage("Upload failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-container">
      <h2>📄 Upload PDF</h2>

      <input
        type="file"
        accept=".pdf"
        disabled={loading}
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button
        onClick={handleUpload}
        disabled={loading}
      >
        {loading ? (
          <>
            <span className="spinner"></span>
            Uploading...
          </>
        ) : (
          "Upload"
        )}
      </button>

      {message && (
        <p className="message">{message}</p>
      )}
    </div>
  );
}

export default Upload;