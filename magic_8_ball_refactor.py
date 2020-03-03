import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        print('Reply Hazy Try Again')
        print('Try Again! Press Enter')
        input()
        return (getAnswer(random.randint(1,9)))
    elif answerNumber == 5:
        print('Ask again later')
        print('Try Again! Press Enter')
        input()
        return (getAnswer(random.randint(1,9)))
    elif answerNumber == 6:
        print('Concentrate and ask again')
        print('Try Again! Press Enter')
        input()
        return (getAnswer(random.randint(1,9)))
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

print('Think of a yes/no question and press enter to see the result')
input()
print(getAnswer(random.randint(1,9)))

    
    
