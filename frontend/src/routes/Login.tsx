import axios from "axios";
import { FormEvent, useState } from "react";
import backendURL from "../api";
import { useNavigate } from "react-router-dom";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  async function handleLogin(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    axios
      .post(`${backendURL}/login/`, { username, password })
      .then((response) => {
        localStorage.setItem('token', response.data.token);      
        navigate("/");
        window.location.reload();
      })
      .catch(() => setError("Erro de autenticação!"));
  }
  return (
    <main className="login" >
     
      <form onSubmit={handleLogin}>
        <figure>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"> <path fill="currentColor" d="M32 0C18.746 0 8 10.746 8 24c0 5.219 1.711 10.008 4.555 13.93.051.094.059.199.117.289l16 24a4.001 4.001 0 0 0 6.656 0l16-24c.059-.09.066-.195.117-.289C54.289 34.008 56 29.219 56 24 56 10.746 45.254 0 32 0zm0 32a8 8 0 1 1 0-16 8 8 0 0 1 0 16z" /> </svg>
          <span>Log</span>in
        </figure>
        {error && <p style={{color:"firebrick"}}>{error}</p>} 
        <section className="input-box">
          <input id="usernameInput" value={username} onChange={(e) => setUsername(e.target.value)} className="form-input" name="username" type="text" placeholder=" " autoComplete="off" />
          <label htmlFor="usernameInput" className="form-label">Username </label>
        </section>
        <section className="input-box">
          <input id="passwordInput" value={password} onChange={(e) => setPassword(e.target.value)} className="form-input" name="password" type="password" placeholder=" "  />
          <label htmlFor="passwordInput" className="form-label">Password</label>
        </section>
          <button type="submit">Login</button>
      </form>
    </main>
  );
}

export default Login;
