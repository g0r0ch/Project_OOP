class Geom:
    name = 'geom'

# overriding переопределение
    # def draw(self):
    #     print("line paint")
    # def __init__(self):
    #     print("Geom initialise")

    def __init__(self, x1, y1, x2, y2):
        print(f"Geom initialise for {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

# base class extension расширение функциональности базового класса
class Line(Geom):
    # def __init__(self, x1, y1, x2, y2):
        # print("Line initialise")
        # self.x1 = x1
        # self.y1 = y1
        # self.x2 = x2
        # self.y2 = y2

    def draw(self):
        print("line paint")

class Rect(Geom):

    def __init__(self, x1, y1, x2, y2, fill=None):
        # Geom.__init__(self, x1, y1, x2, y2) # incorrect
        # print("Rect initialise")
        super().__init__(x1, y1, x2, y2) # correct ссылка на объект посредник first order call!!! делегирование
        # self.x1 = x1
        # self.y1 = y1
        # self.x2 = x2
        # self.y2 = y2
        self.fill = fill

    def draw(self):
        print("Rect paint")

# l = Line() __call__ __new__ __init__
l = Line(0, 0, 10, 20)
r = Rect(1, 2 , 3, 4)
# print(l.__dict__)
print(r.__dict__)