from PIL import Image
from time import time
import io
def transcode_image(data, file_name, size):
    st = time()
    im = Image.open(io.BytesIO(data))
    im.thumbnail((size, size))
    extension = im.format.lower()
    save_name = f'{file_name}.{extension}'
    fn = time()
    took = fn-st
    return im
    # print(f'Converted {size} file - {took}')
    