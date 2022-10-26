import functools
import random
import sys


class Foo:
    @functools.cached_property
    def prop(self):
        return random.randint(0, sys.maxsize)


@functools.singledispatch
def single_dispatch(value):
    print('base single dispatch')


@single_dispatch.register(list)
def _(l: list):
    print('single_distpatch with list')


class SuperClass:
    pass


class SubClass(SuperClass):
    pass


class SubSubClass(SubClass):
    pass


class SubSubSubClass(SubSubClass, str):
    pass


class SubSubSubClassStrFirst(str, SubSubClass):
    pass


class SingleDispatchClass:
    @functools.singledispatchmethod
    def single_dispatch(self, value):
        print('base single dispatch (class)')

    @single_dispatch.register(list)
    def _(self, l: list):
        print('single_distpatch with list (class)')

    @single_dispatch.register(str)
    def _(self, l: str):
        print('single_distpatch with str (class)')

    @single_dispatch.register(SuperClass)
    def _(self, l: SuperClass):
        print('single_distpatch with SuperClass (class)')

    @single_dispatch.register(SubClass)
    def _(self, l: SubClass):
        print('single_distpatch with SubClass (class)')


if __name__ == '__main__':
    f = Foo()
    print('Before:', f.__dict__)
    p = f.prop
    for _ in range(1000):
        assert p == f.prop
    print('After:', f.__dict__)  # After: {'prop': <a random number>}
    del f.__dict__['prop']
    assert p != f.prop
    single_dispatch(12)  # base single dispatch
    single_dispatch([1, 2, 3])  # single_distpatch with list
    s = SingleDispatchClass()
    s.single_dispatch(12)  # base single dispatch (class)
    s.single_dispatch([1, 2, 3])  # single_distpatch with list (class)
    s.single_dispatch('abc')  # single_distpatch with str (class)
    s.single_dispatch(SuperClass())  # single_distpatch with SuperClass (class)
    s.single_dispatch(SubClass())  # single_distpatch with SubClass (class)
    s.single_dispatch(SubSubClass())  # single_distpatch with SubClass (class)
    s.single_dispatch(SubSubSubClass())  # single_distpatch with SubClass (class)
    s.single_dispatch(SubSubSubClassStrFirst())  # single_distpatch with str (class)
