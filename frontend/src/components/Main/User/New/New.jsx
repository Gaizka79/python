import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";

import axios from "axios";

function New () {

  const [ values, setValues ] = useState({
    username: "",
    email: ""
  });

  const { register, handleSubmit } = useForm();
  let navigate = useNavigate();

  const [ message, setMessage ] = useState(null);

  const onSubmit = async () => {
    try {
      await axios.post("https://backend2-q0hm.onrender.com/usersdb/", values)
        .then((response) => console.log(response.data))
      setMessage("Usuario creado OK");
    } catch (error) {
      console.error(`Error: ${error}`);
      setMessage(error);
    }

    setTimeout(() => {
      return navigate("/", { replace: true });//
    }, 1500);
  }

  const handleChange = event => {
    event.preventDefault();
    setMessage(null);
    
    const { target } = event;
    const { name, value } = target;
    const newValues = {...values, [name]: value};
    setValues(newValues);
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="new"> {/* Añadido onSubmit */}
      <p>Crear</p>
      <label htmlFor="username">Nombre:</label>
      <input 
        {...register("username")}
        type="text"
        name="username"
        value={values.username}
        onChange={handleChange} />

      <label htmlFor="email">email:</label>
      <input 
        {...register("email")}
        type="text"
        name="email"
        value={values.email}
        onChange={handleChange} />

      <button type="submit" className="button">Añadir</button>

      {message ?
        <p>{message}</p> :
        <></>
      }
    </form>
  )
}

export default New;
