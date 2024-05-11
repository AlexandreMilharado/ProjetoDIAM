import Logo from "./Logo"

const Header = () => {

  const isLogged = false;

  return (
    <header>
        <Logo/>
        <nav>
            <a href="/favorites">Favoritos</a>                
            {!isLogged && <a href="/login/">Log in</a> }
            {isLogged && <a id="username-text" href="{/profile}">User</a>}
            {isLogged && <a id="username-text" href="{/logout}">Logout</a>}
        </nav>
    </header>
  )
}

export default Header