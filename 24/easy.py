
# Read input

boards_str = ""
try:
    while True:
        boards_str += input() + "\n"
except EOFError:
    pass

pass

boards = boards_str.split("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
for board in boards:
    rows = board.split("\n")
    next_row = True
    for row in rows:
        if len(row) > 0 and next_row:
            if row[1] == "#":
                print(0,end="")
            else:
                print(1, end="")
        if len(row) > 0 and row[0] == "+":
            next_row = True
        else:
            next_row = False
    print("\r")

