import React, { useRef, useState, useEffect } from "react";
import { v4 as uuidv4 } from "uuid";
import PropTypes from 'prop-types';
import StatsCardNoTitle from "../../components/cardNoTitle"

export default function StatsPlayer(props) {
    const effectRan = useRef(false);
    const [ renderItems, setRenderItems ] = useState(null)

    StatsPlayer.propTypes = {
        items : PropTypes.array
    };

    useEffect(() => {
        if (!effectRan.current) {
            console.log(props.items)
            setRenderItems(props.items?.map((item) => (
                <li key={uuidv4()}>
                    <h3>Player: {item.name}</h3>
                    <h4>Cards</h4>
                    <ul>
                        <StatsCardNoTitle items={item.deck} />
                    </ul>
                </li>   
            )));
        }
        
        return () => effectRan.current = true;
    }, []);

    return (
        <>
            <ol>
                {(props.items.length > 0) && (
                    renderItems
                )}
            </ol>
        </>
    )
}