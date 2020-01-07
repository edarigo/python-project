"""
Class movie info
"""
class MovieInfo:
    def __init__(self,entryMovie):
        self.__entryMovie = entryMovie
        
    def getEntryMovie(self):
        return self.__entryMovie
    
    def setEntryMovie(self, entryMovie):
        self.__entryMovie = entryMovie
    
    def getEntryNumbers(self):
        movie_numbers = [x for x in self.__entryMovie[1:7]]
        return movie_numbers
    
    def getEntryWords(self):
        movie_words = [x for x in self.__entryMovie[7:10]]
        return movie_words
