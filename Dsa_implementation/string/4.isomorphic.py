class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        st = {}
        ts = {}

        for i, j in zip(s, t):
            if i in st:
                if st[i] != j:
                    return False
            else:
                st[i] = j

            if j in ts:
                if ts[j] != i:
                    return False
            else:
                ts[j] = i

        return True


s = "egg"
t = "add"

obj = Solution()
print(obj.isIsomorphic(s, t))