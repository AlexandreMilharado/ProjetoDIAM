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
        setPlaces(response.data.result);
      }
    }
    fetchPlaces();
    
  },[searchFilter])


  return (
    <>
        <section className="search-input-container">
          <form id="searchForm">
            <input value={searchFilter} onChange={(e) => setSearchFilter(e.target.value)} id="search" className="search-input" type="text" placeholder="Pesquisar..." />
            <svg xmlns="http://www.w3.org/2000/svg" width={64} height={64} fill="none" viewBox="0 0 24 24" > <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 6a5 5 0 0 1 5 5m.659 5.655L21 21m-2-10a8 8 0 1 1-16 0 8 8 0 0 1 16 0Z" /> </svg>          </form>
        </section>
     {!places.length ? <h1 className="message-no-places">Não foram encontrados lugares...</h1> :
      (
        <section id="places-section" className="places">
         <h4 className="main-page-title">Lugares em destaque</h4>
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