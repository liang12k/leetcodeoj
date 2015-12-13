class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ansLatestIdx=0
        for n in nums:
            # handles all nums len; default max duplic can be 2
            # once after max duplic 2 is passed, cmp all elems onwards
            # the latest num 'n' vs last invalid duplic idx (ansLatestIdx) needs to have the next val
            # ^ if so, place the latest val here (ansLatestIdx-2), max 2 spaces away
            #
            # eg:   *n* what'll be replaced by latest non duplic val
            #       _n_ is the curr idx where non duplc val should be
            #
            #       [_1_,1,*1*,1,2,2,3,3,3,4]
            #       [1,1,_2_,1,*2*,2,3,3,3,4]->
            #       [1,1,2,_2_,2,*2*,3,3,3,4]->
            #       [1,1,2,2,_3_,3,*3*,3,3,4]->
            #       [1,1,2,2,3,_3_,*4*]->
            #       [1,1,2,2,3,3,_4_]->[1,1,2,2,3,3,4]
            #       *keep cmp against the latest idx where proper next non duplic val is supposed to be
            #        and the latest idx -2 (ansLatestIdx-2) is same as last valid num
            #
            if ansLatestIdx<2 or n>nums[ansLatestIdx-2]:
                nums[ansLatestIdx]=n
                ansLatestIdx+=1
        return ansLatestIdx