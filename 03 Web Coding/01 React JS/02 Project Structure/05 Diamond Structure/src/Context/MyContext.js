/* -----> Third Party Packages <----- */
import React from 'react';

/* -----> Create Global Context <----- */
const MyContext = React.createContext({
	postsList: [],
	onUpdatePostsList: () => {},

	isNightModeActive: false,
	onUpdateIsNightModeActive: () => {},
});

/* -----> Default Export <----- */
export default MyContext;
