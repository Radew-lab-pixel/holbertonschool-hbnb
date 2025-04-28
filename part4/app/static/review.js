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

// // Separate function to get place ID
function getPlaceIdFromURL() {
    // Extract the place ID from window.location.search
    const searchParams = window.location.search;
    const match = searchParams.match(/[?&]place_id=([^&]+)/);
    if (match) {
      return decodeURIComponent(match[1]);
    }

    return null;
}


// function getPlaceIdFromURL() {
//   // Extract the place ID from window.location.search
//   const searchParams = window.location.search;
//   const match = searchParams.match(/[?&]place_id=([^&]+)/);
//   if (match) {
//     return decodeURIComponent(match[1]);
//   }

//   return null;
// }


document.addEventListener('DOMContentLoaded', () => {
    const reviewForm = document.getElementById('review-form');
    reviewForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const token = getCookie('token');
        const placeId = getPlaceIdFromURL();

        const reviewText = document.getElementById('review-text').value.trim();
        const reviewRating = document.getElementById('review-rating').value;
            
        if (!reviewText) {
            alert('Please enter your review');
            return;
        }

        await submitReview(token, placeId, reviewText, reviewRating);
    });
});

async function submitReview(token, placeId, text, rating) {
    const numericRating = Number(rating);
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/reviews/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({
                text,
                rating: numericRating,
                place_id: placeId,
            })
        });

        // curl -X POST "http://127.0.0.1:5000/api/v1/reviews/" -H "Content-Type: application/json" -H "Authorization: Bearer <token_goes_here>" -d '{ "text": "Very dirty", "rating": 1, "place_id": "<place_id_goes_here>" }'
        const data = await response.json();

        if (!response.ok) {
            alert(data.error);
        }

        alert(`Added review. Text: ${reviewText}, rating : ${reviewRating}`);
    } catch (error) {
        console.error('Review submission error:', error);
    }
    }
