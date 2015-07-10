'''
::KEY:: need to edit 'nums' list input!
Given a sorted array, remove the duplicates in place such that each element
appear only once and return the new length.

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
        # the tracker, keep tabs on latest value
        # 'counter' for unique values so far & used to slice the list (see for loop)
        currn=None
        counter=0
        for n in nums:
	    # if unique value, this is the latest
	    if currn!=n:
		currn=n
		# set unique value at current counter (used as index)
		nums[counter]=currn
		# increment counter for next index & as latest unique values counted
		counter+=1
	# nums has been edited, slice list to get from [0:counter]
	nums=nums[:counter]
	# return int as directed
	return counter


if __name__=="__main__":
    inp=[1,1,2]
    print Solution().removeDuplicates(inp)
