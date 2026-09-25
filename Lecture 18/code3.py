class Coordinate(object):
    def __init__(self, x, y):
        # __init__ obyekt yarandığı an avtomatik işə düşür
        self.x = x
        self.y = y

    def distance(self, other):
        # İki nöqtə arasındakı məsafəni hesablayır
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def to_origin(self):
        # Obyektin koordinatlarını daxildən (0, 0) edir
        self.x = 0
        self.y = 0

    def __str__(self):
        # print(obyekt) çağırılanda necə görünəcəyini təyin edir
        return "<" + str(self.x) + "," + str(self.y) + ">"

c = Coordinate(3, 4)
origin = Coordinate(0, 0)

print(c.distance(origin))  # Məsafə: 5.0
c.to_origin()              # c nöqtəsi sıfırlandı
print(c)                   # Ekrana çıxır: <0,0>
