import { useState } from "react";
import Logo from "./Logo"
import { Link } from "react-router-dom";
import backendURL from "../api";

const Header = () => {

  const isLogged = localStorage.getItem("token") !== null;

  const [menuOpen,setMenuOpen] = useState(false);

  function logout() {
    localStorage.removeItem('token');
    window.location.reload();
  }

  return (
    <>
    <header>
        <Logo/>
        
        <svg onClick={() => setMenuOpen(true)} className="menu-toggle" xmlns="http://www.w3.org/2000/svg" width={64} height={64} fill="none" stroke="currentColor" strokeWidth={0} viewBox="0 0 24 24"  > <path fill="currentColor" fillRule="evenodd" stroke="none" d="M2 7a1 1 0 0 1 1-1h18a1 1 0 1 1 0 2H3a1 1 0 0 1-1-1zm0 5a1 1 0 0 1 1-1h18a1 1 0 1 1 0 2H3a1 1 0 0 1-1-1zm1 4a1 1 0 1 0 0 2h18a1 1 0 1 0 0-2H3z" clipRule="evenodd" /> </svg>
    </header>
    <nav className={`header-menu ${menuOpen ? "" : 'hidden'}`}>
        <figure className="profile">
        <svg xmlns="http://www.w3.org/2000/svg" width={64} height={64} fill="none" viewBox="0 0 24 24"> <g stroke="currentColor" strokeWidth={1.5}> <circle cx={12} cy={9} r={3} /> <path strokeLinecap="round" d="M17.97 20c-.16-2.892-1.045-5-5.97-5s-5.81 2.108-5.97 5" /> <path strokeLinecap="round" d="M7 3.338A9.954 9.954 0 0 1 12 2c5.523 0 10 4.477 10 10s-4.477 10-10 10S2 17.523 2 12c0-1.821.487-3.53 1.338-5" /> </g> </svg>
          <span>{isLogged ? "Joãozinho99" : "Visitante"}</span>
        </figure>
        {!isLogged ?
        <Link onClick={() => setMenuOpen(false)} className="menu-button" to={"/login"}>
          LogIn
        </Link> :
        <button onClick={() => logout()} className="menu-button">
          LogOut
        </button>}
        <svg className="close-button" onClick={() => setMenuOpen(false)} xmlns="http://www.w3.org/2000/svg" width={64} height={64} fill="none" viewBox="0 0 24 24" > <g stroke="currentColor" strokeLinecap="round" strokeWidth={1.5}> <path d="m14.5 9.5-5 5m0-5 5 5M7 3.338A9.954 9.954 0 0 1 12 2c5.523 0 10 4.477 10 10s-4.477 10-10 10S2 17.523 2 12c0-1.821.487-3.53 1.338-5" /> </g> </svg>
    </nav>
    </>
  )
}

export default Header