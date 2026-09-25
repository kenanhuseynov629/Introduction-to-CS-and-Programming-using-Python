class SimpleWorkout(object):
    """Məşqləri izləmək üçün sadə ilkin klass."""

    def __init__(self, start, end, calories):
        """Obyekt yarandıqda başlama, bitmə vaxtı və kalori təyin olunur."""
        self.start = start
        self.end = end
        self.calories = calories
        self.icon = '😓'
        self.kind = 'Workout'

    def get_calories(self):
        """Kalori dəyərini qaytarır (Getter)."""
        return self.calories

    def get_start(self):
        """Başlama vaxtını qaytarır (Getter)."""
        return self.start

    def get_end(self):
        """Bitmə vaxtını qaytarır (Getter)."""
        return self.end

    def set_calories(self, calories):
        """Kalori dəyərini yeniləyir (Setter)."""
        self.calories = calories

    def set_start(self, start):
        """Başlama vaxtını yeniləyir (Setter)."""
        self.start = start

    def set_end(self, end):
        """Bitmə vaxtını yeniləyir (Setter)."""
        self.end = end

morning_run = SimpleWorkout("08:00", "09:00", 350)
print(morning_run.kind)   # Çıxış: Workout
print(morning_run.icon)