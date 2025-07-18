import React, { useState } from "react";
import axios from "axios";
import "./index.css";

function App() {
  const [transcript, setTranscript] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!transcript.trim()) {
      alert("Please enter a transcript.");
      return;
    }

    const formData = new FormData();
    formData.append("transcript", transcript);

    try {
      setLoading(true);
      const res = await axios.post("http://localhost:8000/summarize/", formData);
      console.log("✅ API Response:", res.data);

      if (res.data.summary) {
        setSummary(res.data.summary);
      } else if (res.data.error) {
        setSummary("❌ Error: " + res.data.error);
      } else {
        setSummary("⚠️ No summary returned from server.");
      }
    } catch (err) {
      console.error("❌ API Call Failed:", err);
      setSummary("❌ API error: Could not fetch summary.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>AI Meeting Summary Generator</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="transcript">Paste your meeting transcript below:</label>
        <textarea
          id="transcript"
          rows="10"
          value={transcript}
          onChange={(e) => setTranscript(e.target.value)}
          placeholder="Enter transcript text here..."
        />
        <button type="submit" disabled={loading}>
          {loading ? "Generating..." : "Generate Summary"}
        </button>
      </form>

      {summary && (
        <div className="summary-box">
          <h2>Summary:</h2>
          <pre>{summary}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
