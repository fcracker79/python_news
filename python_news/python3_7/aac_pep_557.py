import dataclasses


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


if __name__ == '__main__':
    p = Point(1.5, 2.5)
    print(p)  # "Point(x=1.5, y=2.5, z=0.0)"
    try:
        {p}
    except TypeError as e:
        assert e.args[0] == 'unhashable type: \'Point\''
    {FrozenPoint}
