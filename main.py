from stats import get_word_count, get_book_text , get_char_count, get_sort_dict, print_report


def main():
    PATH_TO_BOOK = "//home//zen//Desktop//Boot-dev_Projects///bookbot//books//frankenstein.txt"
    book_text = get_book_text(PATH_TO_BOOK)

    counted_words = get_word_count(book_text)
    counted_chars = get_char_count(book_text)

    sorted_dict = get_sort_dict(counted_chars)

    print_report(counted_words,sorted_dict)
    

    

            

main()
