class MovieMatrix:
    '''Creating matrix from input file'''
    def __init__(self,movieList):
        '''Initialize data from input file'''
        self.__movieList = movieList
        
    def getMovieList(self):
        '''Get method for movie data from input file'''
        return self.__movieList
    
    def setMovieList(self, movieList):
        '''Set method for movie data from input file'''
        self.__movieList = movieList
        
    def getMovieNum(self):
        '''Break out numerical data into separate matrix'''
        matrix_num = []  # Create new matrix     
        for row in range(len(self.__movieList)):
            matrix_num.append([])  # Create new row
            
            # Append the range of the first section of numeric data
            for column in range(2, 5):  
                
                # Make into float value
                item = float(self.__movieList[row][column])  
                matrix_num[row].append(item)   #  Add to matrix
                
            # Append the range of the second section of numeric data
            for column in range(8, 11):
                
                # Make into float value
                item = float(self.__movieList[row][column])   
                matrix_num[row].append(item)   # Add to matrix
                
        # Return the completed matrix        
        return matrix_num

    def getMovieWord(self):
        '''Break out string data into separate matrix'''
        matrix_str = []    # Create new matrix
        for row in range(len(self.__movieList)):
            matrix_str.append([])   # Create new row
            
            # Append the range of the first section of string data
            for column in range(0, 2):
                item = self.__movieList[row][column]
                matrix_str[row].append(item)   #  Add to matrix
                
            # Append the range of the first section of string data
            for column in range(5, 8):
                item = self.__movieList[row][column]
                matrix_str[row].append(item)   #  Add to matrix
                
        # Return the completed matrix 
        return matrix_str
    
    
