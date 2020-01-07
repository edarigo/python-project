import unittest
from MoviePoints import MoviePoints

class TestMoviePoints(unittest.TestCase):
    '''Unit Test to test the MoviePoints Class'''
    
    def setUp(self):
        '''Set up the data to use in the test'''
        
        # Average and Range data to use in test
        self.test_dataAverage = [9.06, 7.96, 129.17, 86.17, 35.27, 110.13]
        self.test_dataRange = [[5, 13], [7.2, 8.9], [100, 201], [64, 99], 
                               [1.5, 103], [17.02, 377.85]]
        
        # Test data for first test
        self.test_inputNum1 = [0,6.3,141,51,62,58.03]
        self.test_inputWords1 = ['action','sci-fi','january']
        
        # Test data for second test
        self.test_inputNum2 = [6,8.8,149,68,321,257.7]
        self.test_inputWords2 = ['action','adventure','april']
        
        # Word frequency data to use in test
        self.test_dataCount = {'adventure': 2, 'drama': 16, 'crime': 4, 'comedy': 3, 
                            'biography': 4, '6': 1, 'action': 1, 'none': 1, 
                            'history': 1, 'romance': 1, '7.8': 1, 'sport': 1, 
                            'december': 3, 'november': 5, 'october': 3, 'july': 1, 
                            'january': 3, '112': 1, 'february': 1, 'may': 1}
        
        # Call MoviePoints class to pass through test matrices  
        self.testPoints1 = MoviePoints('Maze Runner: The Death Cure',self.test_inputNum1,
                                       self.test_inputWords1,self.test_dataAverage,
                                       self.test_dataRange,self.test_dataCount)
        self.testPoints2 = MoviePoints('Avengers: Infinity War',self.test_inputNum2,
                                       self.test_inputWords2,self.test_dataAverage,
                                       self.test_dataRange,self.test_dataCount)
        
    def test_MoviePoints(self):
        '''Test that the function will return the correct percentage and format'''
        
        # Expected result 1
        outputPoints1 = "\'Maze Runner: The Death Cure has a 42.42 % chance of being best picture.\'"
        
        # Expected result 2
        outputPoints2 = "\'Avengers: Infinity War has a 51.52 % chance of being best picture.\'"
        
        # Pass through the test matrices and compare to expected result
        self.assertEqual(self.testPoints1.getTotalPoints(),outputPoints1)
        self.assertEqual(self.testPoints2.getTotalPoints(),outputPoints2)

if __name__ == "__main__":
    unittest.main()