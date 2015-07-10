'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''
class Solution(object):
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums: return nums
        currn=None
        counter=0
        for n in nums:
            if currn!=n:
                currn=n
                nums[counter]=currn
                counter+=1
        nums=nums[:counter]
        return counter


if __name__=="__main__":
    inp=[1,1,2]
    print Solution().removeDuplicates(inp)
