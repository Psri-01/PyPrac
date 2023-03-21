# if list is [2,7,5,10] and target=9 print the output as [0,1] i.e. indexes of those nums whose sum is the target
class Solution(object):
    def twoSum(self, nums, target):
        s = {}
        for i in range(len(nums)):
            out = target - nums[i]
            if out in s:
                return [s[out], i]
            else:
                s[nums[i]] = i
