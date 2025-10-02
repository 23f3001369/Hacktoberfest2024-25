class Solution(object):
    def removeKdigits(self, num, k):
        
        stack = []
        n = len(num)

        if n == k:
            return "0"

        for i in range(n):
            while stack and k > 0 and (stack[-1] > num[i]):
                stack.pop()
                k -= 1
            
            stack.append(num[i])
        
        # for cases like 123456 and k = 3
        while k > 0:
            stack.pop()
            k -= 1
        
        # leading 0
        result = "".join(stack).lstrip("0")
        return result if result else "0"
