import axios from 'axios';
import { Link, useLoaderData } from 'react-router-dom';
import HomePage from './HomePage';
import Button from '@mui/material/Button';
import Rating from '@mui/material/Rating'
import Typography from '@mui/material/Typography'

const apiKey = "7f539340"

export async function filmLoader({ params }) {
    const response = await axios.get(`https://www.omdbapi.com/?i=${params.filmId}&apikey=${apiKey}`);
    return response.data;
}

export default function DetailsPanel() {
    const filmData = useLoaderData();
    const { Title, Poster, Rated, Plot } = filmData;

    return (
        <div className="section_container">
            <Link to="/">Back to home page</Link>
            <h2>Details</h2>
            <div className='basic_container_column'>
                <h3>{Title}</h3>
                <div>
                    <img src={Poster} />
                    <p>{Plot}</p>
                    <pre style={{ fontSize: "40px" }}>{Rated}</pre>
                    <Button variant="contained" className='button'>Check Out</Button>
                    <Button variant="contained" className='button'>Return</Button>
                    {/* <Typography component="legend">Read only</Typography>
                    <Rating name="read-only" value={value} readOnly /> */}
                      
        
                </div>
            </div>
        </div>
    );
}