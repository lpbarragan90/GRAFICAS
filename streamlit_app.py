import pandas as pd
import plotly.express as px
import streamlit as st

# Datos de la tabla
data = {
    "Año": ["2025 YTD", 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016],
    "SCOTUSA": [-1.18, 57.85, 19.63, -32.25, 37.21, 33.09, 28.06, -6.89, 16.96, 17.08],
    "SCOTGLO": [5.52, 45.97, 3.08, -28.05, 8.53, 38.28, 17.84, -14.85, 16.04, 24.13],
    "SCOTEUR": [3.86, 17.78, 7.22, -33.50, 14.28, 12.27, 22.94, -19.68, 19.01, 17.22],
    "SCOTMA32": [2.93, 28.28, 6.83, -16.08, 7.03, 16.49, 11.87, -6.78, 8.62, 17.90],
    "SCOTGL+": [-0.71, 30.82, 9.36, -28.14, 21.49, 19.85, None, None, None, None],
    "SCOTLB": [2.72, 48.53, None, None, None, None, None, None, None, None],
    "CETES283": [9.21, 10.72, 11.10, 7.66, 3.46, 3.87, 6.81, 7.16, 6.11, 3.64],
    "S&P500": [1.46, 24.01, 23.79, -20.00, 27.00, 16.02, 30.99, -7.70, 19.19, 10.47],
    "NASDAQ": [-2.20, 30.78, 42.13, -33.50, 21.38, 43.36, 38.92, -6.21, 27.87, 10.78],
    "USDMXN": [-1.50, 22.61, -12.82, -5.00, 3.05, 5.05, -3.66, -0.04, -4.96, 20.41],
}

df = pd.DataFrame(data)
df.set_index("Año", inplace=True)
df = df.transpose()

st.title("Análisis Interactivo de Activos Financieros")

# Selección de activos
selected_assets = st.multiselect("Selecciona los activos a visualizar", df.index.tolist(), default=["S&P500", "NASDAQ"])

df_selected = df.loc[selected_assets]

graph_type = st.selectbox("Selecciona el tipo de gráfico", ["Línea", "Barras"])

fig = None
if graph_type == "Línea":
    fig = px.line(df_selected.transpose(), x=df_selected.columns, y=df_selected.index, markers=True, title="Evolución de Activos")
elif graph_type == "Barras":
    fig = px.bar(df_selected.transpose(), x=df_selected.columns, y=df_selected.index, barmode="group", title="Comparación de Activos")

st.plotly_chart(fig)

# Mostrar estadísticas
st.subheader("Estadísticas Generales")
st.write(df_selected.describe())
