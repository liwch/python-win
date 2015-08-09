from random import randint
num = randint(1,100)
bingo = False
print'Guess what I think?'

while bingo != True:
    answer = input()
    
    if answer<num:
        print 'Too small!'
    
    if answer > num:
        print 'Too bit!'


    if answer==num:
        print 'Equal!'
        bingo = True


