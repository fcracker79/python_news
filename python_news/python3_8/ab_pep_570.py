# PEP 570 – Python Positional-Only Parameters


def f(a, b, /, c, d=None):
    pass


def g(a, b, c=None, /):
    pass


if __name__ == '__main__':
    f(1, 2, c=3, d=4)
    f(1, 2, 3, d=4)
    f(1, 2, 3)
    # NOT legal
    # f(1, b=2, c=3)
    # f(a=1, b=2, c=3)

    g(1, 2)
    g(1, 2, 3)
    # NOT legal
    # g(1, 2, c=3)
