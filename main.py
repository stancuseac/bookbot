def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # print(file_contents)
    print(count_words(file_contents))

def count_words(text):
    count = 0
    split_text = text.split()
    for _ in split_text:
        count += 1
    return count

if __name__=="__main__":
    main()
