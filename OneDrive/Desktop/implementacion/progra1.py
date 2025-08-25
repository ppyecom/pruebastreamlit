import streamlit as st
import pandas as pd
import numpy as np

#TItulo y subtitulo
st.title("Mi primera app con Streamlit")
st.header("Ejemplo usando Pandas y Numpy")
st.subheader("Mostrando texto, tablas y gráficos")

#Texto simple con formato markdown
st.markdown("Hola, este es un *ejemplo* de una aplicación web usando Streamlit.")

#Crear un dataframe con Pandas y Numpy
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['Columna A', 'Columna B', 'Columna C']
)

#Mostrar tabla
st.write("Aquí hay una tabla generada con Pandas:")
st.dataframe(data)

#Mostrar estadística
st.write("Resumen estadístico de los datos:")
st.write(data.describe())

#Mostrar gráfico interactivo
st.line_chart(data)

#Texto adicional con LaTeX
st.latex(r"E = mc^2")