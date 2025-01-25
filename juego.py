import random
import os

def run():
    IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    DB = [
        "manzana",
        "pera",
        "melon",
        "durazno",
        "mango",
        "pineapple",
        "watermelon"
    ]        

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 0
 
    while True:
        os.system("cls")
        print("\tDescrubre la fruta\n")
        print(IMAGES[attemps])
        for characters in spaces:
            print(characters, end = " ")
        letter = input("\n\nEscriba una letra ")
        
        foun=False
        for idx, characters in enumerate(word):
            if characters == letter:
                spaces[idx] = letter
                foun = True
        
        if not foun:
            attemps +=1

        if "_" not in spaces:
            os.system("cls")
            print("\t********\n")
            print("\tGANASTE\n")
            print("\t :D \n")
            print("\t********")
            break
            input()

        if attemps==6:
            os.system("cls")
            print("\t********\n")
            print("\tPERDISTE\n")
            print("\t :( \n")
            print("\t*******")
            break
            input()        

if __name__ == '__main__':
    run()