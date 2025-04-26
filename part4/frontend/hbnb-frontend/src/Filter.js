import { useState } from 'react';

function Filter({ onFilterChange }) {
    const [maxPrice, setMaxPrice] = useState('');

    const handleChange = (e) => {
        setMaxPrice(e.target.value);
        onFilterChange(e.target.value);
    }

    return (
        <section className="mb-4">
            <label htmlFor="price-filter" className="mr-2 text-lg font-medium text-gray-700">Max Price:</label>
            <select
                id="price-filter"
                value={maxPrice}
                onChange={handleChange}
                className="p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
                <option value="">All</option>
                <option value="100">AU $100</option>
                <option value="150">AU $150</option>
                <option value="200">AU $200</option>
            </select>
        </section>
    );
}

export default Filter;