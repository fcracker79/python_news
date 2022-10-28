# PEP 585 – Type Hinting Generics In Standard Collections


def f_tuple(x: tuple[int, int]):
    ...


def f_list(x: list[int]):
    ...


def f_dict(x: dict[int, int]):
    ...


def f_set(x: set[int]):
    ...


def f_frozenset(x: frozenset[int]):
    ...


class Foo:
    ...


def f_type(x: type[Foo]):
    ...


if __name__ == '__main__':
    f_tuple((1, 1))  # OK
    f_tuple(('a', 'b'))  # warning from IDE
    f_tuple((1, 'b'))  # warning from IDE

    f_list([1, 1])  # OK
    f_list(['a', 'b'])  # warning from IDE
    f_list([1, 'b'])  # OK (?!?)

    f_dict({1: 1})  # OK
    f_dict({'a': 'b'})  # warning from IDE
    f_dict({1: 'b'})  # warning from IDE

    f_set({1, 1})  # OK
    f_set({'a', 'b'})  # warning from IDE
    f_set({1, 'b'})  # OK (?!?)

    f_frozenset(frozenset({1, 1}))  # OK
    f_frozenset(frozenset({'a', 'b'}))  # warning from IDE
    f_frozenset(frozenset({1, 'b'}))  # OK (?!?)
