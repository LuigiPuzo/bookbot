from stats import *

def main():
    #print("Starting the book reader...")
    #num_words = get_num_words('books/frankenstein.txt')
    #print (f"{num_words} words found in the document")
    #print("counting characters")
    num_characters = get_num_characters('books/frankenstein.txt')
    print (num_characters)
    #dump_text('books/frankenstein.txt')
if __name__ == "__main__":
    main()
    