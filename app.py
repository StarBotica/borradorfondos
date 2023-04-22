import streamlit as st
import Image

st.title("Eliminador de fondos")

# subo fichero (por defecto no admite varios a la vez)
fichero = st.file_uploader("Elige tu imagen...",type=['png', 'jpg'])

if fichero:
  
  imagen_subida = Image.open(fichero)
  st.image(image_subida)
  #fixed = remove()
  
  st.download_button("Descarga tu imagen aquí",fichero,mime="image/png")
