import joblib
import pandas as pd
import streamlit as st

# Même ordre que dans train_model.py
FEATURES = ["size", "nb_rooms", "garden"]

model = joblib.load("regression.joblib")

st.title("Prédiction du prix d'une maison")

size = st.number_input("Taille (m²)", min_value=0, value=100)
nb_rooms = st.number_input("Nombre de chambres", min_value=0, value=3)
garden = st.number_input("Jardin (0 = non, 1 = oui)", min_value=0, max_value=1, value=0)

X = pd.DataFrame([[size, nb_rooms, garden]], columns=FEATURES)
prediction = model.predict(X)

st.write("Prix prédit :", round(float(prediction[0]), 2))
