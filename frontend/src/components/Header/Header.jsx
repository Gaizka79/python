import React from "react";

import logo from '../../logo.svg';
import Nav from './Nav/Nav';

import mongo from '../../assets/mongodb_logo.png';
import python from '../../assets/python_logo.png';
import react_logo from '../../assets/react_logo.png';
import fastApi from '../../assets/fastapi_logo.png';

function Header () {

  return (
    <>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <div className="logos">
          <img src={mongo} alt="mongo logo" className="logo"/>
          <img src={python} alt="python logo" className="logo"/>
          <img src={react_logo} alt="react_logo logo" className="logo"/>   
          <img src={fastApi} alt="fastApi logo" className="logo"/>    
          
        </div>
        <img src={logo} className="App-logo reverse" alt="logo" />
      </header>
      <Nav/>
    </>
  )
}

export default Header;
