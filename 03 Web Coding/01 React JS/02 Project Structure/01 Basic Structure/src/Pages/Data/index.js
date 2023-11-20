/* -----> Third Paty Packages <----- */
import React from 'react';

/* -----> External Components <----- */
import Header from '../../Layout/Header';

/* -----> Styles <----- */
import './index.css';

/* -----> Functional Component <----- */
const Data = () => {
	console.log('Data Page');

	// Return JSx
	return (
		<div className="data-page">
			<Header />
			<div className="data-component">Data Page</div>
		</div>
	);
};

/* -----> Default Export <----- */
export default Data;
