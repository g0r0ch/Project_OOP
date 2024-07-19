#base class -- relative ancestor

class Geom:
    name = 'geom'
#важно! через какой объект(l = Line(), r = Rect()) вызван методs(et_coords) класса
    def set_coords(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        # self.draw() # внутри метода следует вызывать методы определённые в базовом классе, НЕ в наследниках!!

#subclass -- succestor
class Line(Geom):
    name = 'line' # ватрушка со стрелкой  = переопределение (вверх = базовый класс, вниз = дочерний) .py
    def draw(self):
        print("line paint")

    # def set_coords(self, x1, x2, y1, y2):
    #     self.x1 = x1
    #     self.x2 = x2
    #     self.y1 = y1
    #     self.y2 = y2


class Rect(Geom):
    def draw(self):
        print("rectangle paint")

    # def set_coords(self, x1, x2, y1, y2):
    #     self.x1 = x1
    #     self.x2 = x2
    #     self.y1 = y1
    #     self.y2 = y2



# g = Geom()
# g.set_coords(0, 0, 0 ,0)
l = Line()
r = Rect()
l.set_coords(1, 1, 2 ,2)
r.set_coords(1, 1, 2 ,2)

## локальные свойства объекта класса
print(l.__dict__)
print(r.__dict__)
print(l.name)
print(r.name)
#print(g.name)
#print(g.draw())
#l.draw()
# print(l.name)