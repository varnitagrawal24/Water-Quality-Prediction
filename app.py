
from urllib import request
from flask import Flask,render_template,url_for
import waterquality
import numpy as np
app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    parameter= request.form(['ph','Hardness','Solids','Chloramines','Sulfate','Conductivity','Organic_carbon','Trihalomethanes','Turbidity'])
    parameter=np.array(parameter)
    parameter=parameter.reshape(1,-1)
    output=waterquality.fun(parameter)
    return render_template('index.html',output=output)

if __name__=='__main__':
    app.run(debug=True)