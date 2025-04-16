/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

// document.addEventListener('DOMContentLoaded', () => {
    /* DO SOMETHING */
//  });

document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

  if (loginForm) {
      loginForm.addEventListener('submit', async (event) => {
          event.preventDefault();
          // Your code to handle form submission
      });
  }
});

async function loginUser(email, password) {
  const response = await fetch('https://your-api-url/login', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
  });
  // Handle the response
}