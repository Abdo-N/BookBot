from typing import TypedDict

class CharacterCount(TypedDict):
    char: str
    num: int

def get_book_text(path: str):
    
    with open(path) as f:
        # do something with f (the file) here
        # f is a file object
        file_contents = f.read()
    
    return file_contents


def get_num_words(content: str):
    data = content.split() #now an array
    count = 0
    for word in data:
        count += 1
    return count

def get_char_count(content: str):
    output = {}

    for letter in content.lower():
        if letter in output:
            output[letter] += 1
        elif letter not in output:
            output[letter] = 1
    return output

def sort_char_count(char_count: dict) -> list[CharacterCount]:
    output: list[CharacterCount] = []
    
    for item,value in char_count.items():
        output.append({"char": item, "num": value})
        

    output.sort(reverse=True, key=sort_on)
    return output
    
def sort_on(charCount: CharacterCount):
    return charCount["num"]


def analyze(path):
    book = get_book_text(path)
    word_count = get_num_words(book)
    char_count = sort_char_count(get_char_count(book))


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}.")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in char_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item['num']}")

    print("============= END ===============")