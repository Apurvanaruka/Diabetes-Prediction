# 🩺 Diabetes Prediction Web App

This is a **Flask-based web application** that predicts whether a person has diabetes or not based on clinical data. The backend uses a machine learning model trained on medical data to make predictions.

## 🔍 Overview

The application allows users to input their health metrics through a simple web form, which are then used by a pre-trained machine learning model to predict the likelihood of diabetes. The result is shown directly in the browser.

## 🧠 Model Training Process

### Dataset Used:
- **Pima Indians Diabetes Dataset** from UCI Machine Learning Repository.

### Features Used:
1. Pregnancies
2. Glucose
3. BloodPressure
4. SkinThickness
5. Insulin
6. BMI
7. DiabetesPedigreeFunction
8. Age

### Target Variable:
- `Outcome`: 1 = Diabetic, 0 = Not Diabetic

### Preprocessing Steps:
- Missing values were handled.
- Data was scaled using `StandardScaler`.

### Model Used:
- A classification model (`RandomForestClassifier`, `LogisticRegression`, etc.) trained on the dataset.
- The best-performing model was selected and saved as `classifier.pkl`.
- The scaler used for feature normalization was also saved as `scaler.pkl`.

## 🛠️ Technical Stack

- **Python 3.x**
- **Flask**: For building the web application
- **Scikit-learn**: For preprocessing and model
- **HTML/CSS**: For frontend templates

## 📁 Project Structure


## 🧾 Parameters Explained

| Parameter | Description |
|----------|-------------|
| **Pregnancies** | Number of times pregnant |
| **Glucose** | Plasma glucose concentration over 2 hours in an oral glucose tolerance test |
| **BloodPressure** | Diastolic blood pressure (mm Hg) |
| **SkinThickness** | Triceps skin fold thickness (mm) – used to estimate body fat |
| **Insulin** | 2-Hour serum insulin (mu U/ml) |
| **BMI** | Body Mass Index (weight in kg / (height in m)^2) |
| **DiabetesPedigreeFunction** | A function that scores the likelihood of diabetes based on family history |
| **Age** | Age in years |

## 🚀 How to Run the App

### Prerequisites:
Make sure you have Python and pip installed.

### Installation:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/diabetes-prediction-app.git 
cd diabetes-prediction-app