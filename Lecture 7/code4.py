def keep_consonants(word):
    consonants = ""
    for letter in word:
        if letter.lower() not in "aeiou":
            consonants += letter
    return consonants

print(keep_consonants("Hello"))