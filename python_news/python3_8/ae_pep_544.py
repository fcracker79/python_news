# https://peps.python.org/pep-0544/
# static duck typing

from typing import Protocol, TypeVar, runtime_checkable
from abc import abstractmethod

class SupportsClose(Protocol):
    def close(self) -> None: ...


class File:
    def close(self) -> None:
        print("close")


def close_resource(r: SupportsClose) -> None:
    r.close()


f = File()
close_resource(f)


# A better example that fits the idea of duck typing

T = TypeVar('T')

class Repeatable(Protocol):
    def __mul__(self: T, repeat_count: int) -> T: ...

RT = TypeVar("RT", bound=Repeatable)

def double(x: RT) -> RT:
    return x * 2


# @runtime_checkable decorator mark a protocol class as runtime protocol

@runtime_checkable
class SupportsComplex(Protocol):
    @abstractmethod
    def __complex__(self) -> complex: ...


# you can then check at runtime isinstance(z, SupportsComplex)