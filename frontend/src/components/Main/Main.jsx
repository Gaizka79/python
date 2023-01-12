import React from "react";
import { Routes, Route } from 'react-router-dom';

import Home from './Home/Home';
import User from './User/User';
import New from "./User/New/New";
import Edit from "./User/Edit/Edit";

function Main () {
  return (
    <main className="main">
      <Routes>
        <Route element={<Home/>} exact path='/'/>
        <Route element={<User/>} path='/users'/>
        <Route element={<New/>} path='/new'/>
        <Route element={<Edit/>} path='/edit/:_id'/>
      </Routes>
    </main>
  )
}

export default Main;
