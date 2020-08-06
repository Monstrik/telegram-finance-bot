# def myfunc(i: int):
#     print(str(i))
#
#
# myfunc("0")

from typing import List, NamedTuple, Optional


class User(NamedTuple):
    """User structure"""
    id: int
    name: str


class Point(NamedTuple):
    x: int
    y: int

    def print(self):
        print("X=" + str(self.x) + "  Y=" + self.y)


u = User(id=1, name='sd')

print(u.name)
p = Point(23, 56)

p.print()
