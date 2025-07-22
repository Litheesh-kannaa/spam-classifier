document.querySelector('#emailForm').addEventListener('submit', async function (e) {
  e.preventDefault();

  const email = document.querySelector('#emailInput').value;

  const response = await fetch('http://localhost:8000/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `email=${encodeURIComponent(email)}`,
  });

  const result = await response.text();

  const outputDiv = document.getElementById('result');
 outputDiv.textContent = result === 'spam' 
  ? 'This is a spam email.' 
  : result === 'not spam' 
    ? 'This is a genuine (not spam) email.' 
    : `Result: ${result}`;

  outputDiv.style.fontWeight = 'bold';
  outputDiv.style.fontSize = '1.2rem';
  outputDiv.style.marginTop = '10px';
});
