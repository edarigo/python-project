import unittest
from MovieMatrix import MovieMatrix

class TestMovieMatrix(unittest.TestCase):
    '''Unit Test for Movie Matrix Class'''
    def setUp(self):
        '''Set up data to be used in test'''
        # First test matrix
        self.test_matrix = [['2018','Maze Runner: The Death Cure','0','6.3','141',
                             'Action','Sci-Fi','January','51','62','58.03'],
                            ['2018','12 Strong','0','6.6','130','Action','Drama',
                             'January','54','15.82','45.49'],
                            ['2018','Sherlock Gnomes','0','4.9','86','Animation',
                             'Adventure','March','36','59','43.24'],
                            ['2018','Ready Player One','5','7.7','140','Action',
                             'Adventure','March','64','175','136.73']]
        
        # Second test matrix                    
        self.test_matrix2 = [['2018','Love, Simon','3','7.9','110','Comedy','Drama',
                              'March','72','17','40.83'],
                             ['2018','Death Wish','1','6.4','107','Action','Crime',
                              'March','31','30','13'],
                             ['2018','Black Panther','28','7.5','134','Action',
                              'Adventure','February','88','200','699.97'],
                             ['2018','Avengers: Infinity War','6','8.8','149',
                              'Action','Adventure','April','68','321','257.7']]
        
        # Call MovieMatrix class to pass through test matrices                     
        self.list1 = MovieMatrix(self.test_matrix)
        self.list2 = MovieMatrix(self.test_matrix2)
        
    def test_MovieNum(self):
        '''Test that only numeric data will be put into new matrix'''
        # Expected result for the first matrix
        self.movieNum_result = [[0,6.3,141,51,62,58.03],[0,6.6,130,54,15.82,45.49],
                            [0,4.9,86,36,59,43.24,],[5,7.7,140,64,175,136.73]]
        
        # Expected result for the second matrix
        self.movieNum2_result = [[3,7.9,110,72,17,40.83],[1,6.4,107,31,30,13],
                             [28,7.5,134,88,200,699.97],[6,8.8,149,68,321,257.7]]
        
        # Pass through the test matrices and compare to expected result
        self.assertListEqual(self.list1.getMovieNum(),self.movieNum_result)
        self.assertListEqual(self.list2.getMovieNum(),self.movieNum2_result)
        
    def test_MovieWord(self):
        '''Test that only string data will be put into new matrix'''
        # Expected result for the first matrix
        self.movieWord_result = [['2018','Maze Runner: The Death Cure','Action','Sci-Fi','January'],
                            ['2018','12 Strong','Action','Drama','January'],
                            ['2018','Sherlock Gnomes','Animation','Adventure','March'],
                            ['2018','Ready Player One','Action','Adventure','March']]
        
        # Expected result for the second matrix
        self.movieWord2_result = [['2018','Love, Simon','Comedy','Drama','March'],
                             ['2018','Death Wish','Action','Crime','March'],
                             ['2018','Black Panther','Action','Adventure','February'],
                             ['2018','Avengers: Infinity War','Action','Adventure','April']]
        
        # Pass through the test matrices and compare to expected result
        self.assertListEqual(self.list1.getMovieWord(),self.movieWord_result)
        self.assertListEqual(self.list2.getMovieWord(),self.movieWord2_result)
    
if __name__ == "__main__":
    unittest.main()