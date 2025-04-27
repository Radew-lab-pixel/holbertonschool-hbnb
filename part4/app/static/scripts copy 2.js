document.addEventListener('DOMContentLoaded', () => {
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
        alert('Login failed: ' + error.message);
      }
    });
  }

  const reviewForm = document.getElementById('review-form');
  if (reviewForm) {
    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const reviewText = document.getElementById('review').value;
      const rating = document.getElementById('rating').value;
      if (!reviewText || !rating) {
        alert('Please fill in all fields');
        return;
      }
      if (reviewText.length < 10) {
        alert('Review text must be at least 10 characters long');
        return;
      }
      if (reviewText.length > 50) {
        alert('Review text must be less than 50 characters long');
        return;
      }
      if (!/^[a-zA-Z\s]+$/.test(reviewText)) {
        alert('Review text must contain only letters and spaces');
        return;
      }
      const placeId = getPlaceIdFromURL();
      const token = checkAuthentication();
      try {
        const result = await submitReview(token, placeId, reviewText, rating);
        handleResponse(result);
      } catch (error) {
        if (error.message.includes('401') || error.message.includes('Unauthorized')) {
          alert('Session expired. Please log in again.');
          window.location.href = '/login';
        } else {
          handleResponse(null, error);
        }
      }
    });
  }

  const urlDisplayElement = document.getElementById('url-address');
  if (urlDisplayElement) {
    urlDisplayElement.textContent = `Current URL: ${window.location.href}`;
  }
});

async function loginUser(email, password) {
  console.log('Attempting login with:', { email, password });
  try {
    const response = await fetch('http://localhost:5001/api/v1/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
    });
    console.log('Login response status:', response.status);
    if (response.ok) {
      const data = await response.json();
      console.log('Login response data:', data);
      const expires = (new Date(Date.now() + 86400 * 1000)).toUTCString();
      document.cookie = `token=${data.access_token}; path=/; Secure; SameSite=Strict; expires=${expires};`;
      console.log('Token set, redirecting to /');
      window.location.href = '/';
    } else {
      const error = await response.json();
      console.error('Login failed with error:', error);
      throw new Error(error.message || response.statusText);
    }
  } catch (error) {
    console.error('Network or fetch error:', error);
    throw new Error(error.message || 'Network error during login');
  }
}

function getPlaceIdFromURL() {
  const queryString = window.location.search;
  const params = new URLSearchParams(queryString);
  const placeId = params.get('place_id');
  return placeId;
}

function getCookie(name) {
  if (!name || !document.cookie) {
    return null;
  }
  const cookieString = `; ${document.cookie}`;
  const cookies = cookieString.split('; ');
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
    window.location.href = '/';
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
      throw new Error(error.error || response.status.toString());
    }
  } catch (error) {
    throw new Error(error.message || 'Network error');
  }
}

function handleResponse(response, error) {
  if (response !== null && response.success === true) {
    alert('Review submitted successfully!');
    document.getElementById('review-form').reset();
  } else {
    alert(error && error.message ? error.message : 'Failed to submit review');
  }
}

