# s mətni daxilində c simvolunun ilk göründüyü indeks ilə son göründüyü indeks arasındakı fərqi tapmalıdır
# 2 ci numune

def first_to_last_diff(s, c):
    if c not in s:
        return -1
    first_index = s.find(c)
    for j in range(len(s)-1, -1, -1):
        if s[j] == c:
            # j dəyişənində sonuncu tapılan yerin indeksi saxlanılır və dövr dayandırılır
            break
    return j - first_index

print(first_to_last_diff("hello", "l"))