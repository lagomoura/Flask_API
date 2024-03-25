import cv2
from cv2 import cv2_imshow
import numpy as np
import os
from datetime import datetime


def efecto_blur(img, puntos):
  #.coordenadas del rectangulo
  x, y, w, h = cv2.boundingRect(puntos)

  #.identificando region de interes (ROI)
  roi =  img[y:y+h, x:x+w]

  #.Aplicando blur al roi en cascada
  for i in range(3):
    roi_blur = cv2.GaussianBlur(roi, (11,11), 50)

    #.Reemplazando zona roi por zona con blur
    img[y:y+h, x:x+w] = roi_blur

  return img

def qr_detector(img_path):
  for archivo in os.listdir(img_path):
    #.ruta de la img
    ruta_img = os.path.join(img_path, archivo)

    img = cv2.imread(ruta_img)

    if img is None:
      print(f'Imagen con problema {archivo}')

  #.Convertiendo a escala de grises
  img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  #.Inicilizando el detector de QR
  detector_qr = cv2.QRCodeDetector()

  #.Detector
  exito, puntos, qr_info = detector_qr.detectAndDecode(img_gris)

  #.Mostrando info qr
  if exito:
    print(f"QR Detectado!! {archivo}")
    print("Aplicando Blur...")
    img = efecto_blur(img, puntos)
    print('Blur aplicado')
    #.Creando carpeta
    carpeta_destino = 'QR_detectado'
    if not os.path.exists(carpeta_destino):
      os.makedirs(carpeta_destino)

    tag_tiempo = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    nombre_img = f"img_qr_detectado.{tag_tiempo}.jpg"
    ruta_img = os.path.join(carpeta_destino, nombre_img)
    cv2.imwrite(ruta_img, img)

    print('Imagen guardada')
  else:
    print("Sin QRs detectados")

def main():
  img_path = 'imgs'
  qr_detector(img_path)

main()