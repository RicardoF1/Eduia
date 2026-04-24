const API = "http://127.0.0.1:8000";

export const loginRequest = async (email, password) => {
  const res = await fetch(`${API}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  return res.json();
};

export const registerRequest = async (email, password, rol) => {
  const res = await fetch(`${API}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password, rol }),
  });
  return res.json();
};

export const getPerfil = async (token) => {
  const res = await fetch(`${API}/perfil`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return res.json();
};