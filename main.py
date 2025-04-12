from stats import get_num_words, count_characters, sort_and_format
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file_location = sys.argv[1]

    num_words = get_num_words(get_book_text(book_file_location))
    character_count = count_characters(get_book_text(book_file_location))
    print(character_count)

    print(f"============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for chardict in sort_and_format(character_count):
        if chardict["char"].isalpha():
            print(f"{chardict["char"]}: {chardict["count"]}")
    print("============= END ===============")


main()