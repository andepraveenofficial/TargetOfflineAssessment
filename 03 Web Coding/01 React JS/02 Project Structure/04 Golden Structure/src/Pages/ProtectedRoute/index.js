/* -----> Third Party Packages <----- */
import React from 'react';
import Cookies from 'js-cookie';
import { Redirect, Route } from 'react-router-dom';

/* -----> Wrapper Component <----- */
const ProtectedRoute = (props) => {
	console.log('ProtectedRoute');
	const jwtToken = Cookies.get('jwt_token');
	console.log(jwtToken);

	if (jwtToken === undefined) {
		return <Redirect to="/login" />;
	}
	return <Route {...props} />;
};

/* -----> Default Export <----- */
export default ProtectedRoute;
