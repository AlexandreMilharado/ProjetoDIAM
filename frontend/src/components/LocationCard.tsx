interface LocationCardProps {
    place : Place;

}



const LocationCard = ({place} : LocationCardProps) => {
  return (
    <article className="place-card">
        <img src={place.image} alt="Place"/>
        {place.title}
    
    </article>
  )
}

export default LocationCard