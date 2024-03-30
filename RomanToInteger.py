# take an example of IX and XI and do a dry run
"""Intuition:
The key intuition lies in the fact that in Roman numerals, when a smaller value appears before a larger value, it represents subtraction, while when a smaller value appears after or equal to a larger value, it represents addition."""
class RomanToInteger:
    def romanToInt(self, s: str) -> int:
        m = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        for i in range(len(s)):
            if(i < len(s)-1 and m[s[i]] < m[s[i+1]]):
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        return ans


obj = RomanToInteger()
result = obj.romanToInt('IX')
print(result)
