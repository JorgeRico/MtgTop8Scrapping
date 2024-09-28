import { createContext, useContext, useEffect } from "react";
import PropTypes from 'prop-types';
import axios from 'axios';

export const ApiContext = createContext({ undefined });

export const ApiProvider = (props) => {
    const { children } = props;

    // axios
    const headers = {
        'Content-Type'                 : 'application/json',
        'Access-Control-Allow-Origin'  : '*',
        'Access-Control-Allow-Headers' : 'Content-Type',
        'Access-Control-Allow-Methods' : 'GET',
    }

    function getAxiosEndpoint(endpoint) {
        return axios.get(
            endpoint,
            { headers: headers }
        );
    }
    
    useEffect(() => {
        
    }, []);

    return (
        <ApiContext.Provider
            value={{
                getAxiosEndpoint,
            }}
        >
            {children}
        </ApiContext.Provider>
    );
};

ApiProvider.propTypes = {
    children: PropTypes.node
};

export const ApiConsumer = ApiContext.Consumer;

export const useApiContext = () => useContext(ApiContext);
