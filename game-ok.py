from random import randint
num = randint(1,100)
bingo = False
print'Guess what I think?'

while bingo != True:
    answer = input()
    
    if answer<num:
        print 'Too Small!'
    
    if answer > num:
        print 'Too Bit!'


    if answer==num:
        print 'Equal!'
        bingo = True


