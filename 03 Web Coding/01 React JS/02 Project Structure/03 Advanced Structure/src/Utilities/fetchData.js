/* -----> Custom Function <----- */
const fetchData = async (apiUrl) => {
	console.log('useFetchData Custom Hook');

	const options = {
		method: 'GET',
	};

	const response = await fetch(apiUrl, options);
	const data = await response.json();
	console.log(data);

	// Return Data
	return data;
};

/* -----> Default Export <----- */
export default fetchData;
