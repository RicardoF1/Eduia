import { useEffect, useState } from "react";

function Dashboard({ token }) {
    const [user, setUser] = useState(null);
    
    const handleLogout = () => {
      localStorage.removeItem("token");
      window.location.reload();
    };   //variable agegada
    
  useEffect(() => {
    fetch("http://127.0.0.1:8000/perfil", {
      headers: {
        Authorization: "Bearer " + token
      }
    })
      .then((res) => res.json())
      .then((data) => setUser(data.usuario));
  }, [token]);

  return (
    <div>
      <h2>Dashboard</h2>
      {user && <p>Bienvenido {user.sub}</p>}
      <button onClick={handleLogout}>Cerrar sesión</button>
    </div>
  );
}


export default Dashboard;