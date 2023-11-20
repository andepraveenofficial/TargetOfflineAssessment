/* -----> Third Paty Packages <----- */
import React, { useState, useEffect, useMemo, useCallback } from 'react';
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
import NightModeStyles from './StyledComponents/globalStyles';

/* -----> Functional Component <----- */
const App = () => {
	console.log('App Component');

	// State
	const [postsList, setPostsList] = useState([]);
	const [isNightModeActive, setIsNightModeActive] = useState(false);

	// Methods
	const onChangePostsList = useCallback((updatedPostsList) => {
		console.log('onChangePostsList Method');
		setPostsList(updatedPostsList);
	}, []);

	const onChangeNightMode = (updateIsNightModeActive) => {
		setIsNightModeActive(updateIsNightModeActive);
	};

	// Context Object
	const contextObject = useMemo(() => {
		return {
			postsList: postsList,
			onUpdatePostsList: onChangePostsList,

			isNightModeActive: isNightModeActive,
			onUpdateIsNightModeActive: onChangeNightMode,
		};
	}, [postsList, isNightModeActive]);

	// Return JSX
	return (
		<MyContext.Provider value={contextObject}>
			{isNightModeActive ? <NightModeStyles /> : ''}
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
