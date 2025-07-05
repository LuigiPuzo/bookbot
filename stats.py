def get_num_words (filename):
    #print(f"Counting words in file: {filename}")
    wordcount = 0
    try:
        with open(filename, 'r') as file:
            text = file.read()
            for word in text.split():
                #print (word)
                wordcount+=1
            #print(wordcount)
            return wordcount
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

def get_num_characters(filename):
    character_dict = {}
    with open(filename, 'r') as file:
        text = file.read()
        for character in text:
            #print (character.lower())
            if character.lower() in character_dict:
                character_dict[character.lower()] += 1
            else:
                character_dict[character.lower()] = 1
    return character_dict

def dump_text(filename):
    with open(filename, 'r') as file:
        text = file.read()
        for word in text:
            print (word)
    return