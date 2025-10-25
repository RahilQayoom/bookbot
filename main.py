from stats import get_word_count, get_book_text , get_char_count


def main():
    counted_words = get_word_count(get_book_text("//home//zen//Desktop//Boot-dev_Projects///bookbot//books//frankenstein.txt"))
    print(f"Found {counted_words} total words")
    char_counts = get_char_count(get_book_text("//home//zen//Desktop//Boot-dev_Projects///bookbot//books//frankenstein.txt"))
    print(char_counts)

    ##get_char_count("Hello World!, This This world ")

main()
