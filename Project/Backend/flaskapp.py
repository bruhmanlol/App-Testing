from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/test-message", methods = ["GET"])
def hello_world():
    return {
        "data": [
            {
                "name": "Joe",
                "age": 30
            },
            {
                "name": "John",
                "age": 43
            }
        ]
    }


if __name__ == "__main__":
    app.run(port = "5001", debug = True)