import React, { useRef, useState, useEffect } from "react";
import { v4 as uuidv4 } from "uuid";
import PropTypes from 'prop-types';

export default function StatsCardNoTitle(props) {
    const effectRan = useRef(false);
    const [ renderItems, setRenderItems ] = useState(null)

    StatsCardNoTitle.propTypes = {
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
            <ul>
                {(props.items.length > 0) && (
                    renderItems
                )}
            </ul>
        </>
    )
}