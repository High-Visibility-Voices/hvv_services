from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "'ello YA'LL!"

if __name__ == "__main__":
    app.run()
