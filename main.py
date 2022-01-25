from flask import Flask, render_template


app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return render_template("dog.html")

@app.route("/item", methods=["GET"])
def item():
    return render_template("item.html")

## おまじない
if __name__ == "__main__":
    app.run(debug=True)