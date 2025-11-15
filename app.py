from flask import Flask, render_template, request
from agents.health_agent import health_response
from agents.edu_agent import edu_response
from agents.env_agent import env_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    reply = ""
    if request.method == "POST":
        query = request.form["query"]
        category = request.form["category"]
        if category == "health":
            reply = health_response(query)
        elif category == "education":
            reply = edu_response(query)
        elif category == "environment":
            reply = env_response(query)
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
