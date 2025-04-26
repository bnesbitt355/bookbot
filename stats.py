def num_of_words(text):
    file_text = text

    split_text = file_text.split()

    word_count = len(split_text)

    return word_count

def character_appearance(text):
    character_counter = {}

    for char in text.lower():
        if char in character_counter:
            character_counter[char] += 1
        else:
            character_counter[char] = 1

    return character_counter

def sort_on(dict):
    return dict["num"]

def sorted_char_dict(dictionary):
    character_count = []
    
    for key, value in dictionary.items():
        single_char = {"char": key, "num": value}
        character_count.append(single_char)
    
    character_count.sort(reverse=True, key=sort_on)

    count = 0

    for item in character_count:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")



    
    
    

