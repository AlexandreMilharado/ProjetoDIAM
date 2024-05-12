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
            <svg id="search-submit" width="64px" height="64px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M11 6C13.7614 6 16 8.23858 16 11M16.6588 16.6549L21 21M19 11C19 15.4183 15.4183 19 11 19C6.58172 19 3 15.4183 3 11C3 6.58172 6.58172 3 11 3C15.4183 3 19 6.58172 19 11Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
          </form>
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