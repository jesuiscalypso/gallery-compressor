import os
import sys

from gooey import Gooey
from PIL import Image

from cli_arguments import initialize_parser, populate_parser
from utils import get_path, validate_arguments

supported_images = ('.png', '.jpeg', 'jpg')

def main():
    parser = initialize_parser()
    populate_parser(parser)
    arguments = parser.parse_args()
    try:
        validate_arguments(arguments)
    except Exception as e:
        print(f"An error ocurred: {e}")
        sys.exit(1)

    dir = get_path(arguments.directory)
    out_dir = get_path(arguments.output_directory)
    
    if(not out_dir.is_dir()):
        try:
            out_dir.mkdir(parents=True)
        except OSError:
            print("Could not make")

    for file in os.listdir(dir):
        if file.endswith(supported_images):
            image = Image.open(file)
            new_name = str(out_dir) + "/" + str(image.filename) + ".webp"
            try:
                image.save(new_name, 'webp', optimize=True, quality = arguments.quality)
                print("Saved " + new_name)
            except:
                print("Error saving " + new_name)


if __name__ == '__main__':
    main()
