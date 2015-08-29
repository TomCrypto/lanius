from lxml.etree import Element
from lanius.utils import *
from lanius import ansi


class Renderer:
    def __init__(self, theme, style, format, strip, justify, width):
        """Initializes the markdown renderer with params like theme."""
        self.width = width
        self.theme = theme
        self.style = style
        self.format = format
        self.strip = strip
        self.justify = justify

    def render(self, tree):
        """Renders a given HTML tree describing a markdown document."""
        self.links = []

        rendered = '\n'.join(self.call(tree, self.width))
        return rendered if self.strip else '\n' + rendered + '\n'

    def div(self, elem, theme, width):
        """Div block element, used only as root element in markdown."""
        block, indent = [], ansi.length(theme.margin)

        for child in self.children(elem, self.BLOCK):
            if child.tag not in ['ul', 'ol', 'br'] and len(block) != 0:
                block += ['']

            block += [line for line in self.call(child, width - indent)]

        if len(self.links) > 0:
            block += ['']

            for t, link in enumerate(self.links):
                block += [theme.links.format(index=t + 1, href=link)]

        return [theme.margin + line for line in block]

    def blockquote(self, elem, theme, width):
        """Blockquote, can contain everything (equivalent to div)."""
        block, indent = [], ansi.length(theme.margin)

        for child in self.children(elem, self.BLOCK):
            if child.tag not in ['ol', 'ul', 'br']:
                block += ['']

            block += [line for line in self.call(child, width - indent)]

        if len(block) > 0:
            del block[0]

        return [theme.margin + line for line in block]

    def ul(self, elem, theme, width):
        """Unordered list, has complex margins. Contains <li> only."""
        block, indent = [], ansi.length(theme.margin.head)

        for child in self.children(elem, {'li'}):
            block += [''] + add_margin(self.call(child, width - indent),
                                       theme.margin.head,
                                       theme.margin.tail(indent))

        return block

    def ol(self, elem, theme, width):
        """Ordered list, has complex margins. Contains <li> only."""
        block, children = [], self.children(elem, {'li'})

        margins = [theme.margin.head(t + 1) for t in range(len(children))]
        indent = maximum_of(margins, key=ansi.length)  # for long lists

        for t, child in enumerate(children):
            block += [''] + add_margin(self.call(child, width - indent),
                                       theme.margin.head(t + 1),
                                       theme.margin.tail(indent))

        return block

    def li(self, elem, theme, width):
        """List element; this element is a bit of a special case."""
        block, indent = [], ansi.length(theme.margin)

        for child in self.children(elem):
            if child.tag in self.BLOCK:
                if child.tag not in ['ol', 'ul', 'br']:
                    block += ['']

                block += [line for line in self.call(child, width - indent)]
            elif child.tag in self.INLINE:
                if len(block) > 0:
                    block[-1] += self.call(child)
                else:
                    block = [self.call(child)]

        if (len(block) > 0) and block[0].strip() == '':
            del block[0]

        text = [line.lstrip('\n') for line in block]
        wrapped = wrap_text(text, self.justify, width)
        return [theme.margin + line for line in wrapped]

    def p(self, elem, theme, width):
        """Paragraph, which can only contain other inline elements."""
        block, indent = [], ansi.length(theme.margin)

        for child in self.children(elem, self.INLINE | {'br'}):
            if child.tag == 'br':
                block += self.call(child, width)
            elif child.tag in self.INLINE:
                if len(block) > 0:
                    block[-1] += self.call(child)
                else:
                    block = [self.call(child)]

        text = [line.lstrip('\n') for line in block]
        wrapped = wrap_text(text, self.justify, width)
        return [theme.margin + line for line in wrapped]

    def pre(self, elem, theme, width):
        """Preformatted text, contains only one <code> for markdown."""
        block = []

        for child in self.children(elem, {'code'}):
            block += self.call(child, inline=False)

        return [theme.margin + line for line in block[:-1]]

    def hr(self, elem, theme, width):
        """Horizontal rule that should occupy all available width."""
        offset = ansi.length(theme.head) + ansi.length(theme.last)
        return [theme.head + theme.rule * (width - offset) + theme.last]

    def br(self, elem, theme, width):
        """Line break, this is actually an inline element in HTML."""
        return ['']

    def plain(self, elem, theme):
        """Artificial non-HTML element corresponding to plain text."""
        return theme.render(elem.text)

    def strong(self, elem, theme):
        """Strong inline element, commonly rendered using bold text."""
        return theme.render(self.inline(elem))

    def em(self, elem, theme):
        """Emphasis inline element, commonly rendered with italics."""
        return theme.render(self.inline(elem))

    def a(self, elem, theme):
        """Hyperlink (anchor), note links are tracked document-wide."""
        self.links.append(elem.attrib['href'])  # remember URL
        return theme.render(self.inline(elem), len(self.links))

    def code(self, elem, theme, inline=True):
        """Code element, can be either inline or block (inside pre)."""
        if inline:
            return theme.inline.render(elem.text)
        else:
            text = elem.text
            language = None

            if 'class' in elem.attrib:
                language = elem.attrib['class']

            if code_has_language(text):
                text, language = code_parse(text)

            style = self.style if theme.block.highlight else None

            return highlight_code(text, language, style,
                                  self.format).split('\n')

    def h1(self, elem, theme, width):
        """Header level 1, should be assumed to be a title header."""
        return [ansi.center(' ' + self.inline(elem) + ' ', width, theme.fill)]

    def h2(self, elem, theme, width):
        """Header level 2, is less prominent than header level 1."""
        return [theme.prefix + self.inline(elem) + theme.suffix]

    def h3(self, elem, theme, width):
        """Header level 3, is less prominent than header level 2."""
        return [theme.prefix + self.inline(elem) + theme.suffix]

    def h4(self, elem, theme, width):
        """Header level 4, is less prominent than header level 3."""
        return [theme.prefix + self.inline(elem) + theme.suffix]

    def h5(self, elem, theme, width):
        """Header level 5, is less prominent than header level 4."""
        return [theme.prefix + self.inline(elem) + theme.suffix]

    def h6(self, elem, theme, width):
        """Header level 6, is less prominent than header level 5."""
        return [theme.prefix + self.inline(elem) + theme.suffix]

    BLOCK = {
        'hr', 'blockquote', 'ol', 'ul', 'pre', 'div',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'br', 'li',
    }

    INLINE = {
        'strong', 'em', 'a', 'code', 'plain'
    }

    @staticmethod
    def children(elem, valid=BLOCK | INLINE):
        if (elem.text is not None) and (elem.text.strip() != ''):
            children = [Element('plain')]
            children[-1].text = elem.text
        else:
            children = []

        for child in elem:
            children += [child]

            if (child.tail is not None) and (child.tail.strip() != ''):
                children += [Element('plain')]
                children[-1].text = child.tail

        return [child for child in children if child.tag in valid]

    def inline(self, elem):
        text = ''

        for child in self.children(elem, self.INLINE | {'br'}):
            text += self.call(child)

        return text

    def call(self, elem, *args, **kwargs):
        theme = self.theme[elem.tag] if elem.tag in self.theme else None
        return getattr(self, elem.tag)(elem, theme, *args, **kwargs)
