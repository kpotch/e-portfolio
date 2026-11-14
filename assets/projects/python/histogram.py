# This program reads a text file (Myra.txt), counts how often each word appears,
# and displays the results in a formatted histogram table.

import string  # Used to remove punctuation from words

def histogram(fin):  
    """
    Reads a file object and returns a dictionary
    containing word frequencies.
    """
    
    # Create an empty dictionary to store word counts
    hist = dict()
    
    # Read every line in the file
    for line in fin:
        # Split the line into a list of words
        words = line.split()
        
        # Process each word in the list
        for word in words:
            # Convert word to lowercase and remove punctuation
            word = word.lower().strip(string.punctuation)
            
            # Check if the word is already in the dictionary
            if word in hist:
                # If yes, increase its count by 1
                hist[word] += 1
            else:
                # If no, add the word to the dictionary with count 1
                hist[word] = 1
                
    # Return the completed histogram dictionary
    return hist


def printHistogram(hist):
    """
    Prints the histogram dictionary in a formatted table.
    """
    
    # Print table header
    print("\nWord       Count")
    print("----------------")
    
    # Loop through each word in the dictionary
    for word in hist:
        # Print each word and its count in aligned columns
        print(f"{word:<12}{hist[word]:2d}")


# Open the file for reading
fin = open('Myra.txt')

# Notify user that file is being read
print('Reading file Myra.txt...')

# Call histogram function to build word frequency dictionary
hist = histogram(fin)

# Display the results using the print function
printHistogram(hist)
