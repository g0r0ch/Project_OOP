

class Point:
    color = 'red'
    circule = 2

    def __init__(self, x=0, y=0):
        print("call init")
        self.x = x
        self.y = y

    def __del__(self):
        print("exemple deleting" + str(self))


    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt = Point()
print(pt.__dict__)


        # print("method called set_coords" + str(self))