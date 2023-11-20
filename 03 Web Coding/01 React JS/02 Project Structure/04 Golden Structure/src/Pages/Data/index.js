/* -----> Third Paty Packages <----- */
import React, { useState, useEffect, useContext } from 'react';

/* -----> External Components <----- */
import Header from '../../Layout/Header';
import Card from '../../Components/Card';

/* -----> Custom  Functions <----- */
import fetchData from '../../Utilities/fetchData';

/* -----> Context <----- */
import MyContext from '../../Context/MyContext';

/* -----> Styles <----- */
import './index.css';

/* -----> Functional Component <----- */
const Data = () => {
	console.log('Data Page');

	// State
	// const [postsList, setPostsList] = useState([]);

	// Context
	const { postsList, onUpdatePostsList } = useContext(MyContext);

	// Methods
	const getPostsData = async () => {
		const apiUrl = 'https://jsonplaceholder.typicode.com/posts';
		try {
			const data = await fetchData(apiUrl);
			const formattedData = data.map((each) => ({
				id: each.id,
				userId: each.userId,
				title: each.title,
				post: each.body,
			}));

			onUpdatePostsList(formattedData);
		} catch (error) {
			console.error('Error fetching data');
		}
	};

	// Mounting
	useEffect(() => {
		getPostsData();
	}, []);

	// Return JSx
	return (
		<div className="data-page">
			<Header />
			<div className="data-component">
				<ul className="posts-list">
					{postsList.map((each) => (
						<Card key={each.id} eachPost={each} />
					))}
				</ul>
			</div>
		</div>
	);
};

/* -----> Default Export <----- */
export default Data;
