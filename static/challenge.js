console.log("here")

const challengeButtons = document.querySelectorAll('.challenge-list button');
const flagForm = document.querySelector('.flag-form');
const challengeTitle = document.getElementById('challenge-title');
const challengeCategory = document.getElementById('challenge-category');
const challengeDescription = document.getElementById('challenge-description');
const flagInput = document.getElementById('flag-input');
const submitButton = document.getElementById('submit-flag');
const resultMessage = document.getElementById('result-message');

let selectedChallengeId = null;

challengeButtons.forEach(button => {
button.addEventListener('click', () => {
    selectedChallengeId = button.getAttribute('data-challenge-id');
    challengeTitle.textContent = button.textContent;
    challengeCategory.textContent = button.getAttribute('data-category');
    challengeDescription.textContent = button.getAttribute('data-description');
    flagInput.value = '';
    resultMessage.textContent = '';
    flagForm.style.display = 'block';
    flagInput.focus();
});
});

submitButton.addEventListener('click', () => {
const flag = flagInput.value.trim();
if (!flag) {
    resultMessage.textContent = 'Please enter a flag.';
    resultMessage.style.color = 'red';
    return;
}

fetch(`/submit?challenge_id=${encodeURIComponent(selectedChallengeId)}&flag=${encodeURIComponent(flag)}`)
    .then(response => response.text())
    .then(text => {
    if (text.toLowerCase().includes('incorrect')) {
        resultMessage.style.color = 'red';
    } else {
        resultMessage.style.color = 'green';
    }
    resultMessage.textContent = text;
    })
    .catch(() => {
    resultMessage.style.color = 'red';
    resultMessage.textContent = 'Error submitting flag.';
    });
});