def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = count_characters(text)
    sorted_list = sorted_letters_list(char_dict)
    print_report(book_path, num_words, sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    split_text = text.split()
    return len(split_text)

def count_characters(text):
    char_dict = {}
    for word in text:
        for char in word.lower():
            if char in char_dict:
                char_dict[char] += 1
            else: 
                char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sorted_letters_list(dict):
    listed_dict = []
    for key in dict:
        if key.isalpha():
            temp = {"char":key, "num":dict[key]}
            listed_dict.append(temp)
    listed_dict.sort(reverse=True, key=sort_on)
    return listed_dict

def print_report(book_path, word_count, character_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for key in character_list:
        temp_key = key["char"]
        temp_value = key["num"]
        print(f"The '{temp_key}' character was found {temp_value} times")
    print("\n--- End report ---")
    
if __name__=="__main__":
    main()
