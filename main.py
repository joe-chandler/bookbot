import sys
from curses.ascii import isalpha
from stats import count_book_words, count_book_characters, sort_char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    count = count_book_words(text)
    char_count = count_book_characters(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in sort_char_dict(char_count):
        if isalpha(i['char']):
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()