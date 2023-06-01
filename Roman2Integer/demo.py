def romanToInt_my_first(s: str) -> int:
    #This is my first answer. 
    #This solution is not simple.
    ans = 0
    
    if "CM" in s:
        s = s.replace('CM', '')
        ans += 900

    if "CD" in s:
        s = s.replace('CD', '')
        ans += 400

    if "XC" in s:
        s = s.replace('XC', '')
        ans += 90

    if "XL" in s:
        s = s.replace('XL', '')
        ans += 40

    if "IX" in s:
        s = s.replace('IX', '')
        ans += 9

    if "IV" in s:
        s = s.replace('IV', '')
        ans += 4

    if "D" in s:
        s = s.replace('D', '')
        ans += 500

    if "L" in s:
        s = s.replace('L', '')
        ans += 50

    if "V" in s:
        s = s.replace('V', '')
        ans += 5

    ans += s.count("I")
    ans += s.count("X")*10
    ans += s.count("C")*100
    ans += s.count("M")*1000
    return ans


def romanToInt(s: str) -> int:
    #This method was written after watching a solution video.
    dict = {"I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}

    ans = 0
    for i, v in enumerate(s):
        corr = -1 if i<len(s)-1 and dict[s[i+1]] > dict[s[i]] else 1
        ans += dict[v] * corr

    return ans