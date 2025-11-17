def get_num_words(text):
    """
    Returns the number of words in the given text string.
    """
    return len(text.split())

def get_char_counts(text):
    """
    Returns a dictionary with the count of each character (lowercased) in the text.
    """
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def get_sorted_char_counts(char_counts):
    """
    Returns a sorted list of dictionaries with character and count.
    Only includes alphabetical characters.
    Sorted from greatest to least by count.
    """
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list