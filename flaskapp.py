"""
needed for pylint. deploys flaskapp.
"""

import pickle
#import pandas as pd
#import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the trained model
#model = pickle.load(open("model.pkl", "rb"))

with open("model.pkl", "wb") as file:
    model = pickle.load(file)


@app.route("/")
"""
needed for pylint. deploys flaskapp.
"""
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get form data
    hours = float(request.form["hours"])

    # Predict scores
    prediction = model.predict([[hours]])[0]

    return render_template("results.html", hours=hours, prediction=round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
