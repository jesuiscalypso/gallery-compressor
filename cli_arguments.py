import argparse

from gooey import Gooey, GooeyParser

from utils import resource_path


@Gooey(
    program_name="Gallery Compressor",
    image_dir=resource_path("assets")
)
def initialize_parser():
    parser = GooeyParser(
        prog='Gallery Compressor',
        description="Compresses every .png, .jpg or .jpeg file in a folder into a .webp",
        epilog="Made for the NekoWeb Discord Server",
    )

    return parser

def populate_parser(parser: GooeyParser):
    _ = parser.add_argument('directory', help='Input directory (i.e. where all the images are)', widget='DirChooser')

    _ = parser.add_argument('output_directory', help='Output directory (i.e. where all the images are going to be put once converted)', widget='DirChooser')

    _ = parser.add_argument('-q', '--quality', nargs='?', type=int, default=80, help='Level of quality for the output image in percentage (default is 80)', widget='IntegerField')
    


