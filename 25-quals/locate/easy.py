import base64
from PIL import Image
import sys
import io
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
    for i, image in enumerate(images):
        if image:
            image_bytes = base64.b64decode(image)
            buf = io.BytesIO(image_bytes)
            pi = Image.open(buf)
            # pi = Image.frombytes('RGB', (5, 5), image_bytes)
            pi.save('{0}.bmp'.format(str(i)))

    for x in range(0,5):
        for y in range(0,5):
            # print('{0}{1}'.format(X_LETTERS[x], y + 1))
            redshift = True
            red_high = 0
            for image in images:
                if image:
                    image_bytes = base64.b64decode(image)
                    buf = io.BytesIO(image_bytes)
                    pi = Image.open(buf)
                    # pi = Image.frombytes('RGB', (5, 5), image_bytes)
                    pi.save('{0}{1}.bmp'.format(X_LETTERS[x], y + 1))
                    rgb = pi.convert('RGB')
                    r, g, b = rgb.getpixel((x, y))
                    # print('{0} {1} {2}'.format(r,g,b))
                    # print('{0} {1}'.format(red_high, r))
                    if r > red_high:
                        red_high = r
                    else:
                        redshift = False
            if redshift:
                print('{0}{1}'.format(X_LETTERS[x], y + 1))
