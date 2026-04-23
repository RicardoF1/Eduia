import { useState } from "react";
import Login from "./Login";
import Dashboard from "./Perfil";
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