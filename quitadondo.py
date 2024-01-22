from PIL import Image, ImageSequence
from rembg import remove, new_session
from io import BytesIO

def process_frame(frame):
    # Crear una nueva sesión con el modelo especificado
    session = new_session(model_name='isnet-anime')

    # Convertir el cuadro a formato que pueda ser procesado por rembg
    with BytesIO() as output:
        frame.save(output, format="PNG")
        input_data = output.getvalue()

    # Eliminar fondo usando la sesión creada
    output_data = remove(input_data, session=session)

    # Cargar la imagen procesada
    processed_frame = Image.open(BytesIO(output_data))
    return processed_frame

def process_gif(input_path, output_path):
    gif = Image.open(input_path)
    frames = []

    # Procesar cada cuadro del GIF
    for frame in ImageSequence.Iterator(gif):
        processed_frame = process_frame(frame)
        frames.append(processed_frame)

    # Guardar los cuadros procesados como un nuevo GIF
    frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, duration=gif.info['duration'])
    print(f"GIF procesado y guardado como '{output_path}'")

# Ruta del archivo GIF original y del nuevo GIF
input_gif = "ChicaPlanta.gif"
output_gif = "chica_planta_sin_fondo.gif"

process_gif(input_gif, output_gif)
