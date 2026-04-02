from flask import Flask, render_template, request
import requests
from collections import Counter

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    pulls = []
    total_prs = 0
    authors = {}
    states = {"open": 0, "closed": 0}

    if request.method == "POST":
        owner = request.form.get("owner")
        repo = request.form.get("repo")

        url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=all&per_page=100"
        response = requests.get(url)

        if response.status_code == 200:
            pulls = response.json()
            total_prs = len(pulls)

            # Count PRs per author
            author_list = [pr["user"]["login"] for pr in pulls]
            authors = dict(Counter(author_list))

            # Count PR states
            for pr in pulls:
                if pr["state"] == "open":
                    states["open"] += 1
                else:
                    states["closed"] += 1

    return render_template(
        "index.html",
        pulls=pulls,
        total_prs=total_prs,
        authors=authors,
        states=states
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)