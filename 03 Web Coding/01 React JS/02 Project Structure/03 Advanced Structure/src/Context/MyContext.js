/* -----> Third Party Packages <----- */
import React from 'react';

/* -----> Create Global Context <----- */
const MyContext = React.createContext({
	name: 'Ande Praveen',
	changeName: () => {},
});

/* -----> Default Export <----- */
export default MyContext;
