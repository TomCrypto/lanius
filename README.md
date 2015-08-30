# **Lanius Markdown Viewer**

Simple markdown viewer for the terminal. A work in progress.

Requirements: 

 - markdown
 - pygments
 - munch
 - lxml

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

Possibly supported in the future:

 1. tables (using the `tabulate` module?)
 2. footnotes

Will not be supported:

 1. general embedded HTML
 2. images

Possible uses for this tool:

 - building block for terminal-based markdown renderers
 - manpage replacement for custom documentation tools
 - something to add to your linux environment
