import unittest

import statistics

# the analyze function takes in an var arguent of numbers
# it should return a dicitonary of {'mean':0,'median':0,'mode':0,'largest':0,'smallest':0}
def analyze(*nums):
    
    # defining helpful variables using built in math functions and sorted
    length = len(nums)
    mean = sum(nums) / length
    sortednums = sorted(nums)
    median = sortednums[length // 2]
    
    largest = sortednums[length - 1]
    smallest = sortednums[0]
 
    mode = statistics.mode(nums)
    # If you don't want to import stats for whatever reason, this also works:
    # mode = max(sortednums, key=sortednums.count)

    #Here is another way to define the mode:
    # counts = {}
    # for num in nums:
    #     counts[num] = counts.get(num, 0) + 1
    # max_seen = max(counts.values())
    # mode = []
    # for count in counts:
    #     if counts[count] == max_seen:
    #         mode.append(count)
    

    # Creating the dictionary (key ,value pair) from the statistics calculated above
    stat_dictionary = {
      'mean':mean,
      'median':median,
      'mode':mode,
      'largest':largest,
      'smallest':smallest
    }
    return stat_dictionary
# Test cases passed


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_analyze_1(self):
        data = analyze(1,2,2,2,3)
        self.assertDictEqual(data, {'mean':2,'median':2,'mode':2, 'largest':3,'smallest':1})
        

    def test_analyze_2(self):
        data = analyze(10,5,10,200,-65)
        self.assertDictEqual(data, {'mean':32,'median':10,'mode':10, 'largest':200,'smallest':-65})
        


if __name__ == '__main__':
    unittest.main()
