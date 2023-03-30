#!/usr/bin/python3
# script markdown2html.py that takes an argument 2 strings
"""script markdown2html.py that takes an argument 2 strings"""
import markdown
import sys


# script markdown2html.py that takes an argument 2 strings
"""script markdown2html.py that takes an argument 2 strings"""
if len(sys.argv) != 3:
    """script markdown2html.py that takes an argument 2 strings"""
    print("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

first = sys.argv[1]
sec = sys.argv[2]

try:
    # script markdown2html.py that takes an argument 2 strings
    """script markdown2html.py that takes an argument 2 strings"""
    with open(first, 'r') as f:
        tempMd = f.read()
except FileNotFoundError:
    # script markdown2html.py that takes an argument 2 strings
    """script markdown2html.py that takes an argument 2 strings"""
    print("Missing {} ".format(first))
    sys.exit(1)

textmark = markdown.markdown(tempMd)

with open(sec, 'w') as f:
    # script markdown2html.py that takes an argument 2 strings
    """script markdown2html.py that takes an argument 2 strings"""
    f.write(textmark)
