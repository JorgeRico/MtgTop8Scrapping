import React, { useRef, useState, useEffect } from "react";
import endpoints from "./../../services/endpoints.js"
import { useApi } from './../../hooks/use-api.js';
import { Link, useParams } from 'react-router-dom';
import StatsCard from "../../components/card"
import CardLink from "../../components/cardLink"

function League() {
    const api                                  = useApi();
    const effectRan                            = useRef(false);
    const [ leagueName, setLEagueName]         = useState(null);
    const [ renderElements, setRenderElements] = useState(null);
    const [ top20, setTop20 ]                  = useState('')
    const [ mainboard, setMainboard ]          = useState('')
    const [ sideboard, setSideboard ]          = useState('')
    const [ players, setPlayers ]              = useState('')
    const { id }                               = useParams();
    
    // api call
    async function apiCall() {
        await api.getAxiosEndpoint(endpoints.API_LEAGUES + '/' + id)
        .then((response) => {
            setLEagueName(response.data.name)
        })
        .catch((err) => { 
            console.log('error')
        });

        await api.getAxiosEndpoint(endpoints.API_LEAGUES + '/' + id + '/tournaments')
        .then((response) => {
            setRenderElements(response.data);
        })
        .catch((err) => { 
            console.log('error')
        });

        await api.getAxiosEndpoint(endpoints.API_LEAGUES + '/' + id + '/stats')
        .then((response) => {
            setTop20(response.data.top20);
            setMainboard(response.data.mb);
            setSideboard(response.data.sb);
            setPlayers(response.data.players);
        })
        .catch((err) => { 
            console.log('error')
        });
    }

    useEffect(() => {
        if (!effectRan.current) {
            apiCall();
        }
        
        return () => effectRan.current = true;
    }, []);

    return (
        <>
            <h1>{leagueName}</h1>
            <Link to={'/'}>
                back
            </Link>
            {renderElements != null && (
                <CardLink url="/tournaments/" items={renderElements} />
            )}
            <h2>Stats</h2>
            {top20.length > 0 && (
                <StatsCard name="Top10" items={top20} />
            )}
            {mainboard.length > 0 && (
                <StatsCard name="Mainboard" items={mainboard} />
            )}
            {sideboard.length > 0 && (
                <StatsCard name="Sideboard" items={sideboard} />
            )}
            {players.length > 0 && (
                <StatsCard name="Players" items={players} />
            )}
        </>
    );
}

export default League;