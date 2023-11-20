/* -----> Third Paty Packages <----- */
import React from 'react';

/* -----> External Components <----- */
import Login from './Pages/Login';
import Home from './Pages/Home';
import Data from './Pages/Data';
import NotFound from './Pages/NotFound';

/* -----> Styles <----- */
import './App.css';

/* -----> Functional Component <----- */
const App = () => {
	console.log('App Component');

	// Return JSX
	return (
		<div className="app-component">
			<Login />
		</div>
	);
};

/* -----> Default Export <----- */
export default App;
