myname = "Jonathan"

pi = 3.142

# function to calc the area of a
# circle

def areaCircle(radius):
    """Calculates the area of a circle"""
    pi = 3.142
    area = pi*(radius*radius)
    return f"Area of the circle: {area}"

# func to count the number of words in a text file

def countWords(file):
    countWords.__doc__="counts the  number of words in a text file"
    with open(file) as f:
        file_contents = f.read()
        word_list = file_contents.split()
        word_count = len(word_list)
    return f"No. of words: {word_count}"