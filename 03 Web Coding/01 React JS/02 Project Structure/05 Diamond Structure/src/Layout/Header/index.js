/* -----> Third Party Packages <----- */
import React, { memo, useContext } from 'react';
import { Link, withRouter } from 'react-router-dom';
import Cookies from 'js-cookie';

/* -----> Context <----- */
import MyContext from '../../Context/MyContext';

/* -----> Styles <----- */
import './index.css';

/* -----> Functional Component <----- */
const Header = memo((props) => {
	console.log('Header Layout');

	// Context
	const { isNightModeActive, onUpdateIsNightModeActive } =
		useContext(MyContext);

	// Methods
	const onLogoutButton = () => {
		console.log('onLogoutButton Method');
		Cookies.remove('jwt_token');
		const { history } = props;
		history.replace('/login');
	};

	const onLightMode = () => {
		onUpdateIsNightModeActive(() => !isNightModeActive);
	};

	// Component Parts
	const lightMode = isNightModeActive ? 'Night' : 'Day';

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
				<button
					className="light-mode"
					type="button"
					onClick={onLightMode}
				>
					{lightMode}
				</button>
			</div>
		</div>
	);
});

/* -----> Default Export <----- */
export default withRouter(Header);
