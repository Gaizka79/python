import React, { useContext } from "react";
import { Link } from "react-router-dom";

import { userContext } from "../../../context/userContext";
import axios from "axios";

function User (props) {
  const { setUsers } = useContext(userContext);
  const { username, email, id } = props.value;
  
  //var BASE_URL = "https://backend2-q0hm.onrender.com/usersdb/"

  const handleDelete = async (event) => {
    event.preventDefault();
    console.log(event);
    console.log(id);
    try {
      axios.delete(`https://backend2-q0hm.onrender.com/usersdb/${id}`)
        .then((response) => console.log(response.data))
      
      const resp = await axios.get("https://backend2-q0hm.onrender.com/usersdb/")
      setUsers(resp.data)
      
    } catch (error) {
      console.error(`Error: ${error}`);
    }
  }
  
  return (
    <article className="user">
        <p className="_id">Id: {id}</p>
        <h2>{username}</h2>
        <p><b>email:</b> {email}</p>
        <div className="edit_buttons">
          <Link to={`/edit/${id}`}><button className="button"><b>Editar</b></button></Link>
          <button className="button" onClick={handleDelete}><b>Borrar</b></button>
        </div>
    </article>
  )
}

export default User;
