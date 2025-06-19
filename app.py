import pandas as pd
import streamlit as st
import csv, io

st.title("Consulta de notas – Quiz Sistema Óseo")

# ---------- CARGA ROBUSTA DEL CSV ----------
csv_path = "Nota quiz S. Óseo.csv"

# Detecta el separador (coma o punto-y-coma)
with open(csv_path, "r", encoding="utf-8") as f:
    sample = f.read(1024)
    f.seek(0)
    dialect = csv.Sniffer().sniff(sample, delimiters=";,")
    df = pd.read_csv(f, sep=dialect.delimiter, decimal=",")  # decimal=',' admite 1,0 ó 1.0

# Limpia posibles espacios invisibles en los nombres de columna
df.columns = df.columns.str.strip()

# Nombre exacto de la columna con el documento
COL = "No. DNI"          # si sigue fallando, añade st.write(list(df.columns)) para ver el nombre real

# ---------- INTERFAZ ----------
dni = st.text_input("Ingresa tu DNI:")

if st.button("Consultar"):
    fila = df[df[COL].astype(str) == dni.]()
