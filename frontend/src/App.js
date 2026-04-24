import { useState } from "react";
import Login from "./components/Login";
import Register from "./components/Register";
import Perfil from "./components/Perfil";
import Lab from "./components/Lab";
import "./styles/app.css";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [view, setView] = useState("login");

  if (token) return <Lab />;

  return (
    <div className="app-container">
      <div className="app-switch">
        <button
          className={view === "login" ? "tab active" : "tab"}
          onClick={() => setView("login")}
        >
          Login
        </button>

        <button
          className={view === "register" ? "tab active" : "tab"}
          onClick={() => setView("register")}
        >
          Registro
        </button>
      </div>

      {view === "login" ? (
        <Login setToken={setToken} />
      ) : (

        <Register setView={setView} />
      )}
    </div>
  );
}

export default App;


/* import { useState } from "react";
import Login from "./Login";
import Dashboard from "./perfil";
import Register from "./Register";


function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [view, setView] = useState("login");

  if (token) return <Dashboard token={token} />;

  return (
    <div>
      <button onClick={() => setView("login")}>Login</button>
      <button onClick={() => setView("register")}>Registro</button>

      {view === "login" ? (
        <Login setToken={setToken} />
      ) : (
        <Register />
      )}
    </div>
  );
}

export default App; */