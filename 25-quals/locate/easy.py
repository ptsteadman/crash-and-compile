import base64
from PIL import Image
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
            decoded_image = base64.b64decode(image)
            print(decoded_image)

