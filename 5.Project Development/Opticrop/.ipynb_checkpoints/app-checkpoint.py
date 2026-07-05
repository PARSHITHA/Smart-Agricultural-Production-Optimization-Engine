from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/findyourcrop")
def find():
    return render_template("findyourcrop.html")


@app.route("/predict", methods=["POST"])
def predict():

    N = float(request.form["nitrogen"])
    P = float(request.form["phosphorus"])
    K = float(request.form["potassium"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    data = np.array([[N, P, K,
                      temperature,
                      humidity,
                      ph,
                      rainfall]])

    prediction = model.predict(data)[0]

    return render_template(
        "findyourcrop.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)