# PEP 557: Data classes

import dataclasses
import typing


@dataclasses.dataclass(
    init=True,
    repr=True,
    eq=True,
    order=False,
    # If eq and frozen are both true, Data Classes will generate
    # a __hash__ method for you.
    # If eq is true and frozen is false, __hash__ will be set to None,
    # marking it unhashable (which it is).
    # If eq is false, __hash__ will be left untouched meaning the __hash__ method
    # of the superclass will be used
    # (if the superclass is object, this means it will fall back to id-based hashing).
    unsafe_hash=False,
    frozen=False
)
class Point:
    x: float
    y: float
    z: float = 0.0


@dataclasses.dataclass(frozen=True)
class FrozenPoint:
    x: float
    y: float
    z: float = 0.0


@dataclasses.dataclass(frozen=True)
class ClassWithFields:
    x: typing.List[str] = dataclasses.field(default_factory=list)
    y: set = frozenset()


@dataclasses.dataclass(frozen=True)
class TestPostInit:
    x: typing.List[str]
    y: typing.Dict[str, int] = None

    def __post_init__(self):
        object.__setattr__(self, 'y', {s: i for i, s in enumerate(self.x)})
        # Cannot set on frozen instances
        # self.y = {s: i for i, s in enumerate(self.x)}


if __name__ == '__main__':
    p = Point(1.5, 2.5)
    print(p)  # "Point(x=1.5, y=2.5, z=0.0)"
    try:
        {p}
    except TypeError as e:
        assert e.args[0] == 'unhashable type: \'Point\''
    {FrozenPoint}
    cf1 = ClassWithFields()
    cf2 = ClassWithFields()
    assert cf1.x is not cf2.x
    assert cf1.y is cf2.y
    t = TestPostInit(x=['a', 'b'])
    assert 0 == t.y['a']
    assert 1 == t.y['b']
