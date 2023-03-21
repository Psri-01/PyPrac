def romanToInt(self, s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, "k": 0}
    tmp = s + "k"
    res = idx = 0

    while idx != len(s):

        if roman[s[idx]] < roman[tmp[idx + 1]]:
            res += roman[tmp[idx + 1]] - roman[s[idx]]
            idx += 2
        else:
            res += roman[s[idx]]
            idx += 1

    return res
