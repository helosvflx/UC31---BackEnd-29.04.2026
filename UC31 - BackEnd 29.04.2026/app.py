from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("contato.html")

@app.route("/home")
def home():
    return "heloisasevf@gmail.com"

if __name__ == "__main__":
    app.run(debug=True)