import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

## import ridge regressor model and standard scaler pickle

ridge_model = pickle.load(open(r'E:\AnacondaWorkspace\pwskillmds\4_Machine_Learning\6_Linear_Regression\3_Algerian_forest_fire_Project\model\ridge.pkl', 'rb'))
standard_scaler = pickle.load(open(r'E:\AnacondaWorkspace\pwskillmds\4_Machine_Learning\6_Linear_Regression\3_Algerian_forest_fire_Project\model\scaler.pkl', 'rb'))

## route for home page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pred', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))
        new_data_scaled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data_scaled)
        return render_template('home.html',result=result[0])
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")