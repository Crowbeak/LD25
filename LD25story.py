from LD25simulate import *

def sCredits():
    print "Made for Ludum Dare 25 by Lena LeRay."
    print "Theme: You Are the Villain"
    print "Please play through to the end."
    print "You won't see how it connects to the theme if you stop early."
    

def firstSim():
    print '\nAlright. May as well get started. The work isn\'t hard, but it IS'
    print 'tedious sometimes. Maybe this will be one of those days where'
    print 'rearranging robots to maximize farm and factory outputs seems more'
    print 'like a game [Ha~h!] than work. It\'s a bit too groggy in the day to'
    print 'say for sure yet.\n'


def instructions():
    print '\nYour job is to maximize the output of our nation\'s farms and'
    print 'factories by assigning labor robots to each appropriately. This'
    print 'usually coincides with assigning new robots to farm or factory'
    print 'positions and decommissioning old robots for parts.'
    print '\nYou will run one or more simulations for a given farm/factory pair'
    print 'and use the results to decide which robots to decommission. You may'
    print 'run as few or as many simulations as you deem necessary.'
    print '\nTIPS:'
    print '----------'
    print 'When new robots are constructed, room must be made for them by'
    print 'decommissioning an equal number of robots.'
    print '\nRobots with higher utility stats tend to be more useful in'
    print 'factories.'
    print '\nRobots with higher carrying capacity tend to be more useful on'
    print 'farms.'
    print '\nRemember: your job is very important. The parts and scrap from'
    print 'decommissioned robots is essential in these days of scarcity.'
    print '\nDo your duty -- serve us all, and serve yourself!'


def intro():
    print '\n\n"Good morning!"\n'
    print 'Dave is as cheerful as ever. Does he really not drink coffee?\n'
    print '"I really don\'t drink coffee," he says with a grin.\n'
    print 'Before you can ask how he knew what you were thinki--\n'
    print '"You\'ve asked me that question so many times now," he says, "that I'
    print 'can see it in your face."\n'
    
    choice = 0
    while (int(choice) != 1) and (int(choice) != 2):
        print '\nWhat do you do?'
        print '1 - Grunt, wave goodbye, and go to your cubicle.'
        print '2 - Ask about his wife.'
    
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                print '\nDave laughs at you and calls out, "See you later!"'
                print '\nYou wave at a couple of other people on your way to your desk, and'
                print 'plop down into your cushy chair as soon as you get there. You'
                print 'don\'t realize until you\'ve already turned your computer on that'
                print 'you were so annoyed with Dave you didn\'t get any coffee.\n'
                print 'Damnation.\n'
            elif int(choice) == 2:
                print '\nDave blabbers on happily about her newest hobby for a few minutes'
                print 'while you get your sweet, sweet coffee. Unsweetened. Black. It\'s sweet'
                print 'in that you really, really wanted-- ah, forget it, you know what I'
                print 'mean. Anyway, you take your coffee to your desk, plop down into'
                print 'your cushy chair, and turn on the computer.\n'
            else:
                print '\nCome on, now. I know you haven\'t had your coffee yet, but surely you'
                print 'can find the 1 and 2 buttons on your keyboard.'
        except ValueError:
            choice = ord(choice)
            print '\nCome on, now. I know you haven\'t had your coffee yet, but surely you'
            print 'can find the 1 and 2 buttons on your keyboard.'

def loggedIn():
    print 'After logging in, you consider your options.'
    print '\nWhat do you do?'
    
    #Goof off or work.
    nosebook = False
    email = False
    while True:
        print '1 - See what\'s happening on Nosebook.'
        print '2 - Check your email.'
        print '3 - Do the work they\'re paying you to be here for.'
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                if nosebook:
                    print '\nYeah... still a lot of nosebook-picking going on here.'
                else:
                    print '\nAsh is talking about how boring it is to be a fireman. Again.'
                    print 'The hot newcomer on floor 3 is...'
                    print 'Excited about the newest Sunset book?'
                    print 'Ugh. Maybe "hot" isn\'t the right adjective. Moving on.'
                    print 'Dave is also picking his nosebook.'
                    print 'Alright, screw this.'
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
                    print '1 - Review the manual again to stave off the inevitable.'
                    print '2 - Just do it.'
                    
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