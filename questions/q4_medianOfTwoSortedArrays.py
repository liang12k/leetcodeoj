class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        # list to hold all vals
        fullList=[]
        # idx start from end of both arrays
        idx1,idx2=len(nums1)-1,len(nums2)-1
        # continue loop until one or both lists' elemts are read
        # in single O(n) pass
        while idx1>=0 and idx2>=0:
            # append and decrement idx accordingly
            if nums1[idx1]>nums2[idx2]:
                fullList.append(nums1[idx1]); idx1-=1
            else:
                fullList.append(nums2[idx2]); idx2-=1
        # if there's remaining elems from lingering list
        # when list lengths are different
        if idx1>=0 and idx2<0:
            fullList.extend(nums1[:idx1+1][::-1])
        elif idx2>=0 and idx1<0:
            fullList.extend(nums2[:idx2+1][::-1])
        
        fullListLen=len(fullList)
        # handle getting median if len is odd or even
        if fullListLen%2:
            return fullList[fullListLen/2]*1.0
        # if even len, get middle vals and get avg of them both
        return (fullList[fullListLen/2]+fullList[(fullListLen/2)-1])/2.0