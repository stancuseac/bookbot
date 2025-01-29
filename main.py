def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = count_characters(text)
    #print(f"{num_words} words in this document")
    #print(char_dict)
    sorted_letters(char_dict)

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

def sorted_letters(dict):
    listed_dict = [num for x in dict]
    listed_dict.sort(reverse=False, key=sort_on)
    print(dict)

if __name__=="__main__":
    main()
