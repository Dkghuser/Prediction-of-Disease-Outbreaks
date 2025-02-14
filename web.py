import os
import pickle # pre-trained model
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Prediction of Disease Outbreaks", layout="wide", page_icon="🧊")
diabetes_model = pickle.load(open(r"D:\Deepak\OneDrive\Projects\AICTE internship\Prediction of disease outbreaks\saved models\diabetes_model.sav", "rb"))
heart_model = pickle.load(open(r"D:\Deepak\OneDrive\Projects\AICTE internship\Prediction of disease outbreaks\saved models\heart_model.sav", "rb"))
parkinsons_model = pickle.load(open(r"D:\Deepak\OneDrive\Projects\AICTE internship\Prediction of disease outbreaks\saved models\parkinsons_model.sav", "rb"))

with st.sidebar:
    selected_model = option_menu("Prediction of Disease Outbreaks", ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Disease"],
                                menu_icon='hospital-fill',icons=['activity', 'heart', 'person'],default_index=0)
    
if selected_model == "Diabetes Prediction":
    st.title("Diabetes Prediction using ML")
    st.write("Enter the following details to predict if you have diabetes or not.")
    pregnancies = st.number_input("Pregnancies", 0, 17, 3)
    glucose = st.number_input("Glucose", 0, 199, 117)
    blood_pressure = st.number_input("Blood Pressure", 0, 122, 72)
    skin_thickness = st.number_input("Skin Thickness", 0, 99, 23)
    insulin = st.number_input("Insulin", 0, 846, 30)
    bmi = st.number_input("BMI", 0.0, 67.1, 32.0)
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", 0.078, 2.42, 0.3725)
    age = st.number_input("Age", 21, 81, 29)
    
    if st.button("Predict"):
        prediction = diabetes_model.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
        if prediction == 1:
            st.error("You have diabetes.")
        else:
            st.success("You don't have diabetes.")


if selected_model == "Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")
    st.write("Enter the following details to predict if you have heart disease or not.")
    age = st.number_input("Age", 29, 77, 55)
    sex = st.number_input("Sex", 0, 1, 1)
    cp = st.number_input("Chest Pain Type", 0, 3, 1)
    trestbps = st.number_input("Resting Blood Pressure", 94, 200, 130)
    chol = st.number_input("Cholesterol", 126, 564, 250)
    fbs = st.number_input("Fasting Blood Sugar", 0, 1, 0)
    restecg = st.number_input("Resting ECG", 0, 2, 1)
    thalach = st.number_input("Max Heart Rate Achieved", 71, 202, 150)
    exang = st.number_input("Exercise Induced Angina", 0, 1, 0)
    oldpeak = st.number_input("ST Depression", 0.0, 6.2, 1.5)
    slope = st.number_input("Slope", 0, 2, 1)
    ca = st.number_input("Number of Major Vessels", 0, 4, 0)
    thal = st.number_input("Thalassemia", 0, 3, 1)

    if st.button("Predict"):
        prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if prediction == 1:
            st.error("You have a heart disease.")
        else:
            st.success("You don't have any heart disease.")


if selected_model == "Parkinson's Disease":
    st.title("Parkinson's Disease Prediction using ML")
    st.write("Enter the following details to predict if you have Parkinson's disease or not.")
    
    fo = st.number_input("Average vocal fundamental frequency (MDVP:Fo(Hz))", min_value=0.0, value=150.0)
    fhi = st.number_input("Maximum vocal fundamental frequency (MDVP:Fhi(Hz))", min_value=0.0, value=200.0)
    flo = st.number_input("Minimum vocal fundamental frequency (MDVP:Flo(Hz))", min_value=0.0, value=100.0)
    jitter_percent = st.number_input("Variation in fundamental frequency (MDVP:Jitter(%))", min_value=0.0, value=0.01)
    jitter_abs = st.number_input("Absolute variation in fundamental frequency (MDVP:Jitter(Abs))", min_value=0.0, value=0.0001)
    rap = st.number_input("Relative amplitude perturbation (MDVP:RAP)", min_value=0.0, value=0.01)
    ppq = st.number_input("Five-point period perturbation quotient (MDVP:PPQ)", min_value=0.0, value=0.01)
    ddp = st.number_input("Average absolute difference of differences between consecutive periods (Jitter:DDP)", min_value=0.0, value=0.03)
    shimmer = st.number_input("Variation in amplitude (MDVP:Shimmer)", min_value=0.0, value=0.02)
    shimmer_db = st.number_input("Variation in amplitude in decibels (MDVP:Shimmer(dB))", min_value=0.0, value=0.2)
    apq3 = st.number_input("Three-point amplitude perturbation quotient (Shimmer:APQ3)", min_value=0.0, value=0.01)
    apq5 = st.number_input("Five-point amplitude perturbation quotient (Shimmer:APQ5)", min_value=0.0, value=0.02)
    apq = st.number_input("Eleven-point amplitude perturbation quotient (MDVP:APQ)", min_value=0.0, value=0.02)
    dda = st.number_input("Average absolute difference of differences between consecutive amplitudes (Shimmer:DDA)", min_value=0.0, value=0.03)
    nhr = st.number_input("Noise-to-harmonics ratio (NHR)", min_value=0.0, value=0.02)
    hnr = st.number_input("Harmonics-to-noise ratio (HNR)", min_value=0.0, value=20.0)
    rpde = st.number_input("Recurrence period density entropy (RPDE)", min_value=0.0, value=0.5)
    dfa = st.number_input("Detrended fluctuation analysis (DFA)", min_value=0.0, value=0.5)
    spread1 = st.number_input("Nonlinear measure of fundamental frequency variation (spread1)", min_value=-10.0, value=-5.0)
    spread2 = st.number_input("Nonlinear measure of fundamental frequency variation (spread2)", min_value=0.0, value=0.5)
    d2 = st.number_input("Nonlinear measure of fundamental frequency variation (D2)", min_value=0.0, value=2.0)
    ppe = st.number_input("Nonlinear measure of fundamental frequency variation (PPE)", min_value=0.0, value=0.2)

    if st.button("Predict"):
        prediction = parkinsons_model.predict([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])
        if prediction == 1:
            st.error("You have Parkinson's disease.")
        else:
            st.success("You don't have Parkinson's disease.")