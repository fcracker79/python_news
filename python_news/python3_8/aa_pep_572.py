# PEP 572: Assignment Expressions
import re

if __name__ == '__main__':
    pattern = re.compile('([0-9]+)([a-z]+)')
    if match := pattern.match('123abc'):
        print(f'Groups: {match.groups()}')  # Groups: ('123', 'abc')
