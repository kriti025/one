from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('logistic_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
	if request.method == 'POST' and request.form:
		p = int(request.form['p'])
		g = int(request.form['g'])
		bp = int(request.form['bp'])
		st = int(request.form['st'])
		i = int(request.form['i'])
		bmi=float(request.form['bmi'])
		dpf=float(request.form['dpf'])
		age=int(request.form['age'])
		prediction=model.predict([[p,g,bp,st,i,bmi,dpf,age]])
		output=prediction[0]
		if output==0:
			return render_template('predicted.html',prediction_text="You do not have Diabetes")
		else:
			return render_template('predicted.html',prediction_text="You have Diabetes .You should visit your doctor.")
	else:
		return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)