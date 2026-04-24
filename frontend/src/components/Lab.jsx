import { useState } from "react";
import { trainFileRequest } from "../api/ml";
import "../styles/lab.css";

export default function Lab() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleTrain = async () => {
    if (!file) {
      alert("Selecciona un archivo CSV");
      return;
    }

    setLoading(true);

    try {
      const data = await trainFileRequest(file);
      setResult(data);
    } catch (error) {
      alert("Error al entrenar");
    }

    setLoading(false);
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.reload();
  };

  return (
    <div className="lab-container">

      {/* Navbar */}
      <div className="lab-navbar">
        <h2>EduIA Lab</h2>
        <button onClick={handleLogout}>Cerrar sesión</button>
      </div>

      <div className="lab-card">

        <h3 className="lab-title">Laboratorio de Inteligencia Artificial</h3>

        {/* Upload */}
        <input
          type="file"
          accept=".csv"
          className="lab-input"
          onChange={(e) => setFile(e.target.files[0])}
        />

        {/* Button */}
        <button className="lab-button" onClick={handleTrain}>
          {loading ? "Entrenando..." : "Entrenar modelo"}
        </button>

        {/* Resultados */}
        {result && (
          <>
            <div className="lab-result">
              <h4>Accuracy</h4>
              <p>{result.accuracy.toFixed(4)}</p>
              <small>ID Modelo: {result.model_id}</small>
            </div>

            <div className="table-container">
              <table className="lab-table">
                <thead>
                  <tr>
                    <th>Real</th>
                    <th>Predicción</th>
                  </tr>
                </thead>
                <tbody>
                  {result.y_real.map((val, i) => (
                    <tr key={i}>
                      <td>{val}</td>
                      <td>{result.y_pred[i].toFixed(2)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </>
        )}

      </div>
    </div>
  );
}