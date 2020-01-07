from MovieInfo import MovieInfo
from MovieMatrix import MovieMatrix
from AverageRange import AverageRange
from MoviePoints import MoviePoints
import sys

def validInput():
    '''Getting the input and validating the information from user'''
    yearId = input("Enter the year the movie was released: ")  # Year of release
    nomination = input("Enter the number of nominations, enter 0 if none: ")
    
    # Check to see that the year and nomination entries are integers
    try:
        yearId = int(yearId)
        nomination = int(nomination)
    except:
        print("Enter integers only for the categories Year and Nominations.")
        sys.exit()
    
    # Check if the year is after 2018 or before 2000    
    if yearId > 2018 or yearId < 2000:
        print("Movies should only be released between years 2000 and 2018")
        sys.exit()
        
    rating = input("Enter the rating from IMDB database: ")  # Public rating
    duration = input("Enter the duration in minutes: ")   # Time length of movie
    
    # Critic rating
    metacritic = input("Enter the metacritic number according to IMDB: ")
    
    # Estimated budget to shoot the movie
    budget = input("Enter the estimated budget according to IMDB (e.g. 34 \
million is 34.0): ")
    
    # Gross amount earned from box office
    gross_usa = input("Enter the gross box office amount according to IMDB (e.g. 34 \
million is 34.0): ")

    # Check that the rating, duration, critic, budget and gross are float values
    try:    
        rating = float(rating)
        duration = float(duration)
        metacritic = float(metacritic)
        budget = float(budget)
        gross_usa = float(gross_usa)
    except:
        print("Enter numbers only for the categories Rating, Duration, \
Metacritic, Budget and Gross Box Office.")
        sys.exit()
    
    # Accoring to the Academy Award requirements, movies must be at least 40 min
    if duration < 40 :
        print("Movies need to be at least 40 minutes in order to be considered \
for the Best Picture category.")
        sys.exit()
    
    # The category of the movie
    genre1 = input("Enter the first genre of the movie according to IMDB (e.g. Drama): ")
    genre2 = input("Enter the second genre of the movie according to IMDB (e.g. Drama): ")
    
    # Month the movie was released
    release_month = input("Enter the month the movie was released (e.g. October): ")
    
    # Make all strings lower case
    try:
        genre1 = genre1.lower()
        genre2 = genre2.lower()
    except:
        print("Enter words only for both Genre categories.")
        sys.exit()
    
    # List of possible months to enter
    months = ["january","february","march","april","may","june","july",
              "august","september","october","november","december"]
    
    # Make all strings lower case
    try:
        release = release_month.lower()
        if (release in months) == False:  # If the input month is not in the list
            print("Enter the full name of the month.")      
    except:
        print("Enter the full name of the month.")
        sys.exit()
    
    # Return the valid data from user    
    return yearId, nomination, rating, duration, metacritic, budget, gross_usa, \
           genre1, genre2, release

def genreMonthCount(matrix_string):
    '''Count the occurence of words from the data file'''
    wordCounts = {} # Create an empty dictionary to count words

    # Count the words from the genre and month categories
    for column in range(2,5):
        for row in range(len(matrix_string)):
            processLine(matrix_string[row][column].lower(), wordCounts)
     
    pairs = list(wordCounts.items()) # Get pairs from the dictionary   

    items = [[count, word] for (word, count) in pairs] 
    items.sort(reverse = True) # Sort pairs in items
    
    # Returns the dictionary
    return wordCounts
  
def processLine(words, wordCounts): 
    '''Count each word in the line'''
    if words in wordCounts:
        wordCounts[words] += 1
    else:
        wordCounts[words] = 1 # Add an item in the dictionary

if __name__ == '__main__':
    # Prompt user to enter the movie data file for best picture between 2000 - 2017
    filename = input("Enter a filename: ").strip()
    
    # Check that file exists
    try:
        infile = open(filename,"r")   # Open file
    except IOError:
        print("File {} does not exist. Try again.".format(infile))
        sys.exit()

    f = infile.read()   # Read file
    f_items = f.split(",")
    f_list = [x for x in f_items]   # Transfer information into list

    col = 11  # There are 11 categories
    
    # Create matrix where each column is a category
    matrix_file = [f_list[i:i+col] for i in range(0, len(f_list),col)]
    
    # Pass the full data matrix to split up the numeric and string data
    movies_data = MovieMatrix(matrix_file)  
    
    # Contains the matrix with numeric data
    matrix_numbers = movies_data.getMovieNum()
    
    # Contains the matrix with string data
    matrix_string = movies_data.getMovieWord()
    
    # Pass the numeric matrix to get the average and range of numbers
    average_range = AverageRange(matrix_numbers)
    
    # Contains the matrix with the average of each column
    numbers_average = average_range.getMovieAverage()
    
    # Contains the matrix with the range (min - max) of each column
    matrix_range = average_range.getRangeMinMax()
    
    # Contains the dictionary
    word_count = genreMonthCount(matrix_string)

    # Get movie title from user
    title = input("Enter the name of the movie: ")
    
    # Get the validated input data
    movie_input = validInput()
    
    # Pass the data collected from user to be split into numeric and string data
    movie = MovieInfo(movie_input)
    
    # Contains the numeric data from user
    input_numbers = movie.getEntryNumbers()
    
    # Conains the string data from user
    input_words = movie.getEntryWords()
    
    # Pass the title, data from user (numeric and string), average and range
    #   and word frequency dictionary to add up points
    movie_points = MoviePoints(title,input_numbers,input_words,numbers_average,
                               matrix_range,word_count)
    
    # Prints the result from the MoviePoints class
    print(movie_points.getTotalPoints())