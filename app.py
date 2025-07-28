from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Example challenge flags store
flags = {
    "challenge1": "flag{secret1}",
    "challenge2": "flag{secret2}",
    # Add more challenges as needed
}

# HTML template with embedded JS (same as before)
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>CTF Challenge Submission</title>
<style>
  body { font-family: Arial, sans-serif; margin: 2em; }
  .challenge-list button {
    display: block;
    margin: 0.5em 0;
    padding: 0.6em 1em;
    font-size: 1em;
    cursor: pointer;
  }
  .flag-form { margin-top: 1em; }
  .result { margin-top: 1em; font-weight: bold; }
</style>
</head>
<body>

<h1>CTF Challenges</h1>

<div class="challenge-list">
  <button data-challenge-id="challenge1">Challenge 1: Simple Flag</button>
  <button data-challenge-id="challenge2">Challenge 2: Another Flag</button>
</div>

<div class="flag-form" style="display:none;">
  <h2 id="challenge-title"></h2>
  <input type="text" id="flag-input" placeholder="Enter your flag here" size="30" />
  <button id="submit-flag">Submit Flag</button>
  <div class="result" id="result-message"></div>
</div>

<script>
  const challengeButtons = document.querySelectorAll('.challenge-list button');
  const flagForm = document.querySelector('.flag-form');
  const challengeTitle = document.getElementById('challenge-title');
  const flagInput = document.getElementById('flag-input');
  const submitButton = document.getElementById('submit-flag');
  const resultMessage = document.getElementById('result-message');

  let selectedChallengeId = null;

  challengeButtons.forEach(button => {
    button.addEventListener('click', () => {
      selectedChallengeId = button.getAttribute('data-challenge-id');
      challengeTitle.textContent = button.textContent;
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
        if (text.toLowerCase().includes('correct')) {
          resultMessage.style.color = 'green';
        } else {
          resultMessage.style.color = 'red';
        }
        resultMessage.textContent = text;
      })
      .catch(() => {
        resultMessage.style.color = 'red';
        resultMessage.textContent = 'Error submitting flag.';
      });
  });
</script>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html_template)

@app.route("/submit")
def submit_flag():
    challenge_id = request.args.get("challenge_id")
    flag = request.args.get("flag")

    if not challenge_id or not flag:
        return "Incorrect", 400

    if challenge_id not in flags:
        return "Incorrect", 400

    if flag == flags[challenge_id]:
        return "Correct"
    else:
        return "Incorrect"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
