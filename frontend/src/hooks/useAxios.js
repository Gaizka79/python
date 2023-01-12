import { useState, useEffect } from "react";
import axios from "axios";

//axios.defaults.baseURL='/users';

const useAxios = (url = "/userdb") => {

    const [ response, setResponse ] = useState(null);
    const [ error, setError ] = useState(null);
    const [ loading, setLoading ] = useState(true);

    useEffect(() => {
        const fetchData = async() => {
            setTimeout(async() => {
                await axios.get(url)
                    .then((res) => setResponse(res.data))
                    .catch((err) => setError(err))
                    .finally(() => setLoading(false))
            }, 1500);
        };
        
        fetchData();
    }, [url]);
    
    return { response, error, loading };
};

export default useAxios;