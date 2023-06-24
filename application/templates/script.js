// JavaScript code for handling form submission and updating the page

document.addEventListener('DOMContentLoaded', function() {
  const submitBtn = document.getElementById('submitBtn');
  const descriptionInput = document.getElementById('description');
  const outputDiv = document.getElementById('output');

  submitBtn.addEventListener('click', function(event) {
    event.preventDefault(); // Prevent form submission

    const description = descriptionInput.value;

    // Send the description to the backend
    sendData(description);
  });

  function sendData(description) {
    // Send an HTTP POST request to the backend with the description data
    // You will need to implement the backend server logic separately

    // Example using fetch API
    fetch('/api/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ description: description })
    })
    .then(response => response.json())
    .then(data => {
      // Display the updated text on the page
      outputDiv.textContent = data.updatedText;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
});
