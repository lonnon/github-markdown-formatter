github-markdown-formatter
=========================

Convert GitHub-flavored Markdown into GitHub-styled HTML.

Based on [asottile/markdown-code-blocks][asottile/markdown-code-blocks],
it combines the speed of [mistune][mistune] with the power of
[pygments][pygments] to generate HTML, then tacks on GitHub CSS to give
a close approximation of how a Markdown file appears on GitHub.


## Usage

The library provides a single function `highlight` which takes in a
Markdown string and returns HTML. GitHub styles are added inline to the
`<head>` of the generated markup. Output is to stdout.

```sh
python github-markdown-formatter.py README.md > README.html
```


[mistune]: https://github.com/lepture/mistune
[pygments]: http://pygments.org/
[asottile/markdown-code-blocks]: https://github.com/asottile/markdown-code-blocks
