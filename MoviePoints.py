class MoviePoints:
    '''This class calculates the total points and percentage from data provided
    by the user'''
    
    def __init__(self,title,inputNum,inputWords,dataAverage,dataRange,
                 dataCount):
        '''Initialize data title, data from user and data from file'''
        self.title = title  # Movie title
        self.inputNum = inputNum   # Numeric data from user
        self.inputWords = inputWords   # String data from user
        self.__dataAverage = dataAverage   # Average data calculated from file
        self.__dataRange = dataRange   # Range of minimum and maximum data from file
        self.__dataCount = dataCount   # Dictionary of word frequency from file
        
    def getdataAverage(self):
        '''Get method for list of data average'''
        return self.__dataAverage
    
    def getdataRange(self):
        '''Get method for list of data range'''
        return self.__dataRange
    
    def getdataCount(self):
        '''Get method for dictionary word count'''
        return self.__dataCount
    
    def setdataAverage(self, dataAverage):
        '''Set method for list of data average'''
        self.__dataAverage = dataAverage
        
    def setdataRange(self, dataRange):
        '''Set method for list of data range'''
        self.__dataRange = dataRange
        
    def setdataCount(self, dataCount):
        '''Set method for dictionary word count'''
        self.__dataCount = dataCount
    
    def setTitle(self, title):
        '''Set method for movie title'''
        self.title = title
        
    def setInputNum(self, inputNum):
        '''Set method for user provided numeric data'''
        self.inputNum = inputNum
    
    def setInputWords(self, inputWords):
        '''Set method for user provided numeric data'''
        self.inputWords = inputWords
        
    def getTotalPoints(self):
        '''Get method for total points and percentage'''
        total_points = 0
        
        # Points for range of categories with numeric data
        for i in range(len(self.inputNum)):
            
            if self.inputNum[i] > self.__dataAverage[i]:
                '''If the number from user is above average and is within the 
                top range (between average and maximum)'''
                if self.inputNum[i] <= self.__dataRange[i][1]:
                    total_points += 3
                # If the number is above average but not within the range  
                else:
                    total_points += 2
                    
            elif self.inputNum[i] < self.__dataAverage[i]:
                '''if the number from user is below average and is within the 
                bottom range (between average and minimum)'''
                if self.inputNum[i] >= self.__dataRange[i][0]:
                    total_points += 2
                # If the number is below average but not within the range    
                else:
                    total_points += 1

        # Points for genre, if the first genre is in the dictionary
        if (self.inputWords[0] in self.__dataCount) is True: 
            '''If the first genre is one of the more common genres below, 
            more points are rewarded'''
            if self.inputWords[0] == "drama":
                total_points += 5
        
            elif self.inputWords[0] == "crime":
                total_points += 4
    
            elif self.inputWords[0] == "biography":
                total_points += 3
            
            elif self.inputWords[0] == "comedy":
                total_points += 2
                
            else:
                total_points += 1
        else:
            total_points += 0
        
        # If the second genre is in the dictionary
        if (self.inputWords[1] in self.__dataCount) is True: 
            '''If the second genre is one of the more common genres below, 
            more points are rewarded'''
            if self.inputWords[1] == "drama":
                total_points += 5
    
            elif self.inputWords[1] == "crime":
                total_points += 4
    
            elif self.inputWords[1] == "biography":
                total_points += 3
            
            elif self.inputWords[1] == "comedy":
                total_points += 2
                
            else:
                total_points += 1
        else:
            total_points += 0

        # Points for release month
        if (self.inputWords[2] in self.__dataCount) is True:   
            '''If the release month is one of the more common months below, 
            more points are rewarded'''
            if self.inputWords[2] == "november":
                total_points += 5
                
            elif self.inputWords[2] == "december":
                total_points += 3
                
            elif self.inputWords[2] == "october":
                total_points += 2
                
            elif self.inputWords[2] == "january":
                total_points += 2
                
            else:
                total_points += 1
        else:
            total_points += 0
        
        # Total points are added together and divided by 33 (total points possible)
        # Multiply by 100 to get percentage
        probability = (float(total_points) / 33) * 100  
        
        # Return the result with the movie name provided by user and probability
        return repr("{} has a {:,.2f} % chance of being best picture.".format(
                self.title,probability))