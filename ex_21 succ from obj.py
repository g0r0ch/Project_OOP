# class Geom:
#     pass
#
# class Line(Geom):
#     pass

class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


v = Vector([1, 2, 3])
print(v)

# g = Geom()
# l = Line()
# work with class objects
# print(isinstance(l, object))
# issubclass work with classes
# print(issubclass(Line, Geom))
# print(issubclass(int, object))
# print(l.__class__)
# print(g)
# print(Geom.__name__)