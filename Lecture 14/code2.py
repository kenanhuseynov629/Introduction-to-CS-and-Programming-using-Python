def lyrics_to_frequencies(lyrics):
    """
    lyrics: sözlərdən ibarət siyahı (list)
    Qaytarır: hər sözün təkrar sayını saxlayan lüğət (dict)
    """
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

lyrics = ["I", "am", "happy", "I", "am", "happy", "I", "am", "happy"]
print(lyrics_to_frequencies(lyrics))