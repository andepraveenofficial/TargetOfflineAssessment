/* -----> Third Paty Packages <----- */
import React, {
	useState,
	useEffect,
	useContext,
	useMemo,
	useCallback,
	memo,
} from 'react';

/* -----> External Components <----- */
import Header from '../../Layout/Header';
import Card from '../../Components/Card';

/* -----> Custom  Functions <----- */
import fetchData from '../../Utilities/fetchData';

/* -----> Context <----- */
import MyContext from '../../Context/MyContext';

/* -----> Styles <----- */
import './index.css';

/* -----> Functional Component <----- */
const Data = () => {
	console.log('Data Page');

	// State
	// const [postsList, setPostsList] = useState([]);

	// Context
	const { postsList, onUpdatePostsList } = useContext(MyContext);

	// APIs
	const apiUrl = 'https://jsonplaceholder.typicode.com/posts';

	// Methods
	const getPostsData = useCallback(async () => {
		try {
			const data = await fetchData(apiUrl);
			const formattedData = data.map((each) => ({
				id: each.id,
				userId: each.userId,
				title: each.title,
				post: each.body,
			}));

			onUpdatePostsList(formattedData);
		} catch (error) {
			console.error('Error fetching data');
		}
	}, [apiUrl]);

	// Mounting
	useEffect(() => {
		getPostsData();
	}, []);

	// Memoized postsList
	const memoizedPostsList = useMemo(
		() => postsList.map((each) => <Card key={each.id} eachPost={each} />),
		[postsList],
	);

	// Return JSx
	return (
		<div className="data-page">
			<Header />
			<div className="data-component">
				<ul className="posts-list">{memoizedPostsList}</ul>
			</div>
		</div>
	);
};

/* -----> Default Export <----- */
export default memo(Data);
