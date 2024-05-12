import axios from "axios";
import { useEffect, useState } from "react";
import Tag from "./Tag";

interface LocationCardProps {
    place : Place;
}
const backendUrl = import.meta.env.VITE_BACKEND_URL



const LocationCard = ({place} : LocationCardProps) => {

  const [tags, setTags] = useState<Tag[]>([]);
  const [isFavorite, setIsFavorite] = useState(false);
  useEffect(() => {
    async function fetchTags() {
      const {data} = await 
      axios.get(`${backendUrl}/api/${place.id}/getBestTags`,
        {
          params: {
            per_page: 3
          }
        })
      if(data){
        setTags(data.result);
      }    
    }
    fetchTags()
  },[])


  function getHeartsNumber() : string[] {
    const aux = []
    for(let i = 0 ; i < Math.floor(place.rating/2) ; i++ ){
      aux.push(""+i)
    }
    return aux;
  }


  async function likeOrUnlike() {
    setIsFavorite(!isFavorite);
    const token = localStorage.getItem('token');
    const response =  await axios.post(`${backendUrl}/api/${place.id}/favorite`,{},
    {
      headers: {
        'Authorization': `Bearer ${token}`
    }
    }    
    )
    console.log(response);
  }


  return (
    <section className="place">
      <h3 className="place-title">{place.title}</h3>
      <aside>
        <span className="place-location"><svg xmlns="http://www.w3.org/2000/svg" xmlSpace="preserve" viewBox="0 0 64 64" > <path fill="currentColor" d="M32 0C18.746 0 8 10.746 8 24c0 5.219 1.711 10.008 4.555 13.93.051.094.059.199.117.289l16 24a4.001 4.001 0 0 0 6.656 0l16-24c.059-.09.066-.195.117-.289C54.289 34.008 56 29.219 56 24 56 10.746 45.254 0 32 0zm0 32a8 8 0 1 1 0-16 8 8 0 0 1 0 16z" /></svg>
        {place.location}</span>
        <div className="rating-container">
          {getHeartsNumber().map((key) => <svg key={key} width="64px" height="64px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" transform="matrix(1, 0, 0, 1, 0, 0)rotate(0)"><g id="SVGRepo_bgCarrier" strokeWidth="0"></g><g id="SVGRepo_tracerCarrier" strokeLinecap="round" strokeLinejoin="round" stroke="#CCCCCC" strokeWidth="0.4800000000000001"></g><g id="SVGRepo_iconCarrier"> <path d="M11.2691 4.41115C11.5006 3.89177 11.6164 3.63208 11.7776 3.55211C11.9176 3.48263 12.082 3.48263 12.222 3.55211C12.3832 3.63208 12.499 3.89177 12.7305 4.41115L14.5745 8.54808C14.643 8.70162 14.6772 8.77839 14.7302 8.83718C14.777 8.8892 14.8343 8.93081 14.8982 8.95929C14.9705 8.99149 15.0541 9.00031 15.2213 9.01795L19.7256 9.49336C20.2911 9.55304 20.5738 9.58288 20.6997 9.71147C20.809 9.82316 20.8598 9.97956 20.837 10.1342C20.8108 10.3122 20.5996 10.5025 20.1772 10.8832L16.8125 13.9154C16.6877 14.0279 16.6252 14.0842 16.5857 14.1527C16.5507 14.2134 16.5288 14.2807 16.5215 14.3503C16.5132 14.429 16.5306 14.5112 16.5655 14.6757L17.5053 19.1064C17.6233 19.6627 17.6823 19.9408 17.5989 20.1002C17.5264 20.2388 17.3934 20.3354 17.2393 20.3615C17.0619 20.3915 16.8156 20.2495 16.323 19.9654L12.3995 17.7024C12.2539 17.6184 12.1811 17.5765 12.1037 17.56C12.0352 17.5455 11.9644 17.5455 11.8959 17.56C11.8185 17.5765 11.7457 17.6184 11.6001 17.7024L7.67662 19.9654C7.18404 20.2495 6.93775 20.3915 6.76034 20.3615C6.60623 20.3354 6.47319 20.2388 6.40075 20.1002C6.31736 19.9408 6.37635 19.6627 6.49434 19.1064L7.4341 14.6757C7.46898 14.5112 7.48642 14.429 7.47814 14.3503C7.47081 14.2807 7.44894 14.2134 7.41394 14.1527C7.37439 14.0842 7.31195 14.0279 7.18708 13.9154L3.82246 10.8832C3.40005 10.5025 3.18884 10.3122 3.16258 10.1342C3.13978 9.97956 3.19059 9.82316 3.29993 9.71147C3.42581 9.58288 3.70856 9.55304 4.27406 9.49336L8.77835 9.01795C8.94553 9.00031 9.02911 8.99149 9.10139 8.95929C9.16534 8.93081 9.2226 8.8892 9.26946 8.83718C9.32241 8.77839 9.35663 8.70162 9.42508 8.54808L11.2691 4.41115Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"></path> </g></svg> )}
          {place.rating%2 != 0 && <svg width="64px" height="64px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" strokeWidth="0"></g><g id="SVGRepo_tracerCarrier" strokeLinecap="round" strokeLinejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M8.30595 19.371L12.0008 16.7999L12.0008 4.44753V4.44752C12.0008 4.18078 12.0008 4.0474 11.9674 4.01758C11.9387 3.99199 11.8979 3.98509 11.8624 3.99986C11.821 4.01705 11.7772 4.14304 11.6897 4.395L9.94998 9.39985C9.8841 9.58938 9.85116 9.68414 9.7918 9.75471C9.73936 9.81706 9.67249 9.86564 9.597 9.89625C9.51154 9.93089 9.41123 9.93294 9.21063 9.93702L5.26677 10.0174C4.56191 10.0318 4.20949 10.0389 4.06884 10.1732C3.94711 10.2894 3.892 10.459 3.92218 10.6246C3.95706 10.8158 4.23795 11.0288 4.79975 11.4547L7.94316 13.8379C8.10305 13.9591 8.183 14.0197 8.23177 14.098C8.27486 14.1671 8.3004 14.2457 8.30618 14.327C8.31272 14.419 8.28367 14.515 8.22556 14.707L7.08328 18.4827C6.87913 19.1575 6.77706 19.4949 6.86127 19.6702C6.93416 19.8218 7.07846 19.9267 7.24523 19.9491C7.43793 19.9751 7.72727 19.7737 8.30595 19.371Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"></path> </g></svg> }
        </div> 
      </aside>
      <figure className="place-image-container">
        {/* <img src={"https://media.istockphoto.com/id/1354776457/vector/default-image-icon-vector-missing-picture-page-for-website-design-or-mobile-app-no-photo.jpg?s=612x612&w=0&k=20&c=w3OW0wX3LyiFRuDHo9A32Q0IUMtD4yjXEvQlqyYk9O4="} alt="place"/> */}
        <img src={`${backendUrl}/static${place.mainImage}`} alt="place"/>
          <svg onClick={() => likeOrUnlike()} style={{display:(isFavorite ?  "" : "none")}}  className="heart" width="800px" height="800px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#e42121" transform="rotate(0)"><g id="SVGRepo_bgCarrier" strokeWidth="0"/><g id="SVGRepo_tracerCarrier" strokeLinecap="round" strokeLinejoin="round"/><g id="SVGRepo_iconCarrier"> <path d="M2 9.1371C2 14 6.01943 16.5914 8.96173 18.9109C10 19.7294 11 20.5 12 20.5C13 20.5 14 19.7294 15.0383 18.9109C17.9806 16.5914 22 14 22 9.1371C22 4.27416 16.4998 0.825464 12 5.50063C7.50016 0.825464 2 4.27416 2 9.1371Z" fill="#e42121"/> </g></svg>
          <svg onClick={() => likeOrUnlike()} style={{display:(!isFavorite ?  "" : "none")}} className="heart" width="64px" height="64px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" strokeWidth="0"></g><g id="SVGRepo_tracerCarrier" strokeLinecap="round" strokeLinejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fillRule="evenodd" clipRule="evenodd" d="M12 6.00019C10.2006 3.90317 7.19377 3.2551 4.93923 5.17534C2.68468 7.09558 2.36727 10.3061 4.13778 12.5772C5.60984 14.4654 10.0648 18.4479 11.5249 19.7369C11.6882 19.8811 11.7699 19.9532 11.8652 19.9815C11.9483 20.0062 12.0393 20.0062 12.1225 19.9815C12.2178 19.9532 12.2994 19.8811 12.4628 19.7369C13.9229 18.4479 18.3778 14.4654 19.8499 12.5772C21.6204 10.3061 21.3417 7.07538 19.0484 5.17534C16.7551 3.2753 13.7994 3.90317 12 6.00019Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"></path> </g></svg>                 
      </figure>
      
      <section>
          <ul className="tag-list">
             { tags.length ? tags.map((tag,index) => <Tag key={index} tag={tag} displayNumber={false}/>) : <Tag tag={{name:"New"}} displayNumber={false}/>}
          </ul> 
      </section>

        
    </section>
  )
}

export default LocationCard