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

def get_quad_tuple(x, y, size):
    left_x = (size * x) + (x + 1)
    right_x = left_x + size
    top_y = (size * y) + (y + 1)
    bottom_y = top_y + size
    return (left_x, top_y, right_x, bottom_y)

def has_redshift(quad):
    for quad_x in range(0, 9):
        for quad_y in range(0, 9):
            rgb_quad = quad.convert('RGB')
            colors = rgb_quad.getpixel((quad_x, quad_y))
            if colors == (255, 0, 0):
                return True
    return False

boards = boards_str.split("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
for board in boards:
    images = list(filter(None, board.split("\n")))

    for x in range(0,5):
        for y in range(0,5):
            # print('{0}{1}'.format(X_LETTERS[x], y + 1))
            for i, image in enumerate(images):
                image_bytes = base64.b64decode(image)
                buf = io.BytesIO(image_bytes)
                pil_i = Image.open(buf)
                quad = pil_i.crop(get_quad_tuple(x, y, 9))
                if has_redshift(quad):
                    print('{0}{1}'.format(X_LETTERS[x], y + 1))
