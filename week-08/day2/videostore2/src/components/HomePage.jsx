import { useLoaderData } from 'react-router-dom';
import axios from 'axios';
import InventoryItem from './InventoryItem';
import inventory from '../data/inventory.json';


const apiKey = "7f539340"

export async function allFilmsLoader() {
    const promise = inventory.map(imdbId => axios.get(`https://www.omdbapi.com/?i=${imdbId}&apikey=${apiKey}`));
    const response = await Promise.all(promise);
    const allFilmData = response.map(response => response.data);
    return allFilmData;
}
export default function HomePage() {
    const allFilmData = useLoaderData();

    return (
        <div className="page_container">
            <h2>Inventory</h2>
            <div className="section_container">
                {
                    allFilmData.map((filmData, index) => (
                        <InventoryItem
                            key={index}
                            filmData = {filmData}
                        />
                        ))
                        
                }
                <InventoryItem filmData= {{
                    Title: "Super Mario Bros Movie",
                    Poster: "lkdfdfd",
                    imdbID: "tt6718170",
                    Rated: "PG"
                }} />
            </div>
        </div>
    );
}
