# https://peps.python.org/pep-0673/

from typing import Self

class Shape:
    def set_scale(self, scale: float) -> Self:
        self.scale = scale
        return self

class Circle(Shape):
    def set_radius(self, radius: float) -> Self:
        self.radius = radius
        return self

Circle().set_scale(.5).set_radius(.5)
# this way set_scale returns Self instead of Shape so set_scale().set_radius()
# is not marked as error since Shape has not method set_radius().

# Also without Self you need from __future__ import annotations to do
class Sample:
    @classmethod
    def create(cls: Type[Sample]) -> Sample: ...