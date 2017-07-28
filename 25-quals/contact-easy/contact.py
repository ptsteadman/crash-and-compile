from string import ascii_uppercase
from sys import stdin, stdout

space = list(ascii_uppercase)
space.insert(0, ' ')

table = {}

for i, c in enumerate(space):
    table[str((i*2)+1)] = c

def contact():
    message = ''

    for line in stdin.readlines():
        line = line.strip()
        if not '*' in line:
            continue
        if all([c == '%' for c in line]):
            break
        message += table[str(len(line))]

    stdout.write(message + '\n')


if __name__ == '__main__':
    contact()
