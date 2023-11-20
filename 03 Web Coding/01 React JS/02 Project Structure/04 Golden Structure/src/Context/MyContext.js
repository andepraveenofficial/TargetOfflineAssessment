/* -----> Third Party Packages <----- */
import React from 'react';

/* -----> Create Global Context <----- */
const MyContext = React.createContext({
	postsList: [],
	onChangePostsList: () => {},
});

/* -----> Default Export <----- */
export default MyContext;
