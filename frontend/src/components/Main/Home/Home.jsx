import React, { useContext, useEffect } from 'react';

import { userContext } from "../../../context/userContext";

import User from '../User/User';
import Spinner from '../../../utils/Spinner'
import useAxios from "../../../hooks/useAxios";

import { v4 as uuidv4 } from 'uuid';

function Home () {

  const { users, setUsers } = useContext(userContext);
  const { response, loading, error } = useAxios();

  useEffect (() => {
    if (error) console.log(`Error: ${error}`);
    if (response !== null) {
      setUsers(response)
    }
    console.log(response)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  },[response]);

  const paintUsers = () => {
    return users.map(
      (user) => (
      <User value={user} key={uuidv4()}/>))
  };

  return (
    <div className="home container">
      {loading ? <Spinner/>: ""}
      {loading ? <p>"Loading..."</p> : paintUsers()}  {/* //quitamos isLoading */}
    </div>
  )
}

export default Home;
