from flask import Flask, request
import numpy as np 
import pandas as dp 
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)

app = application

#Route for home page:
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', method=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data=CustomData
