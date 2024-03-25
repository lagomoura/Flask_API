import cv2
import os
from skimage.metrics import structural_similarity as ssim #calcula la similitud estructural entre dos imágenes

def calcular_huella(img):
  img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convierte la img en escala de gris
  return cv2.Laplacian(img_gris, cv2.CV_64F).var() #Calcula la huella perceptiva de la imagen convirtiéndola a Laplacian y calculando la varianza.

def comparar_imgs(img1, img2):
  huella1 = calcular_huella(img1) #Calcula la huella perceptiva de la imagen.
  huella2 = calcular_huella(img2)
  similitud = ssim(img1, img2, channel_axis=2) #Calcula la similitud estructural / el argumento channel_axis=2 Indica que los canales de color se encuentran en el tercer eje de la imagen. 

  return huella1, huella2, similitud

def buscar_imgs_similares(carpeta):
  imgs = []
  for archivo in os.listdir(carpeta):
    if archivo.endswith(".jpg") or archivo.endswith(".png") or archivo.endswith(".jpeg"):
      ruta = os.path.join(carpeta, archivo)
      img = cv2.imread(ruta)
      imgs.append((ruta, img))

  imgs_similares = []
  for i in range(len(imgs)):
    for j in range(i+1, len(imgs)):
      huella1, huella2, similitud = comparar_imgs(imgs[i][1], imgs[j][1])
      if similitud > 0.9:
        imgs_similares.append((imgs[i][0], imgs[j][0], similitud))
      else:
        print(f"No hay similitud entre imgs {similitud}") 
  
  return imgs_similares 

carpeta_imgs = '/content/imgs'

imgs_similares = buscar_imgs_similares(carpeta_imgs)

for img1, img2, similitud in imgs_similares:
  print(f"Img1: {img1}, Img2: {img2}, Similitud: {(similitud * 100).round(2)}%")