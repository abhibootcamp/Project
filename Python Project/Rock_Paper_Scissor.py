import random
def rock_paper_scissor():
    user = input(f'Enter \'R\' for Rock.\nEnter \'P\' for Paper.\nEnter \'S\' for Scissors.\n')
    computer = random.choice(['R','P','S'])
    if user == computer:
        print("Game is Tie")
    elif (user =='R' and computer =='S') or (user =='S' and computer =='P') or (user =='p' and computer =='R'):
        print("Congratulation! You Won.")
    else:
        print("Sorry You Lost. Computer Won!")

if __name__ == '__main__':
    rock_paper_scissor()