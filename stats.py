def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(file_content):
    book_text = file_content.split()
    total_count:int = 0
    for i in book_text:
        total_count += 1
    return total_count