import { useEffect, useState } from "react";
import { getPerfil } from "../api/auth";
import "../styles/perfil.css";

function Perfil({ token }) {
  const [user, setUser] = useState(null);

  //variable cerrar sesion
  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.reload();
  };

  useEffect(() => {
    getPerfil(token).then(data => setUser(data.usuario));
  }, [token]);

  return (
    <div className="dashboard">
      <div className="card">
        <h2>Perfil</h2>
        {user && <p>Bienvenido {user.sub}</p>}
        <button onClick={handleLogout}>Cerrar sesión</button>
      </div>
    </div>
  );
}

export default Perfil;


/* import { useEffect, useState } from "react";

function Dashboard({ token }) {
  const [user, setUser] = useState(null);

  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.reload();
  };

  useEffect(() => {
    fetch("http://127.0.0.1:8000/perfil", {
      headers: {
        Authorization: "Bearer " + token
      }
    })
      .then((res) => res.json())
      .then((data) => setUser(data));
  }, [token]);

  return (
    <div>
      <h2>Dashboard</h2>
      {user && <p>Bienvenido {user.email}</p>}
      <button onClick={handleLogout}>Cerrar sesión</button>
    </div>
  );
}

export default Dashboard;
 */

