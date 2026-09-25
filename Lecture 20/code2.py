from dateutil import parser

class Workout(object):
    """Məşqləri izləmək üçün əsas baza klassı."""

    # Klass Dəyişəni: Bütün məşq obyektləri üçün saatda yandırılan orta kalori
    cal_per_hr = 200

    def __init__(self, start, end, calories=None):
        """
        start və end mətn formatında tarixlərdir (örnəyin: "1/1/2021 1:23 PM").
        calories könüllü parametridir, verilməzsə None olur.
        """
        self.start = parser.parse(start)
        self.end = parser.parse(end)
        self.icon = '😓'
        self.kind = 'Workout'
        self.calories = calories

    def get_calories(self):
        """
        Kalori verilməyibsə (None-dursa), məşq müddətinə əsasən avtomatik hesablayır.
        Əks halda mövcud kalori dəyərini qaytarır.
        """
        if self.calories is None:
            # (self.end - self.start) timedelta obyekti verir
            duration_seconds = (self.end - self.start).total_seconds()
            return Workout.cal_per_hr * (duration_seconds / 3600.0)
        else:
            return self.calories

    def get_duration(self):
        """Məşqin davam etmə müddətini timedelta obyekti kimi qaytarır."""
        return self.end - self.start

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_kind(self):
        return self.kind

    def set_calories(self, calories):
        self.calories = calories

    def set_start(self, start):
        self.start = parser.parse(start)

    def set_end(self, end):
        self.end = parser.parse(end)

    def __eq__(self, other):
        """İki məşq obyektinin eyniliyini yoxlayır."""
        return (type(self) == type(other) and
                self.start == other.start and
                self.end == other.end and
                self.kind == other.kind and
                self.get_calories() == other.get_calories())

    def __str__(self):
        """Ekrana ağıllı saat şəkilli vizual kart çıxarır."""
        width = 16
        retstr = f"|{'-' * width}|\n"
        retstr += f"|{' ' * width}|\n"
        retstr += f"| {self.icon}{' ' * (width - 3)}|\n"
        retstr += f"| {self.kind}{' ' * (width - len(self.kind) - 1)}|\n"
        retstr += f"|{' ' * width}|\n"
        duration_str = str(self.get_duration())
        retstr += f"| {duration_str}{' ' * (width - len(duration_str) - 1)}|\n"
        cal_str = f"{round(self.get_calories(), 1)}"
        retstr += f"| {cal_str} Calories {' ' * (width - len(cal_str) - 11)}|\n"
        retstr += f"|{' ' * width}|\n"
        retstr += f"|{'_' * width}|\n"
        return retstr

# 1 saat 30 dəqiqəlik məşq (10:00 - 11:30)
# calories parametrini boş buraxırıq (default olaraq None olur)
w1 = Workout("2026-06-25 10:00", "2026-06-25 11:30")

# Müddəti alaq:
print(w1.get_duration())  
# Çıxış: 1:30:00

# Kalori avtomatik hesablanır: 1.5 saat * 200 kal/saat = 300.0
print(w1.get_calories())  
# Çıxış: 300.0