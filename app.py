import streamlit as st

st.title("Eliminador de fondos")

# subo fichero (por defecto no admite varios a la vez)
fichero = st.file_uploader("Elige tu imagen...",type=['png', 'jpg'])

if fichero:
  st.download_button("Descarga tu imagen aquí",fichero,mime="image/png")
