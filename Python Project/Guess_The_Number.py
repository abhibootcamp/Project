import random
def guess_user():
    x = 1000
    random_num = random.randint(1,x)
    life = 10
    guess = int(input(f"Enter Number in the range from 1 to {x} and you have {life} life.\n"))
    life -= 1
    while guess > 1000 or guess < 1:
        print("Please Enter a Valid Number")
        guess = int(input(f"Enter Number in the range from 1 to {x} and you have {life} life.\n"))
    while guess != random_num and life > 0:
        if guess > random_num :
            guess = int(input(f"Too High! Enter Number in the range from 1 to {x} and you have {life} life.\n"))
            life -= 1
            while guess > 1000 or guess < 1:
                print("Please Enter a Valid Number")
                guess = int(input(f"Enter Number in the range from 1 to {x} and you have {life} life.\n"))
        elif guess < random_num :
            guess = int(input(f"Too Low! Enter Number in the range from 1 to {x} and you have {life} life.\n"))
            life -= 1
            while guess > 1000 or guess < 1:
                print("Please Enter a Valid Number")
                guess = int(input(f"Enter Number in the range from 1 to {x} and you have {life} life.\n"))
    if (life == 0 and guess!= random_num) :
        print(f"Sorry! You Lost the Game!. Correct Number is {random_num}")
    else:
        print(f'Congratulation! You Won. You guess it Right {random_num} , and you have {life + 1} points.')
        
if __name__ == '__main__':    
    guess_user()