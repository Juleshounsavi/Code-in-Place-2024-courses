
def main():
    words = load_words_from_file("words.txt")
    word_counts = count_words(words)
    for word, count in word_counts.items():
        print_histogram_bar(word, count)

def print_histogram_bar(word, count):
    """
    Prints one bar in the histogram.

    Uses formatted strings to do so. The 
        {word : <8}
    adds white space after a string to make
    the string take up 8 total characters of space.
    This makes all of our words on the left of the 
    histogram line up nicely. On the other end,
        {'x' * count}
    takes the 'x' string and duplicates it by 'count'
    number of times. So 'x' * 5 would be 'xxxxx'.

    Calling print_histogram_bar("mom", 7) would print:
        mom     : xxxxxxx
    """
    print(f"{word : <8}: {'x' * count}")

def load_words_from_file(filepath):
    """
    Loads words from a file into a list and returns it.
    We assume the file to have one word per line.
    Returns a list of strings. You should not modify this
    function.
    """
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)
    
    return words

def count_words(words):
    """
    Counts the occurrences of each word in the list.
    Returns a dictionary with words as keys and their
    counts as values.
    """
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1
    return word_counts

if __name__ == '__main__':
    main()
