#model1

import sys

from PIL import Image
from rembg import remove


def main():
    input_path = sys.arvg[1]
    output_path = sys.arvg[2]
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)
    
if __name__ == "__main__":
    main()