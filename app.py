import streamlit as st
import joblib

# Load model
model = joblib.load('injury_risk_model.pkl')

st.title("🏋️ Athlete Injury Risk Predictor")
st.write("Enter the athlete's details to predict injury risk level.")

# User inputs
age = st.slider("Age", 15, 40)
matches = st.slider("Matches Played", 0, 20)
training = st.slider("Training Hours/Week", 0, 20)
injuries = st.slider("Past Injuries", 0, 5)
sleep = st.slider("Sleep Hours/Night", 4.0, 9.0)
fitness = st.slider("Fitness Test Score", 30, 100)

if st.button("Predict Injury Risk"):
    data = [[age, matches, training, injuries, sleep, fitness]]
    pred = model.predict(data)
    risk_label = {0: 'High', 1: 'Low', 2: 'Medium'}
    st.success(f"🏷️ Predicted Injury Risk: **{risk_label[pred[0]]}**")
