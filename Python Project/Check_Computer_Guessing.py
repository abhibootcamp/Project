import random
def guess_computer():
    low = 1
    high = 1000
    random_num = random.randint(low,high)
    expression = input(f'Is Number {random_num}. If correct then Enter \'c\' , if Low then Enter \'l\' , if Hight then Enter \'h\'\n')
    cnt = 1
    while expression != 'c':
        if expression == 'l':
            low = random_num + 1
        elif expression == 'h':
            high = random_num + 1
        random_num = random.randint(low,high)
        expression = input(f'Is Number {random_num}. If correct then Enter \'c\' , if Low then Enter \'l\' , if Hight then Enter \'h\'\n')
        cnt += 1
    print(f'Computer Guess it right in {cnt} move. The correct No is {random_num}')
    

if __name__ == '__main__':
    guess_computer()    