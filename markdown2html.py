#!/usr/bin/python3
'''script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name'''

import markdown
import sys

if len(sys.argv) != 3:
    print("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

first = sys.argv[1]
sec = sys.argv[2]

try:
    with open(first, 'r') as f:
        tempMd = f.read()
except FileNotFoundError:
    print("Missing {} ".format(first))
    sys.exit(1)

textmark = markdown.markdown(tempMd)

with open(sec, 'w') as f:
    f.write(textmark)
