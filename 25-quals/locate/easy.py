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

boards = boards_str.split("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
for board in boards:
    images = board.split("\n")
    for image in images:
        if image:
            image_bytes = base64.b64decode(image)
            i = Image.frombytes('RGB', (5, 5), image_bytes)
            print(i)

