## class StripChars:
import math
class Derivate:
    def __init__(self, func):
        self.__fn = func

        # self.__counter = 0
        # self.__chars = chars
    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return(self.__fn(x + dx) - self.__fn(x)) / dx

@Derivate
def df_sin(x):
    return math.sin(x)

df_sin = Derivate(df_sin)
print(df_sin(math.pi/3))

    # def __call__(self, *args, **kwargs):
        # if not isinstance(args[0], str):
        # self.__counter += step
        # return self.__counter
        #      raise TypeError("Arg should be a string")
        # return args[0].strip(self.__chars)

# s1 = StripChars(":!. ")
# s2 = StripChars(" ")
# res = s1(" Hello world!")
# res2 = s2(" Hello world!")
# print(res, res2, sep="\n")


# c = Counter()
# c2 = Counter()
# c()
# c(2)
# res = c(10)
# res2 = c2(-5)
# print(res, res2)