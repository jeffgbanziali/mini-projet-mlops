import streamlit as st
import joblib
import pandas as pd

# Chargement du modèle
model = joblib.load("regression.joblib")

st.title("Estimation du prix d'une maison")

size = st.number_input("Taille de la maison (m²)", min_value=0.0, value=None, step=1.0)
nb_rooms = st.number_input("Nombre de chambres", min_value=0, max_value=20, value=None, step=1)
garden = st.selectbox("Présence d'un jardin", options=[0, 1], format_func=lambda x: "Oui" if x == 1 else "Non")

if st.button("Estimer le prix"):
    if size is not None and nb_rooms is not None:
        data = pd.DataFrame([{
            "size": size,
            "nb_rooms": nb_rooms,
            "garden": garden
        }])
        prediction = model.predict(data)[0]
        st.success(f"Prix estimé : {prediction:,.2f} €")
    else:
        st.warning("Veuillez remplir tous les champs avant de lancer l'estimation.")