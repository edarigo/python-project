import unittest
from MovieInfo import MovieInfo

class TestMovieInfo(unittest.TestCase):
    '''Unit Test to test the MovieInfo Class'''
    
    def setUp(self):
        '''Set up the data to use in test'''
        
        # First list for testing
        self.list1 = MovieInfo([2018,0,6.3,141,51,62,58.03,"action","sci-fi", "january"])
        
        # Second list for testing
        self.list2 = MovieInfo([2018,6,8.8,149,68,321,257.7,"action","adventure","april"])
        
    def test_EntryNumbers(self):
        '''Test that the function will return a list of numeric data'''
        
        # Expected result 1
        self.list1_result = [0,6.3,141,51,62,58.03]
        
        # Expected result 2
        self.list2_result = [6,8.8,149,68,321,257.7]
        
        # Pass through the test matrices and compare to expected result
        self.assertListEqual(self.list1.getEntryNumbers(),self.list1_result)
        self.assertListEqual(self.list2.getEntryNumbers(),self.list2_result)
        
    def test_EntryWords(self):
        '''Test that the function will return a list of string data'''
        
        # Expected result 1
        self.list1_result = ["action","sci-fi", "january"]
        
        # Expected result 2
        self.list2_result = ["action","adventure","april"]
        
        # Pass through the test matrices and compare to expected result
        self.assertListEqual(self.list1.getEntryWords(),self.list1_result)
        self.assertListEqual(self.list2.getEntryWords(),self.list2_result)
    
if __name__ == "__main__":
    unittest.main()