from string import ascii_letters


class Person:
    S_RUS = "абвгдеёжзийклмнопрстуфхцщьъэюя-"  # sample is in HW CLI on GIT
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        # self.verify_weight(weight)
        # self.verify_old(old)
        # self.verify_ps(ps)


        self.fio = fio.split()
        self.old = old
        self.passport = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("fio should be a str")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Unproper fio format")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("fio should have even a symbol")
            if len(s.strip(letters)) != 0:
                raise TypeError("only letters or - should be used")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 and old > 120:
            raise TypeError("Age should be int between [14; 120]")

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Weight should be more then 20")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("pass should be string")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("passport num not valid")

        @property
        def fio(self):
            return self.__fio

        @property
        def old(self):
            return self.old

        @old.setter
        def old(self, old):
            self.verify_old(old)
            self.__old = old

        @property
        def weight(self):
            return self.weight

        @weight.setter
        def old(self, weight):
            self.verify_weight(weight)
            self.__weight = weight

        @property
        def passport(self):
            return self.__passport

        @passport.setter
        def old(self, ps):
            self.verify_ps(ps)
            self.__passport = ps

p = Person("Svistoplias Ivan Semenovich", 15, "1200 456780", 21.2)
p.old = 200
p.passport = '4567 123456'
p.weight = 70.0
print(p.__dict__)

