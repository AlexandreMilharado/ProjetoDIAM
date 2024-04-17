import LocationSVG from "../assets/LocationSVG"

const Header = () => {
  return (
    <header>
        <figure>
            <LocationSVG/>
            On<span className="detailed">Spot</span>
        </figure>
        <nav>
            <a href='#'>Adicionados por mim</a>
            <a href='#'>Favoritos</a>
            <a href='#'>Log in</a>
        </nav>
    </header>
  )
}

export default Header