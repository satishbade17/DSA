class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        s = s.lstrip()

        if not s:
            return 0

        sign = 1
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]

        res = 0

        for char in s:
            if char.isdigit():
                res = res * 10 + int(char)
            else:
                break

        res *= sign

        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX

        return res
sol = Solution()

print(sol.myAtoi("42"))          # 42
print(sol.myAtoi("   -42"))      # -42
print(sol.myAtoi("4193 with"))   # 4193
print(sol.myAtoi("words 123"))   # 0
print(sol.myAtoi("-91283472332"))# -2147483648