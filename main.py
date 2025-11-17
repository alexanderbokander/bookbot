import sys
from stats import get_num_words, get_char_counts, get_sorted_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    char_counts = get_char_counts(book_text)
    sorted_char_counts = get_sorted_char_counts(char_counts)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_counts:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
