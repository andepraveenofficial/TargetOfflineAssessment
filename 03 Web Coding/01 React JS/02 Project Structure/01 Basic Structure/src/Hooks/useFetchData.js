/* -----> Third Party Packages <----- */
import { useEffect, useState } from 'react';

/* -----> Custom Hook <----- */
const useFetchData = (apiUrl) => {
	console.log('useFetchData Custom Hook');
	// State
	const [data, setData] = useState([]);

	// Methods
	const getData = async () => {
		const options = {
			method: 'GET',
		};

		const response = await fetch(apiUrl, options);
		const data = await response.json();
		console.log(data);
		setData(data);
	};

	// Mounting
	useEffect(() => {
		getData();
	}, []);

	// Return Data
	return data;
};

/* -----> Default Export <----- */
export default useFetchData;
