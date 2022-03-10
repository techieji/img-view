from PIL import Image    # pip install pillow
import shutil
import itertools as it

WIDTH, HEIGHT = shutil.get_terminal_size((50, 50))
WIDTH = WIDTH * 2 - 10
HEIGHT = HEIGHT * 2 - 10

def print_arr(arr1, arr2):
    for color1, color2 in zip(arr1, arr2):
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        print(f'\033[38;2;{r1};{g1};{b1}m\033[48;2;{r2};{g2};{b2}m▀\033[0m', end="")
    print()

def view_file(image):
    image.thumbnail((WIDTH, HEIGHT))
    col = 0
    row = 0
    iterator = iter(image.getdata())
    try:
        while row <= image.size[1]:
            arr1 = list(it.islice(iterator, image.size[0]))
            arr2 = list(it.islice(iterator, image.size[0]))
            print_arr(arr1, arr2)
            row += 2
    finally:
        print()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        HEIGHT = int(sys.argv[2])
    view_file(Image.open(sys.argv[1]))
