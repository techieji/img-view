from PIL import Image    # pip install pillow
import shutil

WIDTH, HEIGHT = shutil.get_terminal_size((50, 50))
WIDTH -= 10
HEIGHT -= 10

def print_rgb(color, stdscr=None):
    r, g, b = color
    print(f'\x1b[38;2;{r};{g};{b}m█\x1b[0m', end="")
    print(f'\x1b[38;2;{r};{g};{b}m█\x1b[0m', end="")

def view_file(image):
    image.thumbnail((WIDTH, HEIGHT))
    col = 0
    for x in image.getdata():
        if col >= image.size[0]:
            print()
            col = 0
        try:
            print_rgb(x)
        except:
            print('e', end='')
        col += 1
    print()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        HEIGHT = int(sys.argv[2])
    view_file(Image.open(sys.argv[1]))
