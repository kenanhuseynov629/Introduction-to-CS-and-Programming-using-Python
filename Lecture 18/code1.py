class Coordinate(object):
    """X və Y qiymətlərindən ibarət koordinat obyektini təmsil edir."""
    
    def __init__(self, x, y):
        """x və y atributlarını mənimsədir."""
        self.x = x
        self.y = y

    def distance(self, other):
        """İki Coordinate obyekti arasındakı Evklid məsafəsini hesablayır."""
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def to_origin(self):
        """Obyektin x və y koordinatlarını sıfıra (0, 0) bərabər edir."""
        self.x = 0
        self.y = 0

    def __str__(self):
        """Koordinatın oxunabilən sətir (string) təsvirini qaytarır."""
        return "<" + str(self.x) + "," + str(self.y) + ">"

c = Coordinate(3, 4)
origin = Coordinate(0, 0)

print(f"c-nin x-i {c.x}, origin-in x-i isə {origin.x}")
print("Məsafə:", c.distance(origin))

# to_origin metodunu çağırmaq
c.to_origin()
print("Sıfırlandıqdan sonra c-nin koordinatları:", c.x, c.y)
print("Print(c):", c)