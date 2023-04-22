import streamlit as st
from PIL import Image
#from rembg import remove

st.title("Eliminador de fondos")

# subo fichero (por defecto no admite varios a la vez)
fichero = st.file_uploader("Elige tu imagen...",type=['png', 'jpg'])

if fichero:
  
  imagen_subida = Image.open(fichero)
  st.image(imagen_subida)
  #fixed = remove()
  
  st.download_button("Descarga tu imagen aquí",fichero,mime="image/png")
