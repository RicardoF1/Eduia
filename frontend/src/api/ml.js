const API = "http://127.0.0.1:8000";

export const trainFileRequest = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${API}/train/file`, {
    method: "POST",
    body: formData,
  });

  return res.json();
};