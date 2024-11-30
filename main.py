import string

def main():
    bookpath = "/home/bubbledev/workspace/github.com/bookbot/books/frankenstein.txt"
    total = 0
    text = getText(bookpath)
    count = getWordsCount(text)
    lowertext = lowercase(text)
    dic_count = {letter: 0 for letter in string.ascii_lowercase}
    for char in lowertext :
        if char.isalpha():
            dic_count[char] += 1
            total += 1
    print(f"{total} words found in the document")
    for letter, data in dic_count.items():
        print(f"'{letter}' character was found {data} times ")
    print("--- End report ---")
            

    




def getText(path):
    with open(path) as f:
        return f.read()

def getWordsCount(texts):
    splits = texts.split()
    return len(splits)

def lowercase(xx):
    lowered = xx.lower()
    return lowered

main()
