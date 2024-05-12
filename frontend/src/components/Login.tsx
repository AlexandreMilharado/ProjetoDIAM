import axios from "axios";
import { FormEvent, useState } from "react";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState("");
  const [error, setError] = useState("");

  async function handleLogin(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    axios
      .post(`http://localhost:8000/login/`, { username, password })
      .then((response) => {
        localStorage.setItem('token', response.data.token);       
      })
      .catch((error) => setError(error));
  }
  return (
    <section>
      <h2>Login</h2>
      {error && <p>{error}</p>}
      <p>{msg}</p>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
    </section>
  );
}

export default Login;
