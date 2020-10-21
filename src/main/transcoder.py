from PIL import Image
from time import time

def transcode_image(file_name, size):
    st = time()
    im = Image.open(file_name)
    im.thumbnail((size, size))
    extension = im.format.lower()
    save_name = f'{file_name}.{extension}'
    im.save(save_name)
    fn = time()
    took = fn-st
    return save_name
    # print(f'Converted {size} file - {took}')
    