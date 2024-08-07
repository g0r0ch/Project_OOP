class Point:

    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <+ self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("access denied")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key =='z':
            raise AttributeError("Prohibit atr name")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False
        # print("__getattr__:" + item)

    def __delattr__(self, item):
        print("__delattr__:" + item)
        object.__delattr__(self, item)



pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt1.yy)
del pt1.x
print(pt1.__dict__)
