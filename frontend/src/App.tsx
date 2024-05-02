// import HelloWorld from "./HelloWorld";
import Header from "./components/Header";
import LocationCard from "./components/LocationCard";

function App() {
  return (
    <div>
      <Header/>
      <div className="test-div">
        <LocationCard place={{id:0,title:"Sitio de teste Spot fixe", location:"Lisboa",reviewNumber:4,rating:8,description:"Sitio calmo",image:"https://www.cm-amadora.pt/images/DESPORTO_LAZER/PARQUES_JARDINS/PARQUE_FANTASIA/1.jpg"}}></LocationCard>
      </div>
      {/* <HelloWorld /> */}
    </div>
  );
}

export default App;
