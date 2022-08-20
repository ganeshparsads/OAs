class Solution:
    def numDecodings(self, s):
        # the key is to deal with zeros, so let's handle invalid cases first
        # if "00" in s or s[0] == '0':
        #     return 0
        
        res = [1]
        for i in range(len(s)):
            if i == 0:  # initialize the first character's result
                res.append(1)
                continue
            # get current and previous char
            c = s[i]
            cp = s[i - 1]
            if c == '0':  # if current is zero, must combine with previous digist so will have same variants as the result before the last one
                if cp > '2':
                    return 0
                res.append(res[-2])
                continue
            if cp == '0':  # if previous is zero, the current char has to form a number by itself, so will have same variants as last one
                res.append(res[-1])
                continue
            # if neither is zero, we check if it can combine with previou char
            cur = res[-1]
            if int(cp + c) < 27:
                cur += res[-2]
            res.append(cur)
            
        return res[-1]

ip = "100200300"
obj = Solution()

print(obj.numDecodings(ip))
