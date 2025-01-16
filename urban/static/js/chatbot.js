function sendMessage() {
    const userMessage = document.getElementById("user-input").value;
    if (!userMessage) {
        return;
    }
    fetch('http://localhost:5005/webhooks/rest/webhook', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            sender: 'user',
            message: userMessage
        })
    })
    .then(response => response.json())
    .then(data => {
        const messages = document.getElementById("messages");
        messages.innerHTML += `<div class='user-message'>${userMessage}</div>`;
        data.forEach(reply => {
            messages.innerHTML += `<div class='bot-message'>${reply.text}</div>`;
        });
        document.getElementById("user-input").value = "";  // Clear input after sending message
    })
    .catch(error => {
        console.error("Error:", error);
    });
}