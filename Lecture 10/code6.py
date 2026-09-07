def square_list(L):
    """
    Mutates L in place by squaring each element.
    Returns None!
    """
    for i in range(len(L)):    # i növbə ilə 0, 1, 2... indekslərini alır [65]
        L[i] = L[i]**2         # i-ci yuvadakı dəyəri silib yerinə kvadratını yazırıq [66, 67]

# Sınaq və Trassirovka:
Lin = [12, 13, 15]
square_list(Lin)               # Diqqət: Heç bir dəyişənə mənimsətmirik! [68]
print(Lin)                     # [9, 15, 51] çap olunacaq (Orijinal Lin mutasiya olundu!) [68, 69]