import React from "react";
import { Link } from "react-router-dom";

function Nav () {

  return (
    <nav>
      <Link to={"/new"}><button className="button"><b>Nuevo</b></button></Link>
      <Link to={"/"}><button className="button"><b>Home</b></button></Link>
    </nav>
  )
}

export default Nav;
