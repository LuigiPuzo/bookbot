import sys
from stats import *

def main():

    try: 
        book = sys.argv[1]
    except:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    num_words = get_num_words(book)
    num_characters = get_num_characters(book)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book}...")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")
    sorted_dict = get_sorted_list(book)
    print ("============= END ===============")

if __name__ == "__main__":
    main()
    