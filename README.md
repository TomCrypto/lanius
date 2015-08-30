# **Lanius Markdown Viewer**

A simple and elegant Markdown viewer for the terminal. This command-line tool
takes in Markdown text in a file or on standard input and pretty-prints it on
standard output, using the capabilities of modern terminal emulators.

## Requirements

This tool supports only terminals capable of standard ANSI escape codes -- such
as all modern UNIX terminal emulators -- and depends on some Python libraries:

 - The `markdown` (python-markdown) module, used to parse the input into an HTML document;

 - The `lxml` module, which converts the HTML document into a tree prior to rendering;

 - The `pygments` module, which is used to provide syntax highlighting for code blocks.
Lanius uses the `TerminalFormatter` or the `Terminal256Formatter` according to user preference;

 - The `munch` module, for accessing theme properties in the renderer more conveniently (e.g.
`theme.margin` rather than `theme['margin']`).

## Features

Lanius supports all of basic Markdown with the obvious exception of images. It also
supports the usual extensions expected of Markdown viewers. *However*, due to the
fact that Python-Markdown currently does not support nested fenced code blocks, the
first line of a code block may be `@lang:language-name`, which will be understood by
Lanius as a language hint.

This feature will be removed once Python-Markdown is able to handle nested fenced
code blocks, as it is incompatible with other Markdown viewers.

The following features are currently **not** supported but may one day be:

 - tables
 - footnotes

The following features are not and never will be supported by Lanius:

 - general embedded HTML (a subset of embedded HTML might work)
 - images


Note that any HTML elements not recognized by Lanius (such as `<img>`) will be silently
discarded, however Lanius may break on Markdown containing embedded HTML that would not
normally be generated by Python-Markdown (such as an anchor with no `href` attribute). It
also may be that unrecognized elements are inside recognized elements (such as `<img>`
inside `<p>`) which causes spurious whitespace, so, like, don't do it. It might make more
sense to put a placeholder instead of discarding them though.

This tool is a work in progress.

---

# Other stuff

You might need the following for `lxml`:

    sudo apt-get install libxml2
    sudo apt-get install libxslt1.1
    sudo apt-get install libxml2-dev
    sudo apt-get install libxslt1-dev
    sudo apt-get install python-libxml2
    sudo apt-get install python-libxslt1
    sudo apt-get install python-dev
    sudo apt-get install zlib1g-dev  # for debian at least

### TODO

 -   improve `ansi.py` with maybe actual escape codes
 -   clean up functions in utils.py
 -   work out a better justification algorithm
 -   more themes, improve default theme
 -   finish this readme

Possible uses for this tool:

 - building block for terminal-based markdown renderers
 - manpage replacement for custom documentation tools
 - something to add to your linux environment
