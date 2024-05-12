import axios from 'axios';
import  { ReactNode, useEffect, useState } from 'react'
import backendURL from '../api';
import { useNavigate } from 'react-router-dom';

type PlaceDetailProps = {
  placeId? : string,
  
}



const PlaceDetail = ({placeId} : PlaceDetailProps) : ReactNode  => {
  
  const [place,setPlace] = useState<Place>();
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchPlace() {
      try {
        const {data} = await axios.get(`${backendURL}/api/getPlace/${placeId}`);
        if(data.place)
          setPlace(data.place)
        else
        navigate("placeNotExist"); 
      }catch(err){
        navigate("placeNotExist");   
      }
    
    }
    fetchPlace()
  },[])

  return (
    <div>Detail</div>
  )
}

export default PlaceDetail