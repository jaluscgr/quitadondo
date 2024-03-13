# sudo apt-get update
# sudo apt-get install potrace
# pip install Pillow

from PIL import Image
import subprocess

def convert_webp_to_bmp(webp_image_path, bmp_image_path):
    """
    Convierte una imagen .webp a .bmp utilizando Pillow.
    
    Parámetros:
    - webp_image_path: La ruta al archivo de imagen .webp.
    - bmp_image_path: La ruta donde se guardará el archivo .bmp.
    """
    with Image.open(webp_image_path) as image:
        image.save(bmp_image_path, 'BMP')

def convert_bitmap_to_svg(bmp_image_path, svg_image_path):
    """
    Convierte una imagen bitmap (.bmp) a SVG utilizando Potrace.
    
    Parámetros:
    - bmp_image_path: La ruta al archivo de imagen bitmap (.bmp).
    - svg_image_path: La ruta al archivo SVG de salida.
    """
    command = ['potrace', '-s', '-o', svg_image_path, bmp_image_path]
    try:
        subprocess.run(command, check=True)
        print(f"Conversión exitosa. SVG guardado en: {svg_image_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error al convertir a SVG: {e}")

# Rutas de los archivos
webp_image_path = 'imagen.webp'  # Actualiza esto con la ruta a tu imagen .webp
bmp_image_path = 'imagen_temporal.bmp'  # Ruta temporal para el archivo .bmp
svg_image_path = 'salida.svg'  # Ruta para el archivo SVG final

# Convertir de .webp a .bmp
convert_webp_to_bmp(webp_image_path, bmp_image_path)

# Convertir de .bmp a .svg
convert_bitmap_to_svg(bmp_image_path, svg_image_path)