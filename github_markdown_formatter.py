# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import argparse
import os

import mistune
import pygments.formatters
import pygments.lexers
import pygments.util


class CodeRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        try:
            lexer = pygments.lexers.get_lexer_by_name(lang, stripnl=False)
            cssclass = 'highlight {}'.format(lang)
        except pygments.util.ClassNotFound:
            lexer = pygments.lexers.get_lexer_by_name('text', stripnl=False)
            cssclass = 'highlight'
        formatter = pygments.formatters.HtmlFormatter(cssclass=cssclass)
        return pygments.highlight(code, lexer=lexer, formatter=formatter)


def highlight(doc, Renderer=CodeRenderer):
    return mistune.Markdown(Renderer(escape=True, hard_wrap=False))(doc)


def inline_styles(path):
    styles = []
    with os.scandir(path) as iterator:
        for entry in iterator:
            if entry.is_file() and entry.name.endswith('.css'):
                with open(entry.path, 'r', encoding='utf-8') as stylesheet:
                    styles.append(stylesheet.read())
    return ''.join(styles)


def main(argv=None):
    try:
        default_csspath = os.path.dirname(os.path.realpath(__file__))
    except NameError:
        default_csspath = os.path.dirname(os.path.realpath('.'))

    parser = argparse.ArgumentParser(
        description="Convert markdown to HTML with GitHub styling."
    )
    parser.add_argument(
        'filename',
        default='/dev/stdin',
        help="Markdown file to convert",
    )
    parser.add_argument(
        '-o', '--output',
        help="Path to output file (default: stdout)",
    )
    parser.add_argument(
        '-c', '--csspath',
        default=default_csspath,
        help="Path to CSS files (default: %(prog)s path",
    )
    args = parser.parse_args(argv)

    with open(args.filename, 'r', encoding='utf-8') as f:
        hl = highlight(f.read())
        html = (
            '<!doctype html>'
            '<html lang="en">'
            '<head><meta charset="utf-8">'
            '<title>Markdown Preview</title>'
            '<style>{style_markup}</style>'
            '</head><body>'
            '<div class="container" style="margin-top: 20px; margin-bottom: 20px;">'
            '<div class="Box Box--condensed">'
            '<div class="Box-body p-6">'
            '<article class="markdown-body entry-content">'
            '{body_markup}'
            '</div></div></div></article></body></html>'
        )
        output = html.format(
            style_markup=inline_styles(args.csspath),
            body_markup=hl,
        )
        if args.output is None:
            print(output)
        else:
            with open(args.output, 'w', encoding='utf-8') as o:
                o.write(output)


if __name__ == '__main__':
    main()
