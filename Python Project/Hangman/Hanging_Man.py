import random
from Words import words

def get_validate_word():
    word = random.choice(words)
    while '-' in word or ' ' in word :
        word = random.choice(words)
    return word.upper()

def hanging_man():
    word = get_validate_word()
    wordlist = set(word)
    used_letters = set()
    
    life = 10

    while life>0 and len(wordlist)>0 :
        guess_word = [letter if letter in used_letters else '-'  for letter in word]
        print('You used Letter',' '.join(used_letters))
        print(' '.join(guess_word))
        x = input(f'Enter a Letter, Your life is {life}\n').upper()
        while x in used_letters:
            print(f'You already use Letter {x}')
            x = input(f'Enter a Letter, Your life is {life}\n').upper()
        used_letters.add(x)

        if x in wordlist:
            wordlist.remove(x)
        else:
            life -= 1
        
    if life==0 :
        print(f'Sorry You didn\'t Guess Correct. Correct Word is {word}')
    if len(wordlist) == 0:
        print(f"Congratulation You Guess it Right {word}")



if __name__ == '__main__':
    hanging_man()