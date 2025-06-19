import pandas as pd
import streamlit as st

st.title("Consulta de notas – Quiz Sistema Óseo")
df = pd.read_csv("Nota quiz S. Óseo.csv")

dni = st.text_input("Ingresa tu DNI:")
if st.button("Consultar"):
    fila = df[df["DNI"] == int(dni)]
    st.dataframe(fila.drop(columns=["DNI"])) if not fila.empty else st.error("DNI no encontrado")
