/* -----> Third Party Packages <----- */
import React from 'react';
import { Link, withRouter } from 'react-router-dom';
import Cookies from 'js-cookie';

/* -----> Styles <----- */
import './index.css';

/* -----> Functional Component <----- */
const Header = (props) => {
	console.log('Header Layout');

	// Methods
	const onLogoutButton = () => {
		console.log('onLogoutButton Method');
		Cookies.remove('jwt_token');
		const { history } = props;
		history.replace('/login');
	};

	// Return JSX
	return (
		<div className="header-layout">
			<div>
				<Link to="/" className="nav-link">
					Home
				</Link>
				<Link to="/data" className="nav-link">
					Data
				</Link>
			</div>

			<div>
				<button
					className="logout-button"
					type="button"
					onClick={onLogoutButton}
				>
					Logout
				</button>
			</div>
		</div>
	);
};

/* -----> Default Export <----- */
export default withRouter(Header);
