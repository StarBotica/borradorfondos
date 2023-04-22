import streamlit as st
from PIL import Image
from PIL.ImageFilter import *
# documentación: https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html

st.title("Eliminador de fondos")

filtros = ['BLUR','CONTOUR','DETAIL']
with st.sidebar:
  seleccionados = st.multiselect("Elige los filtros que deseas aplicar...",filtros)

# subo fichero
# (por defecto no admite varios a la vez)
# especificando el tipo de fichero para que sea una imagen
fichero = st.file_uploader("Elige tu imagen...",type=['png', 'jpg'])

if fichero:  
  imagen_subida = Image.open(fichero)
  imagen_editada = imagen_subida
  # mostramos la imagen original
  st.image(imagen_subida)
  # aplicamos los filtros seleccionados
  if 'BLUR' in seleccionados:
    imagen_editada = imagen_subida.filter(BLUR)
  if 'CONTOUR' in seleccionados:
    imagen_editada = imagen_subida.filter(CONTOUR)
  if 'DETAIL' in seleccionados:
    imagen_editada = imagen_subida.filter(DETAIL)
  st.image(imagen_editada)
  st.download_button("Descarga tu imagen aquí",fichero,mime="image/png")
