function getPlaceIdFromURL() {
    // Extract the place ID from window.location.search
    const searchParams = window.location.search;
    const match = searchParams.match(/[?&]place_id=([^&]+)/);
    if (match) {
      return decodeURIComponent(match[1]);
    }

    return null;
}

function checkAuthentication() {
    const token = getCookie('token');
    const addReviewSection = document.getElementById('add-review');

    if (!token) {
        addReviewSection.style.display = 'none';
    } else {
        addReviewSection.style.display = 'block';
        // Store the token for later use
        fetchPlaceDetails(token, placeId);
    }
}

function getCookie(name) {
    // Function to get a cookie value by its name
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
        c = c.substring(1);
        }
        if (c.indexOf(`${name}=`) == 0) {
        return c.substring(name.length + 1, c.length);
        }
    }

    return "";
}

async function fetchPlaceDetails(token, placeId) {
    // Make a GET request to fetch place details
    // Include the token in the Authorization header
    // Handle the response and pass the data to displayPlaceDetails function

    const data = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json",
        }
    })
    .then((res) => res.json());

    console.log(data);

    return data;
}

function displayPlaceDetails(place) {
    // Clear the current content of the place details section
    // Create elements to display the place details (name, description, price, amenities and reviews)
    // Append the created elements to the place details section

    document.getElementById("place-details").innerHTML = (
        `<div class="place-details">
            <h2>${place.title}</h2>
        </div>
        <img src="/static/images/house1.jpg" alt="House Image" />
        <div class="place-info">
        <p>Host : ${place.owner.first_name}</p>
        <p>Price: AU $${place.price} per night</p>
        <p>Description: ${place.description} </p>
        <p>Amenities: ${place.amenities.map((obj) => obj.name).join(', ')}</p>
        </div>
        `);
}

document.addEventListener("DOMContentLoaded", async () => {
    const placeId = getPlaceIdFromURL();
    const token = getCookie("token");

    console.log(placeId);

    const place = await fetchPlaceDetails(token, placeId);

    console.log(place);

    displayPlaceDetails(place);
});
