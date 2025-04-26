import sys
from stats import num_of_words, character_appearance, sorted_char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print("Found", num_of_words(get_book_text(sys.argv[1])), "total words")
    print("--------- Character Count -------")
    sorted_char_dict(character_appearance(get_book_text(sys.argv[1])))
    print("============= END ===============")

if __name__ == "__main__":
    main()