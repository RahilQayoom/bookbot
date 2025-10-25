from stats import get_word_count, get_book_text


def main():
    counted_words = get_word_count(get_book_text("//home//zen//Desktop//Boot-dev_Projects///bookbot//books//frankenstein.txt"))
    print(f"Found {counted_words} total words")

main()
