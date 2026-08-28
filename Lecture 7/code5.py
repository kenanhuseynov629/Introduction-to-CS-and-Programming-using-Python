# s mətni daxilində c simvolunun ilk göründüyü indeks ilə son göründüyü indeks arasındakı fərqi tapmalıdır
# 1 ci numune
def first_to_last_diff(s, c):
    first_index = s.find(c)
    last_index = s.rfind(c)
    if first_index == -1 or last_index == -1:
        return -1
    return last_index - first_index

print(first_to_last_diff("hello", "l"))