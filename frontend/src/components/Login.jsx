import { useState } from "react";
import { loginRequest } from "../api/auth";
import "../styles/login.css";
import "../styles/global.css";

export default function Login({ setToken }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    try {
      const data = await loginRequest(email, password);

      if (data.access_token) {
        localStorage.setItem("token", data.access_token);
        setToken(data.access_token);
      } else {
        alert("Credenciales incorrectas");
      }
    } catch (error) {
      alert("Error de conexión con el servidor");
    }
  };

  return (
    <div className="center-screen">
      <div className="login-card">
        <h2 className="login-title">Iniciar sesión</h2>

        <div className="form-group">
          <input
            className="login-input"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>

        <div className="form-group">
          <input
            className="login-input"
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        <button className="login-button" onClick={handleLogin}>
          Entrar
        </button>
      </div>
    </div>
  );
}