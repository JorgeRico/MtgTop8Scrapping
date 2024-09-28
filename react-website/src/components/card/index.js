import React, { useRef, useState, useEffect } from "react";
import { v4 as uuidv4 } from "uuid";
import PropTypes from 'prop-types';

export default function StatsCard(props) {
    const effectRan = useRef(false);
    const [ renderItems, setRenderItems ] = useState(null)

    StatsCard.propTypes = {
        name  : PropTypes.string,
        items : PropTypes.array
    };

    useEffect(() => {
        if (!effectRan.current) {
            setRenderItems(props.items?.map((item) => (
                <li key={uuidv4()}>
                    {item.num} - {item.name}
                </li>   
            )));
        }
        
        return () => effectRan.current = true;
    }, []);

    return (
        <>
            <h3>{props.name} stats</h3>
            <ul>
                {(props.items.length > 0) && (
                    renderItems
                )}
            </ul>
        </>
    )
}