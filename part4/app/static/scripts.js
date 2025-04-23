// app/static/js/scripts.js

// Get cookie by name
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
  return null;
}

// Get place ID from URL
function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
  return params.get('place_id');
}

// Check authentication and redirect if unauthenticated
function checkAuthentication() {
  const token = getCookie('token');
  if (!token) {
    window.location.href = '/index.html';
  }
  return token;
}

// Submit review to API
async function submitReview(token, placeId, text, rating) {
  try {
    const response = await fetch('http://localhost:5000/api/v1/reviews', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        place_id: placeId,
        text: text,
        rating: parseInt(rating) // Ensure rating is an integer
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

// Existing login code
document.addEventListener('DOMContentLoaded', () => {
  // Login form handling
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const email = document.getElementById('email').value; // Changed to .value
      const password = document.getElementById('password').value; // Changed to .value

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
  const token = checkAuthentication();
  const placeId = getPlaceIdFromURL();

  if (reviewForm && token && placeId) {
    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const reviewText = document.getElementById('review').value;
      const rating = document.getElementById('rating').value;

      if (!reviewText || !rating) {
        alert('Please fill in both review and rating fields');
        return;
      }

      try {
        const result = await submitReview(token, placeId, reviewText, rating);
        alert('Review submitted successfully!');
        reviewForm.reset();
      } catch (error) {
        alert(`Error: ${error.message}`);
      }
    });
  }

  // URL display for debugging
  const urlDisplayElement = document.getElementById('url-address');
  if (urlDisplayElement) {
    urlDisplayElement.textContent = `Current URL: ${window.location.href}`;
  }
});

// Login function
async function loginUser(email, password) {
  const response = await fetch('http://localhost:5000/api/v1/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ email, password })
  });

  if (response.ok) {
    const data = await response.json();
    document.cookie = `token=${data.access_token}; path=/`;
    window.location.href = '/index.html';
  } else {
    throw new Error('Login failed: ' + response.statusText);
  }
}