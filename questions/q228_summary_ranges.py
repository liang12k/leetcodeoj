'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans=[] # ans list
        subans=[] # container to hold the ongoing ans strs
        endidx=0
        # handle if single, non-single range (eg: [1] o/p ["1"], [1,3] o/p ["1","3"], [1,2,3] o/p ["1->3"])
        check_subans=lambda lst: lst[0] if lst[0]==lst[-1] else lst[0]+"->"+lst[-1]
        # goes thru the list, handles the blank and single number case
        for idx,n in enumerate(nums):
            if abs(nums[endidx]-n)>1:
                ans.append(check_subans(subans))
                subans=[] # reset the container
            subans.append(str(n)) # always append the number as it's valid in the current range check
            endidx=idx
        if subans: ans.append(check_subans(subans)) # handle lingering num range
        return ans