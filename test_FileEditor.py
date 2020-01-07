import unittest
import FileEditor

class TestFileEditor(unittest.TestCase):
    '''Unit Test to test the functions in FileEditor'''
    
    def setUp(self):
        '''Set up the test data'''
        
        # Data to enter for all data to be valid
        self.movieValid = ('2018','5','7.7','140','64','175','136.73','Action',
                        'Adventure','March')
        
        # Data to enter to see that error statements are working
        self.movieInValid = ('1999','28','seven','30','88','200','699.97','Action',
                        'Adventure','2')
        
        # String matrix data to test the word frequency
        self.test_matrixString = [['2017','The Shape of Water','Adventure','Drama',
                                   'December'],
                                ['2016','Moonlight','Drama','None','November'],
                                ['2015','Spotlight','Crime','Drama','November'],
                                ['2014','Birdman','Comedy','Drama','November'],
                                ['2013','12 Years a Slave','Biography','Drama',
                                 'November'],
                                ['2012','Argo','Biography','Drama','October'],
                                ['2011','The Artist','Comedy','Drama','October'],
                                ['2010','The King\'s Speech','Biography','Drama',
                                 'December'],
                                ['2009','The Hurt Locker','Drama','History','July'],
                                ['2008','Slumdog Millionaire','Drama','Romance',
                                 'January'],
                                ['2007','No Country for Old Men','Crime','Drama',
                                 'November'],
                                ['2006','The Departed','Crime','Drama','October'],
                                ['2005','Crash','6','7.8','112','Drama','None','May'],
                                ['2004','Million Dollar Baby','Drama','Sport',
                                 'January'],
                                ['2003','The Lord of the Rings: The Return of the King',
                                 'Adventure','Drama','December'],
                                ['2002','Chicago','Comedy','Crime','February'],
                                ['2001','A Beautiful Mind','Biography','Drama',
                                 'January'],
                                ['2000','Gladiator','Action','Drama','May']]

    def testValidInput(self):
        '''Test that the function passes through data that is valid and shows 
        error for invalid data'''
        
        # Expected result for valid data
        movie1_result = (2018,5,7.7,140,64,175,136.73,'action','adventure','march')
        
        # Call the validInput function to input data and create data in tuple
        self.assertEqual(FileEditor.validInput(),movie1_result)
        
    def test_genreMonthCount(self):
        '''Test that the function creates a dictionary counting the frequency
        of words'''
        
        # Expected result
        dataCount_result = {'adventure': 2, 'drama': 16, 'crime': 4, 'comedy': 3, 
                            'biography': 4, '6': 1, 'action': 1, 'none': 1, 
                            'history': 1, 'romance': 1, '7.8': 1, 'sport': 1, 
                            'december': 3, 'november': 5, 'october': 3, 'july': 1, 
                            'january': 3, '112': 1, 'february': 1, 'may': 1}
        
        # Call the genreMonthCount function and pass the test string data
        self.assertEqual(FileEditor.genreMonthCount(self.test_matrixString),
                         dataCount_result)
        
if __name__ == "__main__":
    unittest.main()
    