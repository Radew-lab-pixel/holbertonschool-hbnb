/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

// document.addEventListener('DOMContentLoaded', () => {
    /* DO SOMETHING */
//  });

document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

  //const p_url = document.getElementById('')

  if (loginForm) {
      loginForm.addEventListener('submit', async (event) => {
          event.preventDefault();
          // Your code to handle form submission
         const email = document.getElementById('email');
         const password = document.getElementById('password');
      });
    }
    
  

  // for debugging 
  // Display URL information (if the element exists)
   const urlDisplayElement = document.getElementById('url-address');
   if (urlDisplayElement) {
     urlDisplayElement.textContent = `Current URL: ${window.location.href}`;
    // urlDisplayElement.textContent = `Current URL: ${document.url}`; not working
    // You could also show last modified date if needed
    // urlDisplayElement.textContent += ` | Last modified: ${document.lastModified}`;
  }
    
    // You could also show last modified date if needed
    // urlDisplayElement.textContent += ` | Last modified: ${document.lastModified}`;
  

});


async function loginUser(email, password) {
  //const response = await fetch('http://127.0.0.1:5500/api/v1/auth/login', {
  const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
  });
  // Handle the response
  if (response.ok) {
    const data = await response.json();
    document.cookie = `token=${data.access_token}; path=/`;
    window.location.href = 'index.html';
} else {
    alert('Login failed: ' + response.statusText);
}
}


// for testing purpose

// document.getElementById("url-address").innerHTML = document.URL;
 
// document.getElementById("url-address") = document.lastModified;
/* const urlAddressElement = document.getElementById("url-address");
  if (urlAddressElement) {
      urlAddressElement.textContent = "Last modified: " + document.lastModified;
  }
*/
  /* const p_url = document.querySelector('div.url_address');
  p_url.append(document.url); */
 

