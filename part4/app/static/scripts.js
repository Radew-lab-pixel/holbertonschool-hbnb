/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
  // Login form handling
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      if (!email || !password) {
        alert('Please fill in both email and password fields');
        return;
      }

      try {
        await loginUser(email, password);
      } catch (error) {
        console.error('Login error:', error);
        alert('Login failed. Please check your credentials and try again.');
      }
    });
  }

  // Review form handling
  const reviewForm = document.getElementById('review-form');
  if (reviewForm) {
    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      // Get review text
      const reviewText = document.getElementById('review').value;
      // Get rating
      const rating = document.getElementById('rating').value;
      // Check if empty
      if (!reviewText || !rating) {
        alert('Please fill in all fields');
        return;
      }
      // Get placeId
      const placeId = getPlaceIdFromURL();
      // Check token
      const token = checkAuthentication();
      try {
        //Send review to API
        const result = await submitReview(token, placeId, reviewText, rating);
        handleResponse(result);
      } catch (error) {
        handleResponse(null, error);
      }
    });
  }

  // Debugging URL display
  const urlDisplayElement = document.getElementById('url-address');
  if (urlDisplayElement) {
    urlDisplayElement.textContent = `Current URL: ${window.location.href}`;
  }
});

async function loginUser(email, password) {
  const response = await fetch('http://localhost:5001/api/v1/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ email, password })
  });

  if (response.ok) {
    const data = await response.json();
    document.cookie = `token=${data.access_token}; path=/; SameSite=Lax`;
    window.location.href = '/';
  } else {
    alert('Login failed: ' + response.statusText);
  }
}

function getPlaceIdFromURL() {
  // Get the query string
  const queryString = window.location.search;
  // Create URLSearchParams
  const params = new URLSearchParams(queryString);
  // Get place_id
  const placeId = params.get('place_id');
  // Return it
  return placeId;
}

function getCookie(name) {
  // Input validation
  if (!name || !document.cookie) {
    return null;
  }
  // Get all cookies
  const cookieString = `; ${document.cookie}`;
  // Split into individual cookies
  const cookies = cookieString.split('; ');
  // Find the cookie with name
  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i].trim();
    if (cookie.startsWith(name + '=')) {
      const value = cookie.substring(name.length + 1);
      return value ? decodeURIComponent(value) : '';
    }
  }
  return null;
}

function checkAuthentication() {
  const token = getCookie('token');
  if (!token) {
    window.location.href = '/index.html';
  }
  return token;
}

async function submitReview(token, placeId, reviewText, rating) {
  if (!token || !placeId || !reviewText || isNaN(parseInt(rating))) {
    throw new Error('Invalid input parameters');
  }
  try {
    const response = await fetch('http://localhost:5001/api/v1/reviews', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        place_id: placeId,
        text: reviewText,
        rating: parseInt(rating)
      })
    });
    if (response.ok) {
      return { success: true, data: await response.json() };
    } else {
      const error = await response.json();
      throw new Error(error.message || 'Failed to submit review');
    }
  } catch (error) {
    throw new Error(error.message || 'Network error');
  }
}

function handleResponse(response, error) {
  if (response !== null && response.success === true) {
    // Show success message
    alert('Review submitted successfully!');
    // Clear form
    document.getElementById('review-form').reset();
  } else {
    // Show error message
    alert(error && error.message ? error.message : 'Failed to submit review');
  }
}
