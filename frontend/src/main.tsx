import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './styles.css'
import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import ErrorPage from './routes/ErrorPage.tsx';
import MainPage from './routes/MainPage.tsx';
import Login from './routes/Login.tsx';


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
