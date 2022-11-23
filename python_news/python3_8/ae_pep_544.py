# https://peps.python.org/pep-0544/
# static duck typing

from typing import Protocol

class SupportsClose(Protocol):
    def close(self) -> None: ...


class File:
    def close(self) -> None:
        print("close")


def close_resource(r: SupportsClose) -> None:
    r.close()


f = File()
close_resource(f)