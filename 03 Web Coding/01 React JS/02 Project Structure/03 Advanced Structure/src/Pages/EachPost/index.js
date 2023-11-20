/* -----> Third Paty Packages <----- */
import React, { useState, useEffect } from 'react';

/* -----> External Components <----- */
import Header from '../../Layout/Header';

/* -----> Custom Functions <----- */
import fetchData from '../../Utilities/fetchData';

/* -----> Styles <----- */
import './index.css';

/* -----> Functional Component <----- */
const EachPost = (props) => {
	console.log('EachPost Page');

	// State
	const [title, setTitle] = useState('');
	const [post, setPost] = useState('');

	// props object destructuring
	const { match } = props;
	const { postId } = match.params;
	console.log(postId);

	// Methods
	const getData = async () => {
		const apiUrl = `https://jsonplaceholder.typicode.com/posts/${postId}`;
		const data = await fetchData(apiUrl);

		const formattedData = {
			title: data.title,
			post: data.body,
		};

		setTitle(formattedData.title);
		setPost(formattedData.post);
	};

	// Mounting
	useEffect(() => {
		getData();
	}, [postId]);

	// Return JSx
	return (
		<div className="each-post-page">
			<Header />
			<div className="post-container">
				<h1>{title}</h1>
				<p>{post}</p>
			</div>
		</div>
	);
};

/* -----> Default Export <----- */
export default EachPost;
