class Fraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        # Məxrəc 1-dirse yalnız surəti, əks halda num/denom göstərir
        if self.denom == 1:
            return str(self.num)
        return str(self.num) + "/" + str(self.denom)

    def __mul__(self, other):
        # İki kəsrin vurulması və YENİ Fraction obyekti qaytarılması
        top = self.num * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)

    def __add__(self, other):
        # İki kəsrin toplanması və YENİ Fraction obyekti qaytarılması
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)

    def __float__(self):
        # Kəsri float (onluq kəsr) tipinə çevirir
        return self.num / self.denom

    def reduce(self):
        # Kəsri ƏBOB (GCD) vasitəsilə ixtisar edir
        def gcd(n, d):
            while d != 0:
                (d, n) = (n % d, d)
            return n

        if self.denom == 0:
            return None
        elif self.denom == 1:
            # Məxrəc 1 olduqda belə int yox, Fraction obyekti qaytarırıq!
            return Fraction(self.num, 1)
        else:
            greatest_common_divisor = gcd(self.num, self.denom)
            top = int(self.num / greatest_common_divisor)
            bottom = int(self.denom / greatest_common_divisor)
            return Fraction(top, bottom)

kəsr1 = Fraction(1, 4)
kəsr2 = Fraction(3, 4)

# * operatoru avtomatik __mul__ metodunu çağırır
cavab = kəsr1 * kəsr2
print("Hasil:", cavab)         # Ekrana çıxır: 3/16
print("Float:", float(cavab))  # Ekrana çıxır: 0.1875

# Kəsrin ixtisar olunması
kəsr3 = Fraction(2, 12)
ixtisar_olunmuş = kəsr3.reduce()
print("İxtisar:", ixtisar_olunmuş)  # Ekrana çıxır: 1/6