from flask import Flask, render_template, request 
import pickle

app = Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html')

scaler = pickle.load(open('model/scaler.pkl','rb'))
classifier = pickle.load(open('model/classifier.pkl','rb'))

@app.route('/predication',methods=['GET','POST'])
def predicationPage():
    if request.method == "POST":
        Pregnancies = float(request.form.get('Pregnancies'))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        scaled_data = scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        score = classifier.predict(scaled_data)
        result = ""
        if score == 1:
            result = "Diebetes"
        else:
            result = "Not Diebetes"
        return render_template('home.html',result = result)
    else:
        return render_template('home.html')


# Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome