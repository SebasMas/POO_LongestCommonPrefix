class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = 0
        end_found = False
        for char in s[::-1]:
            if char == " ":
                if end_found:
                    break    
            else:
                end_found = True
                t += 1
        return t
        
s = "Hola cómo estás"
solution = Solution()
print(solution.lengthOfLastWord(s))