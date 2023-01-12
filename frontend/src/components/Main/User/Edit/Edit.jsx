import React, { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import { useParams, useNavigate } from "react-router-dom";

import axios from "axios"; 

function Edit () {

  const params = useParams();
  const { register, handleSubmit } = useForm();
  const [ message, setMessage ] = useState(null);
  const [ values, setValues ] = useState({
    username: "",
    email: "",
  });

  const { username, email } = values
  let navigate = useNavigate();

useEffect (() => {
  const getUser = async () => {
    await axios.get(`/userdb/${params._id}`)
      .then((res) => {
        setValues(res.data)
      })
      .catch((err) => {
        console.error(`Error: ${err}`)
        setMessage(err)
      })
  }
  getUser();
},[params._id])

  const onSubmit = async () => {
    try {
      console.log(values)
      await axios.put(`/userdb`, values)
        .then((response) => console.log(response.data))
      setMessage("Usuario editado OK");
    } catch (error) {
      console.error(`Error: ${error}`);
      setMessage(error);
    }
    
    setTimeout(() => {
      return navigate("/", { replace: true });
    }, 1500);
  }

  const handleChange = event => {
      event.preventDefault();
      const { target } = event;
      const { name, value } = target;
      const newValues = {...values, [name]: value};

      setValues(newValues);
  }

  const handleCancel = (event) => {
    event.preventDefault()
    setMessage("Cambios no guardados")
    setTimeout(() => {
      return navigate("/", { replace: true });
    }, 1500);
  }

  return (
    <form  onSubmit={handleSubmit(onSubmit)} className="edit container">
      <p>Editar</p>
      <label htmlFor="username">Nombre:</label>
      <input 
        {...register("username")}
        type="text"
        name="username"
        value={username}
        onChange={handleChange}/>

      <label htmlFor="email">email:</label>
      <input {...register("email")}
        type="text"
        name="email"
        value={email}
        onChange={handleChange}/>

      <button type="submit" className="button">Aceptar</button>
      <button className="button" onClick={handleCancel}>Cancelar</button>

      {message ?
        <p>{message}</p> :
        <></>
      }
    </form>
  )
}

export default Edit;
