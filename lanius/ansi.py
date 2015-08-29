import re


def find_escapes(s):
    return ['\033[' + x + 'm' for x in re.findall(r'\033\[(.*?)m', s)]


def extract_escapes(s):
    return ''.join(find_escapes(s))


def center(s, width, fill=''):
    lpad = fill * (width // 2 - length(s) // 2)  # standard centering
    rpad = fill * (width - width // 2 + length(s) // 2 - length(s))

    return lpad + s + rpad


def strip_escapes(s):
    s2 = ''

    strip = False

    for t in range(len(s)):
        if strip:
            if s[t] == 'm':
                strip = False
            continue

        if s[t] == '\033':
            strip = True
        else:
            s2 += s[t]

    return s2


def length(s):
    return len(s) - len(extract_escapes(s))
