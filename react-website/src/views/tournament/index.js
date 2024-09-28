import React, { useRef, useState, useEffect } from "react";
import endpoints from "./../../services/endpoints.js"
import { useApi } from './../../hooks/use-api.js';
import { Link, useParams } from 'react-router-dom';
import StatsCard from "../../components/card"
import StatsCardNoTitle from "../../components/cardNoTitle"
import PlayerCard from "../../components/player"

function Tournament() {
    const api                                   = useApi();
    const effectRan                             = useRef(false);
    const [ renderPlayers, setRenderPlayers]    = useState([]);
    const [ tournament, setTournament]          = useState({name:'', date:''});
    const [ top10, setTop10 ]                   = useState([])
    const [ mainboard, setMainboard ]           = useState([])
    const [ sideboard, setSideboard ]           = useState([])
    const { id }                                = useParams();

    // api call
    async function apiCall() {
        await api.getAxiosEndpoint(endpoints.API_TOURNAMENTS + '/' + id + '/data')
        .then((response) => {
            setTournament(prevState => ({
                ...prevState,
                'name': response.data.tournament.name,
                'date': response.data.tournament.date
            }));
            console.log(response.data.players)
            setRenderPlayers(response.data.players);
            
        })
        .catch((err) => { 
            console.log('error')
        });

        await api.getAxiosEndpoint(endpoints.API_TOURNAMENTS + '/' + id + '/stats')
        .then((response) => {
            setTop10(response.data.top10);
            setMainboard(response.data.mb);
            setSideboard(response.data.sb);
        })
        .catch((err) => { 
            console.log('error e')
        });
    }

    useEffect(() => {
        if (!effectRan.current) {
            apiCall();
            console.log(renderPlayers)
        }
        
        return () => effectRan.current = true;
    }, []);

    return (
        <>
            <h1>{tournament.name} - {tournament.date}</h1>
            <Link to={'/leagues/1'}>
                back
            </Link>
            {renderPlayers.length > 0 && (
                <PlayerCard items={renderPlayers} />
            )}
            <h2>Stats</h2>
            {top10.length > 0 && (
                <StatsCard name="Top10" items={top10} />
            )}
            {mainboard.length > 0 && (
                <StatsCard name="Mainboard" items={mainboard} />
            )}
            {sideboard.length > 0 && (
                <StatsCard name="Sideboard" items={sideboard} />
            )}
        </>
    );
}

export default Tournament;