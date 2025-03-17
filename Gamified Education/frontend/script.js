function submitAnswer() {
    const answer = document.getElementById('answer-input').value;

    fetch('/submit_answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ answer: answer })
    }).then(response => response.json())
      .then(data => alert(data.message));
}
