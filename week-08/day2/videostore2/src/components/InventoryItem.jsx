import { useNavigate } from "react-router-dom";
import PropTypes from 'prop-types';

export default function InventoryItem(props) {
    const navigate = useNavigate();

    return (
        <div className="inventory_item" onClick={() => navigate(`/film/${props.filmData.imdbID}`)}>
            <h3 className="item_title">{props.filmData.Title}</h3>
            <img src={props.filmData.Poster} />
        </div>
    );
}
InventoryItem.propTypes = {
    filmData: PropTypes.shape({
        Title: PropTypes.string.isRequired,
        Poster: PropTypes.string.isRequired,
        imdbID: PropTypes.string.isRequired,
        Rated: PropTypes.oneOf(['PG', 'PG-13', 'R'])
    })
};