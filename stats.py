def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# def get_char_count(words_from_book):
#     char_count = dict()
#     ##num = 0
#     ## words_from_book = words_from_book.lower().split()
#     words_from_book = words_from_book.lower()
#     for j in words_from_book:
#         ##num = 0
#         for i in j:
#             if i in char_count:
#                 char_count[i] = char_count.get(i) + 1
#             else:
#                 char_count[i] = 1
        
    
            
def get_char_count(words_from_book):
    char_count = dict()
    for char in words_from_book.lower():
        char_count[char] = char_count.get(char, 0) + 1     
    return char_count


# from boots more elegant and right solution 
# def get_char_count(text):
#     counts = {}
#     for c in text.lower():
#         counts[c] = counts.get(c, 0) + 1
#     return counts

def get_word_count(file_content):
    book_text = file_content.split()
    total_count:int = 0
    for i in book_text:
        total_count += 1
    return total_count