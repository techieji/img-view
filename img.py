from PIL import Image    # pip install pillow
import shutil

WIDTH, HEIGHT = shutil.get_terminal_size((50, 50))
WIDTH -= 10
HEIGHT -= 10

def print_rgb(col):
    r, g, b = col
    print(f'\x1b[38;2;{r};{g};{b}m█\x1b[0m', end="")

def view_file(filename):
    image = Image.open(filename)
    image.thumbnail((WIDTH, HEIGHT))
    col = 0
    for x in image.getdata():
        if col >= image.size[0]:
            print()
            col = 0
        print_rgb(x)
        col += 1
    print()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        HEIGHT = int(sys.argv[2])
    view_file(sys.argv[1])
