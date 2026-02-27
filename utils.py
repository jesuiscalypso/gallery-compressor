import os
import sys
from argparse import Namespace
from pathlib import Path

from validation import ArgumentValidator


def validate_arguments(args:Namespace):
    valid = ArgumentValidator.validate_directory_strict(args.directory)
    if not valid:
        raise Exception("Invalid directory")
    valid = ArgumentValidator.validate_directory(args.output_directory)
    if not valid:
        raise Exception("Invalid directory")
    valid = ArgumentValidator.validate_quality(args.quality)
    if not valid:
        raise Exception("Invalid quality")

def get_path(path_str: str) -> Path:
    path = Path(path_str)
    return path

def fatal(msg: str, code: int = 1):
    print(msg)
    sys.exit(code)

def resource_path(relative_path:str):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
