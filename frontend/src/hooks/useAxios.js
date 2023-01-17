import { useState, useEffect } from "react";
import axios from "axios";

//axios.defaults.baseURL='/users';
axios.defaults.baseURL="https://backend2-q0hm.onrender.com/usersdb"

//const useAxios = (url = "/userdb") => {
const useAxios = (baseURL) => {

    const [ response, setResponse ] = useState(null);
    const [ error, setError ] = useState(null);
    const [ loading, setLoading ] = useState(true);

    useEffect(() => {
        const fetchData = async() => {
            setTimeout(async() => {
                await axios.get(baseURL)    //await axios.get(url)
                    .then((res) => setResponse(res.data))
                    .catch((err) => setError(err))
                    .finally(() => setLoading(false))
            }, 1500);
        };
        
        fetchData();
    }, [baseURL]);
    
    return { response, error, loading };
};

export default useAxios;