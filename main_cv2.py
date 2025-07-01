import cv2
import os

# Ruta a la imagen base
ruta_imagen = "ejemplo.png"  # Cambiá esto por tu imagen
imagen_original = cv2.imread(ruta_imagen)

# Verificamos si la imagen se cargó correctamente
if imagen_original is None:
    raise FileNotFoundError("No se pudo cargar la imagen. Verificá la ruta.")

# Configuración del texto
font = cv2.FONT_HERSHEY_SIMPLEX
posicion = (50, 50)  # Coordenadas (x, y) del texto
color = (255, 255, 255)  # Blanco
grosor = 2
tamaño_fuente = 1

# Carpeta de salida
carpeta_salida = "imagenes_con_texto"
os.makedirs(carpeta_salida, exist_ok=True)

# Cantidad de imágenes que querés generar
cantidad = 1000

for i in range(500, cantidad + 1):
    imagen_copia = imagen_original.copy()

    if i > 999:
        texto = f"001-000{i}"
    else:
        texto = f"001-001000"
    
    cv2.putText(imagen_copia, texto, posicion, font, tamaño_fuente, color, grosor, cv2.LINE_AA)

    ruta_guardado = os.path.join(carpeta_salida, f"imagen_{i:03d}.jpg")
    cv2.imwrite(ruta_guardado, imagen_copia)

print(f"Se generaron {cantidad} imágenes en la carpeta '{carpeta_salida}'.")
