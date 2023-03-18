# app.py

from flask import Flask, jsonify
from my_script import generate_data

app = Flask(__name__)

@app.route('/scatterplot-data')
def scatterplot_data():
    data = generate_data()
    return jsonify(data=data)
