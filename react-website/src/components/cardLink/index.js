import React, { useRef, useState, useEffect } from "react";
import { v4 as uuidv4 } from "uuid";
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

export default function StatsCardLink(props) {
    const effectRan = useRef(false);
    const [ renderItems, setRenderItems ] = useState(null)

    StatsCardLink.propTypes = {
        url  : PropTypes.string,
        items : PropTypes.array
    };

    useEffect(() => {
        if (!effectRan.current) {
            setRenderItems(props.items?.map((item) => (
                <li key={uuidv4()}>
                    <Link to={props.url + item.id}>
                        {item.name}
                    </Link>
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