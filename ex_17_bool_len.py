# способ настройки определения правдивости классов True for each class object
class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y
#  приоритет! only bool true or false
    def __bool__(self):
        print("__bool__")
        return self.x == self.y

p = Point(0, 0)
# print(bool(p))
# dunder bool неявно отрабатывает в условных операторах
if p:
    print("obj p is True")
else:
    print("obj p is False")
