string = 'abc'


def all_variants(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            yield s[i:j]


print(*sorted(all_variants(string), key=lambda x: (len(x), x)), sep='\n')
