import Logo from "./Logo"

const Header = () => {

  const isLogged = false;

  return (
    <header>
        <Logo/>
        {/* <nav>
            <a href="/favorites">Favoritos</a>                
            {!isLogged && <a href="/login">Log in</a> }
            {isLogged && <a id="username-text" href="{/profile}">User</a>}
            {isLogged && <a id="username-text" href="{/logout}">Logout</a>}
        </nav> */}
        <svg className="menu-toggle" xmlns="http://www.w3.org/2000/svg" width={64} height={64} fill="none" stroke="currentColor" strokeWidth={0} viewBox="0 0 24 24"  > <path fill="currentColor" fillRule="evenodd" stroke="none" d="M2 7a1 1 0 0 1 1-1h18a1 1 0 1 1 0 2H3a1 1 0 0 1-1-1zm0 5a1 1 0 0 1 1-1h18a1 1 0 1 1 0 2H3a1 1 0 0 1-1-1zm1 4a1 1 0 1 0 0 2h18a1 1 0 1 0 0-2H3z" clipRule="evenodd" /> </svg>
    </header>
  )
}

export default Header