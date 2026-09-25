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


class Circle(object):
    """Mərkəzi Coordinate obyekti, radiusu int olan Dairə klassı."""
    
    def __init__(self, center, radius):
        # Tip yoxlanışı: center Coordinate, radius int olmalıdır
        if type(center) == Coordinate and type(radius) == int:
            self.center = center
            self.radius = radius
        else:
            raise ValueError("center Coordinate obyekti, radius isə int olmalıdır!")

    def is_inside(self, point):
        """Verilmiş point (Coordinate obyekti) dairənin daxilindədirsə True qaytarır."""
        return point.distance(self.center) < self.radius

    def __str__(self):
        """Dairə obyektinin sətir təsviri."""
        return "circle: " + str(self.center) + ", " + str(self.radius)

center = Coordinate(2, 2)
my_circle = Circle(center, 5)

p1 = Coordinate(3, 3)
p2 = Coordinate(10, 10)

print(my_circle.is_inside(p1))  # True
print(my_circle.is_inside(p2))  # False
print(my_circle)                # circle: <2,2>, 5