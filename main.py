# streamlit_app.py

import streamlit as st

# Título de la app
st.title('Mi Primera Aplicación con Streamlit')

# Descripción
st.write('¡Hola! Esta es una aplicación básica de Streamlit.')

# Caja de texto para entrada del usuario
nombre = st.text_input('¿Cómo te llamas?')

# Mostrar el saludo
if nombre:
    st.write(f'¡Hola, {nombre}! Encantado de conocerte. HICE UN CAMBIO')
