class MovieInfo:
    '''Class takes data from user and splits it into numeric and string lists'''
    def __init__(self,entryMovie):
        '''Initialize list with all data'''
        self.__entryMovie = entryMovie
        
    def getEntryMovie(self):
        '''Get method for data list'''
        return self.__entryMovie
    
    def setEntryMovie(self, entryMovie):
        '''Set method for data list'''
        self.__entryMovie = entryMovie
    
    def getEntryNumbers(self):
        '''Creates list from numeric data'''
        movie_numbers = [x for x in self.__entryMovie[1:7]]
        return movie_numbers  # Returns list
    
    def getEntryWords(self):
        '''Creates list from string data'''
        movie_words = [x for x in self.__entryMovie[7:10]]
        return movie_words  # Returns list
