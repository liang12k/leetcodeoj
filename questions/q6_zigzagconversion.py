class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        # note: the direction is |/|/|/...|/|
        # 
        # ideas:
        # O(n) go thru whole 's' in single pass
        # need to handle base case of few chars (w applying the logic below)
        # numRows for number of lists to hold values
        # idx to keep vals within list
        # idx to keep count where char is entered
        # 
        # whitespaces, TBD (are they needed?)
        # -'ignore' them and just add in the char at correct positions