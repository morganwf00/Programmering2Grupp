from flask import Flask, jsonify, render_template, request, redirect, url_for
from functions.data_fetcher import fetch_fuel_data
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = fetch_fuel_data()

    return render_template("index.html")

@app.route("/minmax")
def minMaxPris():
    return render_template("minMax.html")