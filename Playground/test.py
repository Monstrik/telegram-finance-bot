# def myfunc(i: int):
#     print(str(i))
#
#
# myfunc("0")

# from typing import List, NamedTuple, Optional
#
#
# class User(NamedTuple):
#     """User structure"""
#     id: int
#     name: str
#
#
# class Point(NamedTuple):
#     x: int
#     y: int
#
#     def print(self):
#         print("X=" + str(self.x) + "  Y=" + self.y)
#
#
# u = User(id=1, name='sd')
#
# print(u.name)
# p = Point(23, 56)
#
# p.print()

l = [1, 3, 6, 7, 9, 2, 4, 8, 5]
rows = [f"a{e} = {e} Application " for e in l]

for e in rows:
    print(e)
