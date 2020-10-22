from PIL import Image
import io

def get_new_size(size, new_size):
    width,height = size
    ratio = width/height
    if ratio >= 1:
        return (new_size, int(new_size/ratio))
    else:
        return (int(new_size*ratio), new_size)
        
def transcode_image(data, file_name, size):
    image = Image.open(io.BytesIO(data))
    extension = image.format.lower()
    new_size = get_new_size(image.size, size)
    image = image.resize(new_size, Image.ANTIALIAS)
    save_name = f'{file_name}.{extension}'
    image.save(save_name)
    return save_name


