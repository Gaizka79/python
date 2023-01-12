import './styles/styles.scss';
import { BrowserRouter } from 'react-router-dom';
import { useState } from 'react';
import React from 'react';

import { userContext } from './context/userContext';

import Header from './components/Header';
import Main from './components/Main';
import Footer from './components/Footer';

function App() {

  const [ users, setUsers ] = useState([]);

  const data = {
    users,
    setUsers
  };
  
  return (
    <div className="App">
      <BrowserRouter>
        <Header/>
        <userContext.Provider value={data}>
          <Main/>
        </userContext.Provider>
      </BrowserRouter>
      <Footer/>
    </div>
  );
}

export default App;
