import unittest
from AverageRange import AverageRange

class TestAverageRange(unittest.TestCase):
    '''Unit test to test the AverageRange Class'''
    
    def setUp(self):
        '''Set up data to be used in test'''
        # First matrix to test
        self.test_matrix = [[0,6.3,141,51,62,58.03],[0,6.6,130,54,15.82,45.49],
                            [0,4.9,86,36,59,43.24],[5,7.7,140,64,175,136.73]]
        
        # Second matrix to test
        self.test_matrix2 = [[6,8.8,149,68,321,257.7],[3,7.9,110,72,17,40.83],
                             [1,6.4,107,31,30,13],[28,7.5,134,88,200,699.97]]
        
        # Call AverageRange class to pass through test matrices  
        self.list1 = AverageRange(self.test_matrix)
        self.list2 = AverageRange(self.test_matrix2)
        
    def test_MovieAverage(self):
        '''Test that the function will return the average of each matrix column'''
        
        # Expected result 1
        self.list1_result = [1.25,6.37,124.25,51.25,77.95,70.87]
        
        # Expected result 2
        self.list2_result = [9.5,7.65,125,64.75,142,252.88]
        
        # Pass through the test matrices and compare to expected result        
        self.assertListEqual(self.list1.getMovieAverage(),self.list1_result)
        self.assertListEqual(self.list2.getMovieAverage(),self.list2_result)
        
    def test_RangeMinMax(self):
        '''Test that the function will return the range (min-max) of each matrix
        column'''
        
        # Expected result 1
        self.list1_result = [[0,5],[4.9,7.7],[86,141],[36,64],[15.82,175],
                             [43.24,136.73]]
        
        # Expected result 2
        self.list2_result = [[1,28],[6.4,8.8],[107,149],[31,88],[17,321],
                             [13,699.97]]
        
        # Pass through the test matrices and compare to expected result
        self.assertListEqual(self.list1.getRangeMinMax(),self.list1_result)
        self.assertListEqual(self.list2.getRangeMinMax(),self.list2_result)
    
if __name__ == "__main__":
    unittest.main()