import React, { useRef, useState, useEffect } from "react";
import endpoints from "./../../services/endpoints.js"
import { useApi } from './../../hooks/use-api.js';
import { v4 as uuidv4 } from "uuid";
import { Link } from 'react-router-dom';

function Home() {
    const api       = useApi();
    const effectRan = useRef(false);
    const [ renderElements, setRenderElements]  = useState(null);

    // api call
    async function apiCall() {
        await api.getAxiosEndpoint(endpoints.API_LEAGUES)
        .then((response) => {
            setRenderElements(response.data?.map((item) => (
                element(item)
            )));
        })
        .catch((err) => { 
            console.log('error')
        });
    }

    const element = (item) => {
        return (
            <li key={uuidv4()}>
                <Link to={'leagues/' + item.id}>
                    {item.name}
                </Link>
            </li>
        )
    }

    useEffect(() => {
        if (!effectRan.current) {
            apiCall();
        }
        
        return () => effectRan.current = true;
    }, []);

    return (
        <div className="App">
            <ul>
                {renderElements}
            </ul>
        </div>
    );
}

export default Home;