from flask import Flask, render_template


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    return render_template("dog.html")

## おまじない
if __name__ == "__main__":
    app.run(debug=True)