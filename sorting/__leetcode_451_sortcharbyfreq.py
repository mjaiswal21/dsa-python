from collections import  Counter

#451. Sort Characters By Frequency
def sort_char_by_freq(s:str) -> str:

    #frequency Map
    freq = Counter(s)

    # custom sort based on the freq and char incase freq is same/tie

    sorted_char = sorted(freq.keys(), key=lambda c:(-freq[c], c))

    # building the stringsort_char_by_freq(s:str) -> str

    res = []

    for c in sorted_char:
        res.append(c * freq[c])

    return "".join(res)

st = 'zzzdvgvvvvv'
sorted_str = sort_char_by_freq(st)
print(sorted_str)


