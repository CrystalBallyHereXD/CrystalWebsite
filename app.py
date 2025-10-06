from flask import Flask, render_template
import json
import os
print("Running in folder:", os.getcwd())

app = Flask(__name__)

# load buttons
with open("data.json") as f:
    buttons = json.load(f)["buttons"]

@app.route("/")
def home():
    return render_template("index.html", buttons=buttons)

@app.route("/chh")
def chh_page():
    return render_template("chh.html")

@app.route("/stickmen.html")
def stickmen_page():
    return render_template("stickmen.html")

if __name__ == "__main__":
    app.run(debug=True)
