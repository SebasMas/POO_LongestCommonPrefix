class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {} # Para guardar el valor y su índice
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        return []

tar = 6
n = [3,3]
s = Solution()
print(s.twoSum(n, tar))# two_sum
