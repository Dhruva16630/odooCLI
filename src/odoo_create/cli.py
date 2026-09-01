import sys
from generator import create_module


if len(sys.argv) < 2:
    print("Usage: python cli.py <module_name>")
else:
    create_module(sys.argv[1])

    