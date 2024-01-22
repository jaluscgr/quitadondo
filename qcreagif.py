from PIL import Image
import os



# Ruta de la carpeta que contiene las imágenes PNG
input_folder = 'gifsinfondo'

# Nombre del archivo GIF resultante
output_gif = 'resultado_sin_fondo.gif'

# Leer todos los archivos de la carpeta especificada
images = []

for file_name in sorted(os.listdir(input_folder)):
    if file_name.endswith('.png'):
        file_path = os.path.join(input_folder, file_name)
        images.append(Image.open(file_path))

# Asegurarse de que todas las imágenes se convierten al mismo modo
images = [image.convert('RGBA') for image in images]

# Convertir la lista de imágenes en un GIF
images[0].save(
    output_gif,
    save_all=True,
    append_images=images[1:],
    duration=100,  # Duración en milisegundos entre los fotogramas
    loop=0,  # Número de bucles (0 significa bucle infinito)
    transparency=0,  # Asume que el color en la posición 0 de la paleta es el transparente
    disposal=2  # Indica que cada cuadro se dibuja encima del anterior
)

print("GIF creado con éxito.")
