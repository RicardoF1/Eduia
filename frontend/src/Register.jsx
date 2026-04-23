import { useState } from "react";

function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [rol, setRol] = useState("estudiante");

  const handleRegister = async () => {
    const res = await fetch("http://127.0.0.1:8000/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ email, password, rol })
    });

    const data = await res.json();

    alert(data.mensaje || data.error);
  };

  return (
    <div>
      <h2>Registro</h2>
      <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input placeholder="Password" type="password" onChange={(e) => setPassword(e.target.value)} />
      <select onChange={(e) => setRol(e.target.value)}>
        <option value="estudiante">Estudiante</option>
        <option value="docente">Docente</option>
      </select>
      <button onClick={handleRegister}>Registrarse</button>
    </div>
  );
}

export default Register;