from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")

def index():
    return jsonify({
        "data":data,
        "message":"Planet found",
    }),200

@app.route("/Planet")

def Planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "planet_data":planet_data,
        "message":"data shown"
    }),200

if __name__ == "__main__":
    app.run()

