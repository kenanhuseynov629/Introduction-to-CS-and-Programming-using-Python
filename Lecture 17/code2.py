class Coordinate(object):
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval

    def getX(self):
        """ self obyektinin x oxundakı məsafəsini qaytarır """
        return self.x

    def getY(self):
        """ self obyektinin y oxundakı məsafəsini qaytarır """
        return self.y

    def distance(self, other):
        """ self və other koordinat obyektləri arasındakı Evklid məsafəsini hesblayır """
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

c = Coordinate(3, 4)
origin = Coordinate(0, 0)

# 1. Standart / Pythonic Yol (Shorthand):
d1 = c.distance(origin)
print(d1)  # Ekrana 5.0 çıxır

# 2. Açıq / Ekvalent Yol (Explicit Class Call):
d2 = Coordinate.distance(c, origin)
print(d2)  # Ekrana 5.0 çıxır