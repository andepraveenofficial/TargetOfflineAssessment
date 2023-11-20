/* -----> Third Paty Packages <----- */
import React, { memo } from 'react';

/* -----> External Components <----- */
import Header from '../../Layout/Header';

/* -----> Styles <----- */
import './index.css';

/* -----> Functional Component <----- */
const Home = () => {
	console.log('Home Page');

	// Return JSx
	return (
		<div className="home-page">
			<Header />
			<div className="home-component">Home Page</div>
		</div>
	);
};

/* -----> Default Export <----- */
export default memo(Home);
