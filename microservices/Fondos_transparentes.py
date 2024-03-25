import rembg
import numpy as np
from PIL import Image
import os

import os

def quitar_fondos(file_path):

  for archivo in os.listdir(file_path):
    if archivo.endswith('jpg') or archivo.endswith('jpeg'):

      ruta_img = os.path.join(file_path, archivo)

      input_img = Image.open(ruta_img)

      input_array = np.array(input_img) #.Pasando img a array

      #.Eliminando fondo
      output_array = rembg.remove(input_array)

      #.Nueva img sin bg - Asignando RGBA para poder trabajar con la transparecia de fondo
      output_img = Image.fromarray(output_array, "RGBA")

      #.Guardando img en formato .png
      ruta_salida = os.path.join('sample_data/imgs/tratadas', os.path.splitext(archivo)[0] + ".png")
      output_img.save(ruta_salida)

      print('Procesando...')
      print(f"Archivo: {archivo} listo!")

  print('Fin del proceso')

  #Tiempo de procesamiento sin acelerator - 3.55s/img
  #Tiempo de procesamiento con T4 GPU - 3.11s/img
  
def main():
  file_path = '/content/sample_data/imgs'
  quitar_fondos(file_path)

main()