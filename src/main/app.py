from flask import Flask, render_template
import requests

app = Flask(__name__)

# Repository we want to analyze
REPO_OWNER = "octocat"
REPO_NAME = "Hello-World"

def get_pull_requests():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
    response = requests.get(url)
    return response.json()

@app.route("/")
def dashboard():
    prs = get_pull_requests()
    total_prs = len(prs)

    return render_template("dashboard.html",
                           prs=prs,
                           total_prs=total_prs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)