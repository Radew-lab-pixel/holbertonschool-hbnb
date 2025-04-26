import { Link } from 'react-router-dom';

function PlaceCard({ id, title, price, image }) {
    return (
        <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
            <img
                src={`/static/images/${image || 'house1.jpg'}`}
                alt={title}
                className="w-full h-48 object-cover"
            />
            <div className="p-4">
                <h2 className="text-xl font-semibold text-gray-800">{title}</h2>
                <p className="text-gray-600">AU ${price} per night</p>
                <Link
                    to={`/place?place_id=${id}`}
                    className="mt-2 inline-block px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
                >
                    View Details
                </Link>
            </div>
        </div>
    );
}

export default PlaceCard;