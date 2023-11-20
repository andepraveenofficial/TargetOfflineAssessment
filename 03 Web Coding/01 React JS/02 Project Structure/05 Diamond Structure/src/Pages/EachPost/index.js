/* -----> Third Paty Packages <----- */
import React, { useState, useEffect, useCallback, useMemo, memo } from 'react';

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
	const getData = useCallback(async () => {
		const apiUrl = `https://jsonplaceholder.typicode.com/posts/${postId}`;
		const data = await fetchData(apiUrl);

		const formattedData = {
			title: data.title,
			post: data.body,
		};

		setTitle(formattedData.title);
		setPost(formattedData.post);
	}, [postId]);

	// Mounting
	useEffect(() => {
		getData();
	}, [getData]);

	const renderEachPost = useMemo(
		() => (
			<div className="post-container">
				<h1 className="each-post-heading">{title}</h1>
				<p className="each-post-paragraph">{post}</p>
			</div>
		),
		[title, post],
	);

	// Return JSx
	return (
		<div className="each-post-page">
			<Header />
			{renderEachPost}
		</div>
	);
};

/* -----> Default Export <----- */
export default memo(EachPost);
