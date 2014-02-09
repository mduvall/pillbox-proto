from flask import Flask, render_template, jsonify, request
from models.pill import Pill

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search/<query>")
def search(query):
    if request.args.get("representation") == "json":
        return jsonify(json_list=[p.serialize for p in Pill.search_by_name(query)])
    else:
        return render_template("pill-list.html", pills=Pill.search_by_name(query))

if __name__ == "__main__":
    app.run(debug=True)