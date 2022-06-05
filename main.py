# Orchestration of the BL happens here.

from PIL import Image

print('Loading PyAsciiArt...')

print(PIL.__version__)

im = Image.open('source/title.png', 'r')
pix_val = list(im.getdata())
print(pix_val)
# pix_val_flat = [x for sets in pix_val for x in sets]

print('Done')