# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from deep_learning import DeepLearning
import numpy as np


app = Flask(__name__)
dl = DeepLearning(input_size=784, hidden_size=324, output_size=10)
dl.load("../data/deep_learning.dump")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/estimate", methods = ["POST"])
def estimate():
    try:
        x = np.array(request.json["input"]) / 255.0
        y = int(dl.predicate(x))
        return jsonify({"estimated": y})

    except Exception as e:
        print(e)
        return jsonify({"error": e})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
