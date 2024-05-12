import axios from "axios";
import { ReactNode, useEffect, useState } from "react";
import backendURL from "../api";
import { useNavigate } from "react-router-dom";

type PlaceDetailProps = {
  placeId?: string;
};

const PlaceDetail = ({ placeId }: PlaceDetailProps): ReactNode => {
  const [place, setPlace] = useState<Place>();
  const [authorPlace, setAuthorPlace] = useState<String>();
  const [isFavorite, setIsFavorite] = useState(false);

  const navigate = useNavigate();
  const token = localStorage.getItem("token")


  useEffect(() => {
    async function fetchPlace() {
      try {
        const { data } = await axios.get(
          `${backendURL}/api/getPlace/${placeId}`
        );
        if (data.place && data.author) {
          setPlace(data.place);
          setAuthorPlace(data.author);
        } else navigate("placeNotExist");
      } catch (err) {
        navigate("placeNotExist");
      }
    }
    async function fetchIsFavorite() {
      const {data} = await 
      axios.get(`${backendURL}/api/${placeId}/favorite`,{
        headers: {
          'Authorization': `Bearer ${token}`
        }
      }
      )
      if(data){
        setIsFavorite(data.result)
      }    
    }
    fetchPlace();
    fetchIsFavorite();
  }, []);

  async function likeOrUnlike() {
    const {data} =  await axios.post(`${backendURL}/api/${placeId}/favorite`,{},
    {
      headers: {
        'Authorization': `Bearer ${token}`
    }})
    if(data){
      setIsFavorite(!isFavorite);
    }
  }

  return (
    <main className="place-detail">
      <h4>{place?.title}</h4> 
      <section className="status-favorite">
        <ul>
          <li className="container-flex-center"><svg xmlns="http://www.w3.org/2000/svg" width={32} height={32} fill="none" viewBox="0 0 24 24"><path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.224} d="M11.27 4.411c.23-.52.346-.779.508-.859a.5.5 0 0 1 .444 0c.161.08.277.34.508.86l1.845 4.136c.068.154.102.23.155.29a.5.5 0 0 0 .168.121c.072.032.156.041.323.059l4.505.475c.565.06.848.09.974.218a.5.5 0 0 1 .137.423c-.026.178-.237.368-.66.75l-3.364 3.031c-.125.113-.188.17-.227.238a.5.5 0 0 0-.064.197c-.009.079.009.161.044.326l.94 4.43c.117.557.176.835.093.994a.5.5 0 0 1-.36.261c-.177.03-.423-.111-.916-.396l-3.924-2.263c-.145-.084-.218-.126-.295-.142a.502.502 0 0 0-.208 0c-.078.017-.15.058-.296.142l-3.923 2.263c-.493.285-.74.427-.917.396a.5.5 0 0 1-.36-.26c-.083-.16-.024-.438.094-.995l.94-4.43c.035-.165.052-.247.044-.326a.5.5 0 0 0-.064-.197c-.04-.069-.102-.125-.227-.238l-3.365-3.032c-.422-.38-.633-.57-.66-.749a.5.5 0 0 1 .138-.423c.126-.128.409-.158.974-.218l4.504-.475c.168-.018.251-.027.323-.059a.5.5 0 0 0 .168-.122c.053-.059.088-.135.156-.289l1.844-4.137Z" /></svg>
            {place?.reviewNumber} reviews
          </li>
          <li className="container-flex-center"><svg xmlns="http://www.w3.org/2000/svg" width={32} height={32} fill="none" viewBox="0 0 24 24"><g stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.2}><path d="M12 21c3.5-3.6 7-6.824 7-10.8C19 6.224 15.866 3 12 3s-7 3.224-7 7.2 3.5 7.2 7 10.8Z" /><path d="M12 12a2 2 0 1 0 0-4 2 2 0 0 0 0 4Z" /></g></svg>
            <p>{place?.location}</p>
          </li>
          <li className="container-flex-center"><svg xmlns="http://www.w3.org/2000/svg" width={32} height={32} fill="none" viewBox="0 0 24 24"><g stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.2}><path d="M16 7a4 4 0 1 1-8 0 4 4 0 0 1 8 0ZM12 14a7 7 0 0 0-7 7h14a7 7 0 0 0-7-7Z" /></g></svg>
            {authorPlace}
          </li>
        </ul>
        <button onClick={() => likeOrUnlike()} className={`button-like ${isFavorite ? 'liked' : ''}`} >
            <svg className={`fa fa-heart `}  width="64px" height="64px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill-rule="evenodd" clip-rule="evenodd" d="M12 6.00019C10.2006 3.90317 7.19377 3.2551 4.93923 5.17534C2.68468 7.09558 2.36727 10.3061 4.13778 12.5772C5.60984 14.4654 10.0648 18.4479 11.5249 19.7369C11.6882 19.8811 11.7699 19.9532 11.8652 19.9815C11.9483 20.0062 12.0393 20.0062 12.1225 19.9815C12.2178 19.9532 12.2994 19.8811 12.4628 19.7369C13.9229 18.4479 18.3778 14.4654 19.8499 12.5772C21.6204 10.3061 21.3417 7.07538 19.0484 5.17534C16.7551 3.2753 13.7994 3.90317 12 6.00019Z" stroke="currentColor" stroke-width="1.656" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
        </button>
      </section>
      <img width="100%" src={`${backendURL}/static${place?.mainImage}`} alt="place" />
      <p id="description-place"className="remove-input-default place-detail-description">{ place?.description }</p>
    </main>
  );
};

export default PlaceDetail;
