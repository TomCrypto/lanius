from lanius import ansi
from lanius import wrap

from pygments import formatters
from pygments import highlight
from pygments import lexers
import re


# TODO: experimental!
def just(line, width):
    words = line.split(' ')
    done = {t: t == len(words) - 1 for t in range(len(words))}

    if width - ansi.length(line) > 14:
        return line

    while ansi.length(' '.join(words)) < width:
        best = -1

        for t, word in enumerate(words):
            if not done[t]:
                if (best == -1) or (len(words[t]) < len(words[best])):
                    best = t

        if best == -1:
            done = {t: t == len(words) - 1 for t in range(len(words))}
        else:
            words[best] += ' '
            done[best] = True

    return ' '.join(words)


def fix_straddling_escapes(block):
    for t in range(len(block) - 1):
        block[t + 1] = ansi.extract_escapes(block[t]) + block[t + 1]
        block[t] += '\033[0m'  # handles escapes straddling newlines

    return block


def wrap_text(block, justify, width):
    wrapped = []

    for line in block:
        if line.strip() != '':
            prefix = re.match(r"\s*", line).group(0)
            output = wrap.wrap(line, target=width, measure=ansi.length)

            output = fix_straddling_escapes(output)

            if justify:
                output = [just(prefix + line, width) for line in output]
            else:
                output = [prefix + line for line in output]

            wrapped += output
        else:
            wrapped.append('')

    return wrapped


def code_has_language(code):
    return re.match('^@lang:(.*?)\n(.*)', code, flags=re.DOTALL) is not None


def code_parse(code):
    m = re.match('^@lang:(.*?)\n(.*)', code, flags=re.DOTALL)
    return m.group(2), m.group(1)


def highlight_code(code, language, style, format):
    block = code.split('\n')

    if language is not None:
        lexer = lexers.get_lexer_by_name(language)
    else:
        try:
            lexer = lexers.guess_lexer('\n'.join(block))
        except Exception:
            lexer = lexers.special.TextLexer()

    if style is None or format == 'none':
        f = formatters.NullFormatter()
    elif format == 'color':
        f = formatters.TerminalFormatter(style=style)
    elif format == 'color256':
        f = formatters.Terminal256Formatter(style=style)

    return highlight('\n'.join(block), lexer, f)


def add_margin(block, head, tail=None):
    processed = []

    if tail is None:
        tail = head

    for t, line in enumerate(block):
        processed += [(head if t == 0 else tail) + line]

    return processed


def maximum_of(lst, key):
    return key(lst[max(enumerate(lst), key=lambda t: key(t[1]))[0]])
