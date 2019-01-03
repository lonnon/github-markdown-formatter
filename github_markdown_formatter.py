# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import argparse
import io
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


def inline_styles(filenames):
    path = os.path.dirname(os.path.realpath(__file__))
    styles = []
    for filename in filenames:
        style_path = os.path.join(path, filename)
        with io.open(style_path) as stylesheet:
            styles.append(stylesheet.read())
    return ''.join(styles)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', default='/dev/stdin')
    args = parser.parse_args(argv)

    with io.open(args.filename) as f:
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
        print(html.format(
            style_markup=inline_styles(['frameworks.css', 'github.css']),
            body_markup=hl,
        ).encode('utf-8'))


if __name__ == '__main__':
    exit(main())
