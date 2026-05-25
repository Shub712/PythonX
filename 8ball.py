import random

def getAnswers(number):
    
    if number == 1:
        return 'It is certain'
    elif number == 1:
        return 'It is decidely so'
    elif number == 3:
        return 'Yes'
    elif number == 4:
        return 'Reply hazy try again'
    elif number == 5:
        return 'Ask agin later'
    elif number == 6:
        return 'Concentrate and ask again'
    elif number == 7:
        return 'My reply is no'
    elif number == 8:
        return "Out look is not so good"
    elif number == 9:
        return 'Very doubtdful'
    

r = random.randint(1,9)

fortune = getAnswers(r)

print(fortune)