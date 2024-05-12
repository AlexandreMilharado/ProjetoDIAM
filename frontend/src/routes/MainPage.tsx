import { useEffect, useState } from "react"
import axios from "axios";
import LocationCard from "../components/LocationCard";
import backendURL from "../api";

const MainPage = () => {



  const [places,setPlaces] = useState<Place[]>([]);
  const [searchFilter, setSearchFilter] = useState("");
  


  useEffect(() => {

    async function fetchPlaces(){
      const response = await axios.get(`${backendURL}/api/getPlaces`,
      {
        headers:{'Content-Type': 'application/json'},
        params: { search: searchFilter }
      })
      if(response.data){
        console.log(response.data.result)
        setPlaces(response.data.result);
      }
    }
    fetchPlaces();
    
  },[searchFilter])


  return (
    <>
      <h3 className="main-page-title">Lugares em destaque</h3>
     {!places.length ? <h1 className="message-no-places">Não foram encontrados lugares...</h1> :
      (
        <section id="places-section" className="places">
          {places.map((place,index) => (
            <LocationCard key={index} place={place}/>
          ))}

        </section>

      )

      }
    </>
  )
}

export default MainPage