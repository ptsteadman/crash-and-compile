import base64
from PIL import Image
import sys
# Read input

boards_str = ""
try:
    while True:
        boards_str += input() + "\n"
except EOFError:
    pass

pass

X_LETTERS = ['A', 'B', 'C', 'D', 'E']

boards = boards_str.split("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
for board in boards:
    images = board.split("\n")
    pil_images = []
    for image in images:
        if image:
            image_bytes = base64.b64decode(image)
            i = Image.frombytes('RGB', (5, 5), image_bytes)
            pil_images.append(i)

    for x in range(0,5):
        for y in range(0,5):
            redshift = True
            red_high = 0
            for pi in pil_images:
                r, g, b = pi.getpixel((x, y))
                if r > red_high:
                    red_high = r
                else:
                    redshift = False
                    red_high = r # necessary?
            if redshift:
                print('{0}{1}'.format(X_LETTERS[x], y))




