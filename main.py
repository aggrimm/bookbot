from stats import wordct, charct

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main(filepath):
    text = get_book_text(filepath)
    num_words = wordct(text)
    print(f"{num_words} words found in the document")
    cdict = charct(text)
    print(cdict)

main("books/frankenstein.txt")