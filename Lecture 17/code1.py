class Coordinate(object):
    """ 2D müstəvidə x və y qiymətlərindən ibarət koordinat klassı """
    
    def __init__(self, xval, yval):
        # İki məlumat atributu (instance variables) təyin edilir
        self.x = xval
        self.y = yval

# c obyekti yaradılır (x=3, y=4)
c = Coordinate(3, 4)

# origin obyekti yaradılır (x=0, y=0)
origin = Coordinate(0, 0)

# Məlumat atributlarına müraciət:
print(c.y)       # Ekrana 4 çıxır
print(origin.y)  # Ekrana 0 çıxır