def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"{num_words} words in this document")
    print(count_characters(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    split_text = text.split()
    return len(split_text)

'''
def count_unique_words(text):
    split_text = text.lower().split()
    unique_counts = {}
    for word in split_text:
        if word in unique_counts:
            unique_counts[word] += 1
        else: 
            unique_counts[word] = 1
    print(unique_counts)
    # find out how to remove punctiation and sort the dictionary A-Z
'''

def count_characters(text):
    char_dict = {}
    for word in text:
        for char in word.lower():
            if char in char_dict:
                char_dict[char] += 1
            else: 
                char_dict[char] = 1
    return char_dict

if __name__=="__main__":
    main()
