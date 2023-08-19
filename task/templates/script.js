document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const inputText = document.getElementById('input-data').value;

    fetch('/make_prediction/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Get CSRF token from cookies
        },
        body: JSON.stringify({ input_text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('prediction-result').innerText = `Prediction: ${data.prediction}`;
    });
});

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
