class AverageRange:
    '''This class creates two matricies for average and range using the data from 
    the input file.'''
    def __init__(self,matrixNum):
        '''Initialize matrixNum, which holds the numeric information from the 
        input file'''
        self.matrixNum = matrixNum
        
    def setMovieList(self, matrixNum):
        '''Set matrixNum method'''
        self.matrixNum = matrixNum

    def getMovieAverage(self):
        '''Creat matrix with average of the columns from matrix_num'''
        average_list = []   # Create empty list
        for column in range(len(self.matrixNum[0])):
            total = 0   # Initialize total to 0
            for row in range(len(self.matrixNum)):
                total += self.matrixNum[row][column]
                
                # Find average of each column
                average = round(total / len(self.matrixNum), 2)  
            average_list.append(average)  # Add average to average_list
        return average_list   # Return completed list

    def getRangeMinMax(self):
        '''Range of each category from minimum number to maximum number'''
        rangeMinMax = []    # Create empty list
        for column in range(len(self.matrixNum[0])):
            #  Starting with the first item in the first column
            minColumn = self.matrixNum[0][column]   
            maxColumn = self.matrixNum[0][column]
            rangeMinMax.append([])  # Add new row
            
            # Find the minimum value in the each column
            for row in range(len(self.matrixNum)):
                if self.matrixNum[row][column] < minColumn:
                    minColumn = self.matrixNum[row][column]
            rangeMinMax[column].append(minColumn)  # Add minimum value to matrix
            
            # Find the maximum value in each column
            for row in range(len(self.matrixNum)):
                if self.matrixNum[row][column] > maxColumn:
                    maxColumn = self.matrixNum[row][column]
            rangeMinMax[column].append(maxColumn)   # Add maximum value to matrix
        return rangeMinMax   # Return completed matrix