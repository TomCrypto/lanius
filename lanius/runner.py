from pygments.styles import STYLE_MAP
from lanius.themes import THEME_LIST
from lanius.renderer import Renderer

import subprocess
import fileinput
import lxml.html
import markdown
import argparse
import sys
import os


def run(argv=None):
    parser = argparse.ArgumentParser(description="Lanius Markdown Viewer.")

    default_arg = os.getenv('LANIUS_THEME', 'default')
    parser.add_argument('-t', '--theme', default=default_arg,
                        help="theme to use for markdown display",
                        metavar='KEY', choices=THEME_LIST.keys())

    default_arg = os.getenv('LANIUS_STYLE', 'monokai')
    parser.add_argument('-x', '--style', default=default_arg,
                        help="syntax highlighting style to use",
                        metavar='KEY', choices=STYLE_MAP.keys())

    default_arg = os.getenv('LANIUS_FORMAT', 'color256')
    parser.add_argument('-f', '--format', default=default_arg,
                        help="syntax highlighting format to use",
                        metavar='KEY', choices=['none', 'color', 'color256'])

    default_arg = os.getenv('LANIUS_STRIP', '').strip() != ''
    parser.add_argument('-s', '--strip', default=default_arg,
                        help="strip whitespace at start and end",
                        action='store_true')

    default_arg = os.getenv('LANIUS_JUSTIFY', '').strip() != ''
    parser.add_argument('-j', '--justify', default=default_arg,
                        help="attempt to right-justify the text",
                        action='store_true')

    parser.add_argument('file', nargs='?', default=['-'],
                        help="path to markdown file",
                        metavar='PATH')

    args = parser.parse_args(argv)

    if args.theme not in THEME_LIST.keys():
        raise ValueError("Invalid theme '{0}'".format(args.theme))

    if args.style not in STYLE_MAP.keys():
        raise ValueError("Invalid style '{0}'".format(args.style))

    if args.format not in ['none', 'color', 'color256']:
        raise ValueError("Invalid format '{0}'".format(args.format))

    exts = [
        'markdown.extensions.smart_strong',
        'markdown.extensions.fenced_code',
        'markdown.extensions.sane_lists',
        'markdown.extensions.smarty',
    ]

    f = fileinput.input(files=args.file)
    stream = markdown.markdown(''.join(f), exts)
    f.close()

    if stream.strip() == '':
        return  # no input

    try:
        markup = lxml.html.fromstring(stream)
    except Exception:
        raise ValueError("Failed to parse input markdown")

    try:
        width = int(subprocess.check_output(['tput', 'cols']))
    except Exception:
        width = 80

    renderer = Renderer(THEME_LIST[args.theme],
                        args.style, args.format,
                        args.strip, args.justify,
                        width - 1)

    if sys.hexversion < 0x03000000:
        print(renderer.render(markup).encode('utf-8'))
    else:
        print(renderer.render(markup))


def main():
    run()
