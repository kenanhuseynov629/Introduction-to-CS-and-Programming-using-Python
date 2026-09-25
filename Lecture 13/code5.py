def pairwise_div(Lnum, Ldenom):
    """
    Lnum və Ldenom eyni uzunluqda və boş olmayan ədəd listləridir.
    Lnum-un elementlərini Ldenom-un uyğun elementlərinə bölərək yeni list qaytarır.
    Əgər Ldenom daxilində 0 varsa, ValueError qaldırır.
    """
    if 0 in Ldenom:
        raise ValueError("Ldenom listində sıfır (0) var, bölmə aparıla bilməz!")
    
    result = []
    for i in range(len(Lnum)):
        result.append(Lnum[i] / Ldenom[i])
    return result

Lnum = [1, 2, 3, 4]
Ldenom = [2, 8, 4, 8]
print(pairwise_div(Lnum, Ldenom))