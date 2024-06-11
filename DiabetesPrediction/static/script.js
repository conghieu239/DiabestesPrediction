// scripts.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('prediction-form');
    const resultDiv = document.getElementById('prediction-result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(prediction => {
            resultDiv.textContent = 'Predicted Outcome: ' + prediction;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
