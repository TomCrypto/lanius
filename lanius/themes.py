from munch import munchify

DefaultTheme = {
    'hr': munchify({
        'head': u'─',
        'rule': u'─',
        'last': u'─',
    }),
    'div': munchify({
        'margin': ' ',
        'links': '[{index}] \033[3;4m{href}\033[0m',
    }),
    'blockquote': munchify({
        'margin': '\033[33;1m█\033[0m ',
    }),
    'plain': munchify({
        'render': lambda text: text,
    }),
    'strong': munchify({
        'render': lambda text: '\033[1m{0}\033[0m'.format(text),
    }),
    'em': munchify({
        'render': lambda text: '\033[3m{0}\033[0m'.format(text),
    }),
    'a': munchify({
        'render': lambda i, text: '\033[3;4m{0}\033[0m [{1}]'.format(i, text)
    }),
    'code': munchify({
        'inline': {
            'render': lambda text: '\033[37;3m{0}\033[0m'.format(text),
        },
        'block': {
            'highlight': True,
        },
    }),
    'h1': munchify({
        'fill': u'▄',
    }),
    'h2': munchify({
        'prefix': u'\033[1m§\033[0m \033[4;3;1m',
        'suffix': u'\033[0m',
    }),
    'h3': munchify({
        'prefix': u'\033[1m§\033[0m \033[4;1m',
        'suffix': u'\033[0m',
    }),
    'h4': munchify({
        'prefix': u'\033[1m§\033[0m \033[1m',
        'suffix': u'\033[0m',
    }),
    'h5': munchify({
        'prefix': u'\033[1m§\033[0m \033[4m',
        'suffix': u'\033[0m',
    }),
    'h6': munchify({
        'prefix': u'\033[1m§\033[0m ',
        'suffix': '',
    }),
    'ol': munchify({
        'margin': {
            'head': lambda index: '{0}. '.format(index),
            'tail': lambda length: ' ' * length,
        },
    }),
    'ul': munchify({
        'margin': {
            'head': u'• ',
            'tail': lambda length: ' ' * length,
        },
    }),
    'pre': munchify({
        'margin': '\033[47;1m \033[0m ',
    }),
    'li': munchify({
        'margin': '',
    }),
    'p': munchify({
        'margin': '',
    }),
}

PlainTheme = {
    'hr': munchify({
        'head': '-',
        'rule': '-',
        'last': '-',
    }),
    'div': munchify({
        'margin': ' ',
        'links': '[{index}] {href}',
    }),
    'blockquote': munchify({
        'margin': '> ',
    }),
    'plain': munchify({
        'render': lambda text: text,
    }),
    'strong': munchify({
        'render': lambda text: '**{0}**'.format(text),
    }),
    'em': munchify({
        'render': lambda text: '*{0}*'.format(text),
    }),
    'a': munchify({
        'render': lambda idx, text: '<{0}> [{1}]'.format(idx, text),
    }),
    'code': munchify({
        'inline': {
            'render': lambda text: '`{0}`'.format(text),
        },
        'block': {
            'highlight': False,
        },
    }),
    'h1': munchify({
        'fill': '=',
    }),
    'h2': munchify({
        'prefix': '§ ',
        'suffix': '',
    }),
    'h3': munchify({
        'prefix': '§ ',
        'suffix': '',
    }),
    'h4': munchify({
        'prefix': '§ ',
        'suffix': '',
    }),
    'h5': munchify({
        'prefix': '§ ',
        'suffix': '',
    }),
    'h6': munchify({
        'prefix': '§ ',
        'suffix': '',
    }),
    'ol': munchify({
        'margin': {
            'head': lambda index: '{0}. '.format(index),
            'tail': lambda length: ' ' * length,
        },
    }),
    'ul': munchify({
        'margin': {
            'head': '- ',
            'tail': lambda length: ' ' * length,
        },
    }),
    'pre': munchify({
        'margin': '  ',
    }),
    'li': munchify({
        'margin': '',
    }),
    'p': munchify({
        'margin': '',
    }),
}

THEME_LIST = {
    'default': DefaultTheme,
    'plain': PlainTheme,
}
