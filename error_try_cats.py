print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        if int(numCats) <= 0:
            print('You dont have any cats.')
        else:
            print('That is not that many cats.')
except ValueError:
    print('You did not enter a number. ex. 1,2,3, etc...')
    
          
