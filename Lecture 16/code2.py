def score_count_memo(x, d):
    if x in d:
        return d[x]
    else:
        score = score_count_memo(x - 1, d) + score_count_memo(x - 2, d) + score_count_memo(x - 3, d)
        d[x] = score
        return score

d = {1: 1, 2: 2, 3: 3}
print(score_count_memo(13, d))  # Nəticə: 1431