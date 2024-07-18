#обращение к элементам определенных коллекций

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)
# print(s1.marks[2]) обращение через ссылку на объект print(s1[2])
    def __getitem__(self, item):
        if 0 <= item <len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("index out of range")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Index should be positive")
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            #расширить список значениями None до значения индекса
            self.marks.extend([None]*off)
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("place for your prime")
        del self.marks[key]

s1 = Student("Sergey", [5, 5, 3, 2, 5])
del s1[2]
s1[6] = -3
print(s1.marks)