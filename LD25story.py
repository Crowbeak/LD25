import time
from LD25simulate import *

def text(stringList):
    """
    Prints strings in list word with a 0.2 second time step between each string.
    """
    for i in stringList:
        print i
        time.sleep(0.2)

def sCredits():
    word = ['Made for Ludum Dare 25 by Lena LeRay.',
            'Theme: You Are the Villain',
            'Please play through to the end.',
            'You won\'t see how it connects to the theme if you stop early.']
    text(word)
    

def firstSim():
    word = ['\nAlright. May as well get started. The work isn\'t hard, but it IS',
            'tedious sometimes. Maybe this will be one of those days where',
            'rearranging robots to maximize farm and factory outputs seems more',
            'like a game [Ha~h!] than work. It\'s a bit too groggy in the day to',
            'say for sure yet.\n']
    text(word)


def instructions():
    word = ['\nYour job is to maximize the output of our nation\'s farms and',
            'factories by assigning labor robots to each appropriately. This',
            'usually coincides with assigning new robots to farm or factory',
            'positions and decommissioning old robots for parts.',
            '\nYou will run one or more simulations for a given farm/factory pair',
            'and use the results to decide which robots to decommission. You may',
            'run as few or as many simulations as you deem necessary.',
            '\nTIPS:',
            '----------',
            'When new robots are constructed, room must be made for them by',
            'decommissioning an equal number of robots.',
            '\nRobots with higher utility stats tend to be more useful in',
            'factories.',
            '\nRobots with higher carrying capacity tend to be more useful on',
            'farms.',
            '\nRemember: your job is very important. The parts and scrap from',
            'decommissioned robots is essential in these days of scarcity.',
            '\nDo your duty -- serve us all, and serve yourself!']
    text(word)


def intro():
    dave = ['\n\n"Good morning!"\n',
            'Dave is as cheerful as ever. Does he really not drink coffee?\n',
            '"I really don\'t drink coffee," he says with a grin.\n',
            'Before you can ask how he knew what you were thinki--\n',
            '"You\'ve asked me that question so many times now," he says, "that I',
            'can see it in your face."\n']
    text(dave)
    
    choice = 0
    while (int(choice) != 1) and (int(choice) != 2):
        print '\nWhat do you do?'
        time.sleep(0.2)
        print '1 - Grunt, wave goodbye, and go to your cubicle.'
        time.sleep(0.2)
        print '2 - Ask about his wife.'
    
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                grunt = ['\nDave laughs at you and calls out, "See you later!"',
                         '\nYou wave at a couple of other people on your way to your desk, and',
                         'plop down into your cushy chair as soon as you get there. You',
                         'don\'t realize until you\'ve already turned your computer on that',
                         'you were so annoyed with Dave you didn\'t get any coffee.\n',
                         'Damnation.\n']
                text(grunt)
            elif int(choice) == 2:
                wife = ['\nDave blabbers on happily about her newest hobby for a few minutes',
                        'while you get your sweet, sweet coffee. Unsweetened. Black. It\'s sweet',
                        'in that you really, really wanted-- ah, forget it, you know what I',
                        'mean. Anyway, you take your coffee to your desk, plop down into',
                        'your cushy chair, and turn on the computer.\n']
                text(wife)
            else:
                print '\nCome on, now. I know you haven\'t had your coffee yet, but surely you'
                time.sleep(0,2)
                print 'can find the 1 and 2 buttons on your keyboard.'
        except ValueError:
            choice = ord(choice)
            print '\nCome on, now. I know you haven\'t had your coffee yet, but surely you'
            time.sleep(0.2)
            print 'can find the 1 and 2 buttons on your keyboard.'

def loggedIn():
    print 'After logging in, you consider your options.'
    time.sleep(0.2)
    print '\nWhat do you do?'
    time.sleep(0.2)
    
    #Goof off or work.
    nosebook = False
    email = False
    while True:
        print '1 - See what\'s happening on Nosebook.'
        time.sleep(0.2)
        print '2 - Check your email.'
        time.sleep(0.2)
        print '3 - Do the work they\'re paying you to be here for.'
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                if nosebook:
                    print '\nYeah... still a lot of nosebook-picking going on here.'
                else:
                    nbok = ['\nAsh is talking about how boring it is to be a fireman. Again.',
                            'The hot newcomer on floor 3 is...',
                            'Excited about the newest Sunset book?',
                            'Ugh. Maybe "hot" isn\'t the right adjective. Moving on.',
                            'Dave is also picking his nosebook.',
                            'Alright, screw this.']
                    text(nbok)
                    nosebook = True
            elif int(choice) == 2:
                if email:
                    print '\nNo new email. Alas.'
                else:
                    print '\nEarlobe enlargement? Wow, they\'ll try anything these days.'
                    email = True
            elif int(choice) == 3:
                #Working.
                firstSim()
                
                while True:
                    print '\nWhat do you do?'
                    time.sleep(0.2)
                    print '1 - Review the manual again to stave off the inevitable.'
                    time.sleep(0.2)
                    print '2 - Just do it.'
                    time.sleep(0.2)
                    
                    choice = raw_input("Pick one:")
                    try:
                        if int(choice) == 1:
                            instructions()
                        elif int(choice) == 2:
                            runSim(10, 2, '#135466')
                            break
                        else:
                            print 'Try again, please. Invalid input.'
                    except ValueError:
                        choice = ord(choice)
                        print 'Try again, please. Invalid input.'
                break
            else:
                print '\nNo, no, no, that\'s not a valid choice. Try again!'
        except ValueError:
            choice = ord(choice)
            print '\nNo, no, no, that\'s not a valid choice. Try again!'
        
        print '\nWhat do you do next?'

def lunch():
    wrd1 = ['You yawn and stretch. Coffee time is past. It\'s snack time now.',
            '\nWhoops!',
            '\n Apparently you meant lunch time.']
    text(wrd1)
    
    choice = 0
    while (int(choice) != 1) and (int(choice) != 2) and (int(choice) != 3):
        chc1 = ['\nWhere do you want to go?',
                '1 - The good old cafeteria. Mediocre free food, decent conversation.',
                '2 - Home. Sandwiches and solitude.']
        text(chc1)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                cafe = ['\nYou mosey your way down to the first floor. Dave has beaten you',
                        'there and is sitting with Biggs and Wedge at a table smack dab in the',
                        'middle of the room. You grab a tray of food and \'wedge\' yourself in',
                        'between the two \'bigg\' guys.',
                        '\nYou quickly regret your punny decision when Wedge slaps you on the',
                        'back. At least he\'s gentler than usual. Maybe you\'ll just have a',
                        'bruise this time.',
                        '"Hey, man! =D" he says. He\'s got one of those silly emoticon things',
                        'embedded in his forehead to make sure you see the smiley face. Real',
                        'friendly guy, but he doesn\'t always make the best decisions. Biggs,',
                        'his brother, just smiles and waves. He has all the brains his brother',
                        'missed out on, but he\'s a good guy, too.']
                text(cafe)
            elif int(choice) == 2:
                home =
                text(home)
            else:
                print '\nYou... where?!'
        except ValueError:
            choice = ord(choice)
            print '\nYou... where?!'