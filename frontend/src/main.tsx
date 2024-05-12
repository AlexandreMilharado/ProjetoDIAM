import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './styles.css'
import { RouterProvider, createBrowserRouter, useParams } from 'react-router-dom';
import ErrorPage from './routes/ErrorPage.tsx';
import MainPage from './routes/MainPage.tsx';
import Login from './routes/Login.tsx';
import PlaceDetail from './routes/PlaceDetail.tsx';

const PlaceDetailWrapper = () => {
  const { id } = useParams();
  return <PlaceDetail placeId={id}/>;
};


const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "",
        element: <MainPage />,
      },
      {
        path: "/detail/:id",
        element:<PlaceDetailWrapper/>,
      },
    ],
  },
  {
    path: "/login",
    element: <Login />
  }
]);



ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
     <RouterProvider router={router} />
  </React.StrictMode>,
)
