from PIL import Image, ImageDraw, ImageFont
import os

# Ruta de la imagen base
ruta_imagen = "ejemplo.png"
imagen_original = Image.open(ruta_imagen)

# Configuración de texto
fuente = ImageFont.load_default(size=40)  # Cambiá si querés usar otra fuente. Ejemplo ---> ImageFont.truetype("{font}", size=40)
posicion = (50, 50)
color = (255, 255, 255)

# Carpeta de salida
carpeta_salida = "imagenes_con_texto_pill"
os.makedirs(carpeta_salida, exist_ok=True)

cantidad = 1000

for i in range(500, cantidad + 1):
    imagen_copia = imagen_original.copy()
    draw = ImageDraw.Draw(imagen_copia)

    if i > 999:
        texto = f"001-001000"
    else:
        texto = f"001-000{i}"

    draw.text(posicion, texto, font=fuente, fill=color)
    
    ruta_guardado = os.path.join(carpeta_salida, f"imagen_{i:03d}.jpg")
    imagen_copia.save(ruta_guardado)

print(f"Se generaron {cantidad} imágenes con texto usando Pillow.")
