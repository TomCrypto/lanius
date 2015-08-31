from munch import munchify
from six import u

DefaultTheme = {
    'hr': munchify({
        'head': u('\u2015'),
        'rule': u('\u2015'),
        'last': u('\u2015'),
    }),
    'div': munchify({
        'margin': u(' '),
        'links': u('[{index}] \033[3;4m{href}\033[0m'),
    }),
    'blockquote': munchify({
        'margin': u('\033[33;1m\u2588\033[0m '),
    }),
    'plain': munchify({
        'render': lambda text: text,
    }),
    'strong': munchify({
        'render': lambda text: u('\033[1m{0}\033[0m').format(text),
    }),
    'em': munchify({
        'render': lambda text: u('\033[3m{0}\033[0m').format(text),
    }),
    'a': munchify({
        'render': lambda i, text: u('\033[3;4m{0}\033[0m [{1}]').format(i, text)
    }),
    'code': munchify({
        'inline': {
            'render': lambda text: u('\033[37;3m{0}\033[0m').format(text),
        },
        'block': {
            'highlight': True,
        },
    }),
    'h1': munchify({
        'fill': u('\u2584'),
    }),
    'h2': munchify({
        'prefix': u('\033[1m\u00A7\033[0m \033[4;3;1m'),
        'suffix': u('\033[0m'),
    }),
    'h3': munchify({
        'prefix': u('\033[1m\u00A7\033[0m \033[4;1m'),
        'suffix': u('\033[0m'),
    }),
    'h4': munchify({
        'prefix': u('\033[1m\u00A7\033[0m \033[1m'),
        'suffix': u('\033[0m'),
    }),
    'h5': munchify({
        'prefix': u('\033[1m\u00A7\033[0m \033[4m'),
        'suffix': u('\033[0m'),
    }),
    'h6': munchify({
        'prefix': u('\033[1m\u00A7\033[0m '),
        'suffix': u(''),
    }),
    'ol': munchify({
        'margin': {
            'head': lambda index: u('{0}. ').format(index),
            'tail': lambda length: u(' ') * length,
        },
    }),
    'ul': munchify({
        'margin': {
            'head': u('\u2022 '),
            'tail': lambda length: u(' ') * length,
        },
    }),
    'pre': munchify({
        'margin': u('\033[47;1m \033[0m '),
    }),
    'li': munchify({
        'margin': u(''),
    }),
    'p': munchify({
        'margin': u(''),
    }),
}

PlainTheme = {
    'hr': munchify({
        'head': u('-'),
        'rule': u('-'),
        'last': u('-'),
    }),
    'div': munchify({
        'margin': u(' '),
        'links': u('[{index}] {href}'),
    }),
    'blockquote': munchify({
        'margin': u('> '),
    }),
    'plain': munchify({
        'render': lambda text: text,
    }),
    'strong': munchify({
        'render': lambda text: u('**{0}**').format(text),
    }),
    'em': munchify({
        'render': lambda text: u('*{0}*').format(text),
    }),
    'a': munchify({
        'render': lambda idx, text: u('<{0}> [{1}]').format(idx, text),
    }),
    'code': munchify({
        'inline': {
            'render': lambda text: u('`{0}`').format(text),
        },
        'block': {
            'highlight': False,
        },
    }),
    'h1': munchify({
        'fill': u('='),
    }),
    'h2': munchify({
        'prefix': u('\u00A7 '),
        'suffix': u(''),
    }),
    'h3': munchify({
        'prefix': u('\u00A7 '),
        'suffix': u(''),
    }),
    'h4': munchify({
        'prefix': u('\u00A7 '),
        'suffix': u(''),
    }),
    'h5': munchify({
        'prefix': u('\u00A7 '),
        'suffix': u(''),
    }),
    'h6': munchify({
        'prefix': u('\u00A7 '),
        'suffix': u(''),
    }),
    'ol': munchify({
        'margin': {
            'head': lambda index: u('{0}. ').format(index),
            'tail': lambda length: u(' ') * length,
        },
    }),
    'ul': munchify({
        'margin': {
            'head': u('- '),
            'tail': lambda length: u(' ') * length,
        },
    }),
    'pre': munchify({
        'margin': u('  '),
    }),
    'li': munchify({
        'margin': u(''),
    }),
    'p': munchify({
        'margin': u(''),
    }),
}

THEME_LIST = {
    'default': DefaultTheme,
    'plain': PlainTheme,
}
