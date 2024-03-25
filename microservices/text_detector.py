import easyocr

def text_detector(img_path):
  reader = easyocr.Reader(['es','en']) # this needs to run only once to load the model into memory

  resultado = reader.readtext(img_path)

  for ubicacion, texto, accuracy in resultado:

    if texto:
      print(f"Texto/Marca de agua detectado: {texto}")
      print(f"Ubicacion: {ubicacion}")
      print(f"Accuracy: {(accuracy * 100).round()}%")

  if len(resultado) == 0:
    print("Sin deteccion de texto/Marca de agua")


def main():
  img_path = "path"
  text_detector(img_path)

main()