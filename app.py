 
from flask import Flask, render_template, request
from pathlib import Path
from datetime import datetime

app = Flask(__name__)

# Demo data isi folder me save hogi
DATA_FILE = Path("submissions.txt")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username", "").strip()
    game = request.form.get("game", "").strip()

    if not username or not game:
        return "Please fill both fields.", 400

    username = username[:50]
    game = game[:50]

    # Demo data save
    with DATA_FILE.open("a", encoding="utf-8") as file:
        file.write(
            f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Username: {username}\n"
            f"Favorite Game: {game}\n"
            f"------------------------------\n"
        )

    # Submit ke baad simple confirmation
    return """
    <html>
    <head>
        <title>Demo Submitted</title>
        <style>
            body {
                font-family: Arial;
                background: #fafafa;
                text-align: center;
                padding-top: 100px;
            }
            .box {
                background: white;
                display: inline-block;
                padding: 35px;
                border: 1px solid #ddd;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>✅ Demo submitted</h2>
            <p>Your demo information was saved.</p>
            <a href="/">Go back</a>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    print("===================================")
    print("       DEMO SERVER STARTED")
    print("===================================")
    print("PC: http://127.0.0.1:5000")
    print("Data: submissions.txt")
    print("===================================")

    app.run(host="0.0.0.0", port=5000, debug=False)

