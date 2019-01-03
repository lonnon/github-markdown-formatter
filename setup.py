from setuptools import setup

setup(
    name='github-markdown-formatter',
    description='Convert GitHub-flavored Markdown into GitHub-styled HTML',
    url='https://github.com/lonnon/github-markdown-formatter',
    version='1.0.0',
    author='Lonnon Foster',
    author_email='lonnon.foster@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=['mistune', 'pygments'],
    py_modules=['github_markdown_formatter'],
    entry_points={'console_scripts': [
        'github-markdown-format=github_markdown_formatter:main',
    ]},
)
