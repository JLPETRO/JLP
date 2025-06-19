import pandas as pd
import streamlit as st
import csv

st.title("Consulta de notas – Quiz Sistema Óseo")

# --- Carga robusta del CSV ---
csv_path = "Nota quiz S. Óseo.csv"

with open(csv_path, "r", encoding="utf-8") as f:
    sample = f.read(1024)
    f.seek(0)
    dialect = csv.Sniffer().sniff(sample, delimiters=";,")
    df = pd.read_csv(f, sep=dialect.delimiter, decimal=",")

df.columns = df.columns.str.strip()   # limpia espacios
COL = "No. DNI"                       # encabezado exacto de la columna

# --- Interfaz ---
dni = st.text_input("Ingresa tu DNI:")

if st.button("Consultar"):
    fila = df[df[COL].astype(str) == dni.strip()]   # ← línea corregida
    if fila.empty:
        st.error("DNI no encontrado")
    else:
        st.dataframe(fila.drop(columns=[COL]))
