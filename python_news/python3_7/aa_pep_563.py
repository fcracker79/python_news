# PEP 563: Postponed Evaluation of Annotations

# This line is to enable the feature
from __future__ import annotations


class C:
    @classmethod
    def from_string(cls, source: str) -> C:
        ...

    def validate_b(self, obj: B) -> bool:
        ...


class B:
    ...
