from PIL import Image, ImageSequence
from rembg import remove, new_session
from io import BytesIO
import os

def separate_gif_frames(input_gif, output_folder):
    gif = Image.open(input_gif)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for i, frame in enumerate(ImageSequence.Iterator(gif)):
        frame.save(f"{output_folder}/frame_{i:03d}.png")

def force_full_transparency(image):
    """Convertir cualquier píxel semi-transparente en completamente transparente."""
    alpha = image.split()[-1]  # Obtener el canal alfa
    alpha = alpha.point(lambda p: p > 128 and 255)  # Convertir semi-transparencia en transparencia completa
    image.putalpha(alpha)
    return image

def process_frame(input_image_path, output_image_path):
    session = new_session(model_name='isnet-anime')
    with open(input_image_path, "rb") as file:
        input_data = file.read()
    output_data = remove(input_data, session=session)
    image = Image.open(BytesIO(output_data))

    # Forzar la transparencia completa
    image = force_full_transparency(image)

    image.save(output_image_path, format='PNG')

def create_processed_gif(input_folder, output_gif, duration):
    frames = []
    file_names = sorted(os.listdir(input_folder))
    for file_name in file_names:
        if file_name.endswith('.png'):
            frame = Image.open(os.path.join(input_folder, file_name))
            frames.append(frame)
    frames[0].save(output_gif, save_all=True, append_images=frames[1:], loop=0, duration=duration)
    print(f"GIF procesado y guardado como '{output_gif}'")

# Rutas
input_gif = "Heria.gif"
separated_frames_folder = "gifsuelta"
processed_frames_folder = "gifsinfondo"

# 1. Separar GIF en cuadros individuales
separate_gif_frames(input_gif, separated_frames_folder)

# 2. Procesar cada cuadro
if not os.path.exists(processed_frames_folder):
    os.makedirs(processed_frames_folder)
for file_name in sorted(os.listdir(separated_frames_folder)):
    if file_name.endswith('.png'):
        input_path = os.path.join(separated_frames_folder, file_name)
        output_path = os.path.join(processed_frames_folder, file_name)
        process_frame(input_path, output_path)

# 3. Crear el GIF procesado
output_gif = "resultado_sin_fondo.gif"
gif = Image.open(input_gif)
create_processed_gif(processed_frames_folder, output_gif, gif.info['duration'])
