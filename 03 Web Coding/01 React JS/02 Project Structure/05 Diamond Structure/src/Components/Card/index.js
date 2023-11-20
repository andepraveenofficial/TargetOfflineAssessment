/* -----> Third Paty Packages <----- */
import React from 'react';
import { Link } from 'react-router-dom';

/* -----> Style <----- */
import './index.css';

/* -----> Functional Component <----- */
const Card = (props) => {
	console.log('Card Component');

	// props object destructuring
	const { eachPost } = props;
	const { title, post, id } = eachPost;

	// Return JSX
	return (
		<div className="card-component">
			<Link to={`each-post/${id}`} className="post-link">
				<h1 className="post-title">{title}</h1>
			</Link>

			<p className="post-data">{post}</p>
		</div>
	);
};

/* -----> Default Export <----- */
export default Card;
