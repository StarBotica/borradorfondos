import streamlit as st
from PIL import Image
from PIL.ImageFilter import *
# documentación: https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html

# opcional: convertir imagen a binario para poder descargarla
# lo devuelto por esta imagen se le colocará al parámetro data de un botón download
def convertir(img):
  from io import BytesIO
  buf = BytesIO()
  img.save(buf, format="JPEG")
  byte_im = buf.getvalue()
  return byte_im

st.title("Eliminador de fondos")

filtros = ['BLUR','CONTOUR','DETAIL','SHARPEN']
with st.sidebar:
  seleccionados = st.multiselect("Elige los filtros que deseas aplicar...",filtros)

# subo fichero
# (por defecto no admite varios a la vez)
# especificando el tipo de fichero para que sea una imagen
fichero = st.file_uploader("Elige tu imagen...",type=['png', 'jpg'])

if fichero:  
  imagen_subida = Image.open(fichero)
  imagen_editada = imagen_subida
  # aplicamos los filtros seleccionados
  if 'BLUR' in seleccionados:
    imagen_editada = imagen_editada.filter(BLUR)  
  if 'CONTOUR' in seleccionados:
    imagen_editada = imagen_editada.filter(CONTOUR)
  if 'DETAIL' in seleccionados:
    imagen_editada = imagen_editada.filter(DETAIL)
  if 'SHARPEN' in seleccionados:
    imagen_editada = imagen_editada.filter(SHARPEN)
  
    
  # colocamos la imagen original y la editada en dos columnas
  col1, col2 = st.columns(2)

  with col1:
   st.header("Original")
   st.image(imagen_subida)
  with col2:
   st.header("Editada")
   st.image(imagen_editada)
  st.download_button("Descarga tu imagen aquí",data=convertir(imagen_editada),mime="image/png")
