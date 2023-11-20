/* -----> Third Party Packages <----- */
import React, { useState } from 'react';
import Cookies from 'js-cookie';
import { Redirect } from 'react-router-dom';

/* -----> Styles <----- */
import './index.css';

/* -----> Functional Component <----- */
const Login = (props) => {
	console.log('Login Page');

	// State
	const [username, setUsername] = useState('');
	const [password, setPassword] = useState('');
	const [errorMessage, setErrorMessage] = useState('');
	const [showSubmitError, setShowSubmitError] = useState(false);

	// Methods
	const onSubmitSuccess = (formData) => {
		console.log(formData);
		setShowSubmitError(false);

		const { history } = props;

		const jwtToken = formData.jwt_token;
		console.log(jwtToken);

		Cookies.set('jwt_token', jwtToken, { expires: 30 });

		history.replace('/'); // Automatic Browser Path change
	};

	const onSubmitFailure = (formData) => {
		console.log(formData);
		setShowSubmitError(true);
		const errMsg = formData.error_msg;
		console.log(errMsg);
		setErrorMessage(errMsg);
	};

	const onFormSubmit = async (event) => {
		console.log('Form Submitted');
		event.preventDefault(); // Avoid form default behaviour

		const userDetails = { username, password };
		console.log(userDetails);

		const apiUrl = 'https://apis.ccbp.in/login/';
		const options = {
			method: 'POST',
			body: JSON.stringify(userDetails),
		};
		const response = await fetch(apiUrl, options); // Network Call
		console.log(response);

		if (response.ok) {
			console.log('Success');
			const data = await response.json();
			onSubmitSuccess(data);
		} else {
			console.log('Failure');
			const data = await response.json();
			onSubmitFailure(data);
		}
	};

	const renderLoginPage = () => (
		<div className="login-page">
			<form className="form-container" onSubmit={onFormSubmit}>
				<h1 className="login-form-heading">Login Form</h1>
				<div className="input-container">
					<label htmlFor="username">Username</label>
					<input
						id="username"
						className="input-box"
						type="text"
						placeholder="Username : rahul"
						value={username}
						onChange={(event) => setUsername(event.target.value)}
					/>
				</div>
				<div className="input-container">
					<label htmlFor="username">Password</label>
					<input
						id="password"
						className="input-box"
						type="password"
						placeholder="Password : rahul@2021"
						value={password}
						onChange={(event) => setPassword(event.target.value)}
					/>
				</div>
				<div>
					{showSubmitError && (
						<p className="error-message">{errorMessage}</p>
					)}
				</div>
				<div className="button-container">
					<button type="submit" className="button">
						Login
					</button>
				</div>
			</form>
		</div>
	);

	// Return JSX
	const jwtToken = Cookies.get('jwt_token');
	if (jwtToken !== undefined) {
		console.log('Redirect to Home Component');
		return <Redirect to="/" />;
	}
	return renderLoginPage();
};

/* -----> Default Export <----- */
export default Login;
