import { useState, useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';
import Header from './Header';
import Filter from './Filter';
import PlaceCard from './PlaceCard';
import './index.css';

function App() {
  const [maxPrice, setMaxPrice] = useState('');
  const [places, setPlaces] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/v1/places')
      .then(response => response.json())
      .then(data => setPlaces(data))
      .catch(error => console.error('Error fetching places:', error));
  }, []);

  const filteredPlaces = maxPrice
    ? places.filter(place => place.price <= parseFloat(maxPrice))
    : places;

  return (
    <div className="min-h-screen bg-gray-100">
      <Header />
      <main className="pt-20 p-4">
        <Filter onFilterChange={(price) => setMaxPrice(price)} />
        <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-4">
          {filteredPlaces.map(place => (
            <PlaceCard
              key={place.id}
              id={place.id}
              title={place.title}
              price={place.price}
              image={place.image}
            />
          ))}
        </section>
      </main>
    </div>
  );
}

export default App;