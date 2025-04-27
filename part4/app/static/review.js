document.addEventListener('DOMContentLoaded', () => {
    const token = checkAuthentication();
    const placeId = getPlaceIdFromURL();
    
    // checkAuthenication() and getPlaceIdFromURL() from place.js to be imported in add_review.html

    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const reviewText = document.getElementById('review-text').value;
            console.log(reviewText);
            submitReview(token, placeId, reviewText);
        });
    }
});


async function submitReview(token, placeId, reviewText) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/reviews', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ place_id: placeId, review: reviewText })
        });
        handleResponse(response);
    } catch (error) {
        console.error('Error submitting review:', error);
    }
}

// 



// not working too messy to correct
// const reviewForm = document.getElementById('review-form');

// // Handle form submission
// reviewForm.addEventListener('submit', async (e) => {
//   e.preventDefault(); // Prevent page reload
  
//   // Get form values
//   const formData = {
//     rating: reviewForm.querySelector('input[name="rating"]:checked')?.value,
//     review: reviewForm.querySelector('#review-text').value,
//     place_id: new URLSearchParams(window.location.search).get('place_id')
//   };

//   // Simple validation
//   if (!formData.rating) return alert('Please select a rating');
//   if (!formData.review) return alert('Please write a review');

//   try {
//     // Send to API
//     const response = await fetch('http://127.0.0.1:5000/api/v1/reviews', {
//       method: 'POST',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify(formData)
//     });

//     if (!response.ok) throw new Error('Submission failed');
    
//     alert('Review submitted!');
//     reviewForm.reset(); // Clear form
    
//   } catch (error) {
//     console.error(error);
//     alert('Error submitting review');
//   }
// });


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