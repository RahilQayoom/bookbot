import sys
## from pathlib import Path
from stats import get_word_count, get_book_text , get_char_count, get_sort_dict, print_report


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)

    counted_words = get_word_count(book_text)
    counted_chars = get_char_count(book_text)
    sorted_dict = get_sort_dict(counted_chars)

    print_report(counted_words,sorted_dict,path_to_book)
    

    

            

main()
