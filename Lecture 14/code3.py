def most_common_words(freqs):
    """
    freqs: söz tezliyi lüğəti
    Qaytarır: (ən çox təkrar olunan sözlər siyahısı, maksimum təkrar sayı)
    """
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

print(most_common_words({'I': 4, 'am': 3, 'happy': 3}))