/* -----> Third Paty Packages <----- */
import React from 'react';

/* -----> Styles <----- */
import './index.css';

/* -----> Functional Component <----- */
const NotFound = (props) => {
	console.log('NotFound Page');

	// Methods
	const onGotoHomepage = () => {
		console.log('onGotoHomepage Method');
		const { history } = props;
		console.log(history);
		history.replace('/');
	};

	// Return JSx
	return (
		<div className="not-found-page">
			<h1>NotFound Page</h1>
			<button
				type="button"
				onClick={onGotoHomepage}
				className="goto-home-page-button"
			>
				Go to homepage
			</button>
		</div>
	);
};

/* -----> Default Export <----- */
export default NotFound;
