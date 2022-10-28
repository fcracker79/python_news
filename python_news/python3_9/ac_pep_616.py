# PEP 616 – String methods to remove prefixes and


if __name__ == '__main__':
    s = 'ABC Hello World XYZ'
    print(s.removeprefix('ABC'))  # Hello World XYZ
    print(s.removesuffix('XYZ'))  # ABC Hello World
    print(s.removeprefix('foo'))  # ABC Hello World XYZ
    print(s.removesuffix('foo'))  # ABC Hello World XYZ
