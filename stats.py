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
        char_count[char] = char_count.get(char, 0 ) + 1     
    return char_count


# from boots more elegant and right solution 
# def get_char_count(text):
#     counts = {}
#     for c in text.lower():
#         counts[c] = counts.get(c, 0) + 1
#     return counts

 
def sort_on(items):
    return items["num"]
def get_sort_dict(dic):
    sorted_dict = dict()
    list_of_dict = list()
    for key in dic:
        if key.isalpha():

            sorted_dict = {"char": f"{key}", "num": dic[key]}
            list_of_dict.append(sorted_dict)
            sorted_dict = dict()
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict


def print_report(count_of_words,soretd_dic,path_to_file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {count_of_words} total words")
    print("--------- Character Count -------")
    
    ##for index, value in enumerate(soretd_dic):
        ##print(f"{soretd_dic[index]["char"]}: {soretd_dic[index]["num"]}")
    for dic in soretd_dic:
        print(f"{dic["char"]}: {dic["num"]}")
    print("============= END ===============")



def get_word_count(file_content):
    ##book_text = file_content.split()
    # just found out actually did not think about it i could just have used len() instead of using for loop do the counting !
     ##for i in book_text:
      ##  total_count += 1
    total_count:int = 0
    ##total_count = len(file_content.split())
    return len(file_content.split())