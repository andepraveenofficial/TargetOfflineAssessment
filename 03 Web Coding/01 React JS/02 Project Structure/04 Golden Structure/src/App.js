/* -----> Third Paty Packages <----- */
import React, { useState, useEffect } from 'react';
import { BrowserRouter, Switch, Route, Redirect } from 'react-router-dom';

/* -----> External Components <----- */
import ProtectedRoute from './Pages/ProtectedRoute';
import Login from './Pages/Login';
import Home from './Pages/Home';
import Data from './Pages/Data';
import EachPost from './Pages/EachPost';
import NotFound from './Pages/NotFound';

/* -----> Context <----- */
import MyContext from './Context/MyContext';

/* -----> Styles <----- */
import './App.css';

/* -----> Functional Component <----- */
const App = () => {
	console.log('App Component');

	// State
	const [postsList, setPostsList] = useState([]);

	// Methods
	const onChangePostsList = (updatedPostsList) => {
		setPostsList(updatedPostsList);
	};

	// Context Object
	const contextObject = {
		postsList: postsList,
		onUpdatePostsList: onChangePostsList,
	};

	// Return JSX
	return (
		<MyContext.Provider value={contextObject}>
			<div className="app-component">
				<BrowserRouter>
					<Switch>
						<Route exact path="/login" component={Login} />
						<ProtectedRoute exact path="/" component={Home} />
						<ProtectedRoute exact path="/data" component={Data} />
						<ProtectedRoute
							eaxt
							path="/each-post/:postId"
							component={EachPost}
						/>
						<Route exact path="/not-found" component={NotFound} />
						<Redirect to="not-found" />
					</Switch>
				</BrowserRouter>
			</div>
		</MyContext.Provider>
	);
};

/* -----> Default Export <----- */
export default App;
