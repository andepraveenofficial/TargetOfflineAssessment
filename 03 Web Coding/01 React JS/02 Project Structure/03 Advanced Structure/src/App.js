/* -----> Third Paty Packages <----- */
import React from 'react';
import { BrowserRouter, Switch, Route, Redirect } from 'react-router-dom';

/* -----> External Components <----- */
import ProtectedRoute from './Pages/ProtectedRoute';
import Login from './Pages/Login';
import Home from './Pages/Home';
import Data from './Pages/Data';
import EachPost from './Pages/EachPost';
import NotFound from './Pages/NotFound';

/* -----> Styles <----- */
import './App.css';

/* -----> Functional Component <----- */
const App = () => {
	console.log('App Component');

	// Return JSX
	return (
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
	);
};

/* -----> Default Export <----- */
export default App;
