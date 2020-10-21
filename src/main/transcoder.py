from PIL import Image
import io

def transcode_image(data, file_name, size):
    im = Image.open(io.BytesIO(data))
    im.thumbnail((size, size))
    extension = im.format.lower()
    save_name = f'{file_name}.{extension}'
    im.save(save_name)
    return save_name
    