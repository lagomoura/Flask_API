import torch
import clip
from PIL import Image
from transformers import AutoModelForImageClassification, ViTImageProcessor

def detectar_humano():
  device = "cuda" if torch.cuda.is_available() else "cpu"
  model, preprocess = clip.load("ViT-B/32", device=device)

  image_path = "src/imgs/a1.png"
  image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
  text = clip.tokenize(["a human", "a manikin"]).to(device)

  with torch.no_grad():
      logits_per_image, logits_per_text = model(image, text)
      probs = logits_per_image.softmax(dim=-1).cpu().numpy()

  if probs[0][0] > 0.7:
    humano = True
    print("Humano detectado")
    detectar_nsfw(humano, image_path)
  else:
    humano = False
    print("No humano - Procesamiento finalizado!")


def detectar_nsfw(humano, image_path):
  img = image_path
    
  #.Modelo preentrenado
  model = AutoModelForImageClassification.from_pretrained("Falconsai/nsfw_image_detection") #carga el modelo desde la ubicación especificada
    
  #.Carga un procesador específico para el modelo de detección de contenido
  processor = ViTImageProcessor.from_pretrained('Falconsai/nsfw_image_detection')
    
  #.Upload Image
  img = Image.open(img)
    
  #.Operacion de inferencia sin calculo de gradiente
  with torch.no_grad():
    inputs = processor(images=img, return_tensors="pt") #pt = tensor pytorch
    outputs = model(**inputs)
    logits = outputs.logits 
    
  predicted_label = logits.argmax(-1).item()
    
  print(f"Sensibilidad de la foto: {model.config.id2label[predicted_label]}")


def main():
  detectar_humano()

main()