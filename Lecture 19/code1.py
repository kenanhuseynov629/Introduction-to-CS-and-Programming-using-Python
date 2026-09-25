class Animal(object):
    """Bütün heyvanlar üçün baza klassı."""

    def __init__(self, age):
        """Obyekt yarandıqda yaş mənimsədilir, ad isə ilkin olaraq None (yoxdur) edilir."""
        self.age = age
        self.name = None

    def get_age(self):
        """Heyvanın yaşını qaytarır."""
        return self.age

    def get_name(self):
        """Heyvanın adını qaytarır."""
        return self.name

    def set_age(self, newage):
        """Heyvanın yaşını yenisi ilə dəyişir."""
        self.age = newage

    def set_name(self, newname=""):
        """Heyvanın adını dəyişir. Ad verilməzsə boş sətir mənimsədir."""
        self.name = newname

    def __str__(self):
        """Print edildikdə ekrana çıxacaq sətir təsviri."""
        return "animal:" + str(self.name) + ":" + str(self.age)

#a = Animal(4)
#print(a)               # Ekrana çıxır: animal:None:4
#a.set_name("fluffy")
#print(a.get_name())    # Ekrana çıxır: fluffy
#print(a)               # Ekrana çıxır: animal:fluffy:4 

class Cat(Animal):
    def speak(self):
        """Pişiyə məxsus yeni metod: ekrana miyov yazdırır."""
        print("meow")

    def __str__(self):
        """Valideynin __str__ metodunu üstələyir (Override edir)."""
        return "cat:" + str(self.name) + ":" + str(self.age)

#c = Cat(5)
#c.set_name("fluffy")  # Animal-dan irs alınan setter metodu
#print(c)              # Ekrana çıxır: cat:fluffy:5 (Cat-in öz __str__ metodu)
#c.speak()             # Ekrana çıxır: meow

class Person(Animal):
    def __init__(self, name, age):
        """İnsanın adını və yaşını təyin edir, dostlar siyahısını sıfırlayır."""
        Animal.__init__(self, age) # Valideynin init-ini çağırırıq
        self.set_name(name)        # Adı set_name vasitəsilə mənimsədirik
        self.friends = []          # Yeni daxili dəyişən (dostlar siyahısı)

    def get_friends(self):
        """Dostlar siyahısının kopyasını qaytarır (orijinalı qorumaq üçün)."""
        return self.friends.copy()

    def add_friend(self, fname):
        """Siyahıda yoxdursa yeni dost əlavə edir."""
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        """İnsanın danışma metodu."""
        print("hello")

    def age_diff(self, other):
        """İki insan arasındakı yaş fərqini tapır."""
        diff = self.age - other.age
        print(abs(diff), "year difference")

    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)

#p1 = Person("jack", 30)
#p2 = Person("jill", 25)

#print(p1)          # person:jack:30
#p1.speak()         # hello
#p1.age_diff(p2)    # 5 year difference

#p1.add_friend("ana")
#p1.add_friend("bob")
#print(p1.get_friends())  # ['ana', 'bob']

import random

class Student(Person):
    def __init__(self, name, age, major=None):
        """Person-un init-ini çağırır və ixtisas (major) atributunu əlavə edir."""
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        """İxtisası dəyişir."""
        self.major = major

    def speak(self):
        """Danışarkən təsadüfi olaraq 4 ifadədən birini deyir."""
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i'm still zooming")

    def __str__(self):
        return "student:" + str(self.name) + ":" + str(self.age) + ":" + str(self.major)

s1 = Student("john", 20, "computer science")
s2 = Student("jane", 21, "physics")

print(s1)          # student:john:20:computer science
s1.speak()         # i have homework