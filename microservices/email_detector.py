import easyocr
import re

reader = easyocr.Reader(['es','en']) # this needs to run only once to load the model into memory

def detectar_email(texto):
  #.Regex para deteccion de correo
  patron_email = r'\b[A-Za-z0-9._%+-]*[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

  correos_encontrados = re.findall(patron_email, texto)

  return correos_encontrados

def email_detector(resultado):
  for ubicacion, texto, accuracy in resultado:

    emails = detectar_email(texto)

    if emails:
      print(f"Email detectado: {emails}")
      print(f"Ubicacion: {ubicacion}")
      print(f"Accuracy: {(accuracy * 100).round()}%")

  if len(resultado) == 0:
    print("Sin deteccion de email")
    

def main():
  resultado = reader.readtext('/content/emails.jpg')
  email_detector(resultado)
  
main()