import { useState } from "react";
import { registerRequest } from "../api/auth";
import "../styles/register.css";
import "../styles/global.css";

export default function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [rol, setRol] = useState("Estudiante");

  const handleRegister = async () => {
    try {
      const data = await registerRequest(email, password, rol);
      alert(data.mensaje || "Usuario creado");
    } catch (error) {
      alert("Error al registrar");
    }
  };

  return (
    <div className="center-screen">
      <div className="register-card">
        <h2 className="register-title">Crear cuenta</h2>

        <div className="form-group">
          <input
            className="register-input"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>

        <div className="form-group">
          <input
            className="register-input"
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        <div className="form-group">
          <select
            className="register-input"
            value={rol}
            onChange={(e) => setRol(e.target.value)}
          >
            <option value="Estudiante">Estudiante</option>
            <option value="Profesor">Profesor</option>
          </select>
        </div>

        <button className="register-button" onClick={handleRegister}>
          Registrarse
        </button>
      </div>
    </div>
  );
}