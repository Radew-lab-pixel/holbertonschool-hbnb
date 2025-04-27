// Authentication function - should ONLY handle token
function checkAuthentication() {
  const token = localStorage.getItem('jwt') || document.cookie.match(/token=([^;]+)/)?.[1];
  if (!token) {
      window.location.href = '/login';
      return null; // Explicit return null if no token
  }
  return token;
}



// // Separate function to get place ID
function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
//   const placeId = params.get('place_id');
//   console.log(`placeId: ${placeId}`);
  const placeId = "afeee614-70e4-4e5c-adc0-95c9964c1ddd";
  if (!placeId) {
      console.error('No place_id found in URL');
      // Optionally redirect or show error
  }
  return placeId;
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




// function checkAuthentication() {
//   const token = getCookie('token');
//   const addReviewSection = document.getElementById('add-review');

//   if (!token) {
//       addReviewSection.style.display = 'none';
//   } else {
//       addReviewSection.style.display = 'block';
//       // Store the token for later use
//       fetchPlaceDetails(token, placeId);
//   }
// }


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

document.addEventListener('DOMContentLoaded', () => {
  // 1. First check authentication
  const token = checkAuthentication();
  if (!token) return; // Stop if not authenticated
  
  // 2. Then get place ID
  const placeId = getPlaceIdFromURL();
  console.log(placeId);
  if (!placeId) {
      alert('No place specified');
      window.location.href = '/place'; // Redirect to places listing
      return;
  }

  // 3. Now setup form handling
  const reviewForm = document.getElementById('review-form');
  if (reviewForm) {
      reviewForm.addEventListener('submit', async (event) => {
          event.preventDefault();
          
          const reviewText = document.getElementById('review-text').value.trim();
          const reviewRating = document.getElementById('review-rating').value;
          
          if (!reviewText) {
              alert('Please enter your review');
              return;
          }

          await submitReview(token, placeId, reviewText, reviewRating);
          console.log(`Token : ${token}, place_id:${placeId}, text: ${reviewText}, rating : ${reviewRating}`);
      });
  }
});

async function submitReview(token, placeId, text, rating) {
    const numericRating = Number(rating);
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/reviews',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({
                text,
                rating: numericRating,
                place_id: placeId
            })
        });

        // curl -X POST "http://127.0.0.1:5000/api/v1/reviews/" -H "Content-Type: application/json" -H "Authorization: Bearer <token_goes_here>" -d '{ "text": "Very dirty", "rating": 1, "place_id": "<place_id_goes_here>" }'
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.message || 'Failed to submit review');
        }

        alert('Review submitted successfully!');
        window.location.href = `/place.html?place_id=${placeId}`; // Redirect back
        
    } catch (error) {
        console.error('Review submission error:', error);
        alert(`Error: ${error.message}`);
    }
    }
