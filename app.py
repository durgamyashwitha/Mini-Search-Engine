from flask import Flask, render_template,request
from search_engine import search
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search_page():
    query = request.args.get("query")
    results = search(query)
    
    return render_template(
        "results.html",
        query = query,
        results = results,
        count = len(results)
    )

if __name__=="__main__":
    app.run(debug=True)