import easyocr
import re

reader = easyocr.Reader(['es','en']) #. this needs to run only once to load the model into memory

def detectar_url(texto):
  patron_url = r'(?:https?://)?(?:www\.)?[\w-]+\.(?:com|net|org|edu|gov|mil|int|co|io|ai)(?:/[\w/.-]*)*(?:\?[\w=&%-]*)?'
  urls_encontradas = re.findall(patron_url, texto)

  return urls_encontradas

#.upload foto
result = reader.readtext('/content/text.jpeg')

for ubicacion, texto, accuracy in result:

  urls = detectar_url(texto)

  if urls:
    print(f"URL encontrada: {urls}")
    print(f"Ubicacion del texto: {ubicacion}")
    print(texto)
    print(f"Accuracy de deteccion: {(accuracy * 100).round()}%")

if len(result) == 0:
  print("Imagen sin URLs")