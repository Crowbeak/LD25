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
                    chc1 = ['\nWhat do you do?',
                            '1 - Review the manual again to stave off the inevitable. [How to Play]',
                            '2 - Just do it.']
                    text(chc1)
                    
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
            '\nApparently you meant lunch time.']
    text(wrd1)
    
    choice = 0
    while (int(choice) != 1) and (int(choice) != 2):
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
                        '\n"Hey, man! =D" he says. He\'s got one of those silly emoticon things',
                        'embedded in his forehead to make sure you see the smiley face. Real',
                        'friendly guy, but he doesn\'t always make the best decisions. Biggs,',
                        'his brother, just smiles and waves. He has all the brains his brother',
                        'missed out on, but he\'s a good guy, too. Quieter, though, and',
                        'stronger. Wouldn\'t want to be against him in a fight.',
                        '\nYou guys shoot the sheep around the table for about 20 minutes',
                        'before Dave\'s wife calls and completely diverts his attention. Wedge',
                        'uses that as an excuse to "go to the bathroom", by which he means hit',
                        'on one of the new employees a few tables away.',
                        '\nYou and Biggs idly watch the news on a nearby monitor. More',
                        'terrorist activity. Has it been on the rise, lately? Ah, who cares.',
                        'After a while, the sensationalist headlines all blur together.',
                        '\nWedge comes back before Dave -- no surprise there -- and you guys',
                        'go back to talking about... uh.. what were you talking about? Must',
                        'not have been important.']
                text(cafe)
            elif int(choice) == 2:
                home = ['\nYou barely catch Dave before he rockets downstairs to let him know',
                        'that you\'ll be ducking out on the crew for lunch. After asking him',
                        'to give your regards to Biggs and Wedge, you grab your jacket and',
                        'head home.',
                        '\nIt\'s nice to live within walking distance of work, isn\'t it? Even',
                        'with the quality of mass transportation here, there\'s something',
                        'about walking that feels nicer. Especially after long hours in a',
                        'chair staring at robot output simulations.',
                        '\nThe house is quiet when you get home. It always is. Maybe you could',
                        'get a cat? You flip on the TV before rummaging through the fridge.',
                        '\nAh, crap... no sandwich meat. Grilled cheese it is, then.',
                        '\nThe news is showing on TV at the moment. You can\'t make out all of',
                        'what\'s being said over the sizzling skillet, but apparently it\'s all',
                        'about terrorists. But then, it always is, these days. The same old',
                        'headlines are starting to get kind of old.',
                        '\nYou plop down on your couch and eat your delicious, delicious',
                        'grilled goodness. Unfortunately, you forget to change the channel',
                        'BEFORE you grab your greasy sandwich. You manage to finish the',
                        'sandwich and clean the remote with just enough time to get back to',
                        'work on time. And there was much rejoicing. Yaaaaaay.']
                text(home)
            else:
                print '\nYou... wait, what?! Try that again.'
        except ValueError:
            choice = ord(choice)
            print '\nYou... wait, what?! Try that again.'
            

def loggedIn2():
    print 'You log in. Confronted with the usual options...'
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
        print '3 - Work. Maybe it\'ll take your mind off things.'
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                if nosebook:
                    print '\nEven scoffing at the nosebook-picking can\'t cheer you up.'
                    time.sleep(0.2)
                    print 'The term "nosebook-picking" isn\'t even funny right now.'
                else:
                    nbok = ['\nAsh is talking about how awesome it is to be a fireman. Again.',
                            'Wedge renamed his cat? What the hell?',
                            'Everyone thinks the new Kumoman is better than the last one.',
                            'Didn\'t the last one only come out like five years ago?',
                            'Neither Dave nor his wife have posted anything since yesterday.',
                            'This isn\'t helping.']
                    text(nbok)
                    nosebook = True
            elif int(choice) == 2:
                if email:
                    print '\nNo new email. Not that you did a good job reading the first two.'
                else:
                    print '\nSomething from Biggs about a party... don\'t care right now.'
                    time.sleep(0.2)
                    print 'And... news. Never really care about that.'
                    email = True
            elif int(choice) == 3:
                #Working.
                while True:
                    print '\nWhat do you do?'
                    time.sleep(0.2)
                    print '1 - Review the manual again.'
                    time.sleep(0.2)
                    print '2 - Work. Or try to.'
                    time.sleep(0.2)
                    
                    choice = raw_input("Pick one:")
                    try:
                        if int(choice) == 1:
                            instructions()
                        elif int(choice) == 2:
                            runSim(18, 4, '#187949')
                            break
                        else:
                            print 'Try again, please. Invalid input.'
                    except ValueError:
                        choice = ord(choice)
                        print 'Try again, please. Invalid input.'
                break
            else:
                print '\nI know you\'re distracted, but please use proper input.'
        except ValueError:
            choice = ord(choice)
            print '\nI know you\'re distracted, but please use proper input.'
        
        print '\nWhat do you do next?'


def loggedIn3():
    print 'You log in. Confronted with the usual options...'
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
                    print '\nMore nosebook-picking. Ah, nosebook-picking.'
                    time.sleep(0.2)
                    print 'Just the term makes you happy. How do you visualize that?'
                else:
                    nbok = ['\nAsh is talking about how awesome it is to be a fireman. Again.',
                            'Wedge renamed his cat? What the hell?',
                            'Everyone thinks the new Kumoman is better than the last one.',
                            'Didn\'t the last one only come out like five years ago?',
                            'Neither Dave nor his wife have posted anything since yesterday.',
                            'I should probably work. Probably.']
                    text(nbok)
                    nosebook = True
            elif int(choice) == 2:
                if email:
                    print '\nNo new email. Who\'s surprised?'
                else:
                    print '\nSomething from Biggs about a party... don\'t care right now.'
                    time.sleep(0.2)
                    print 'And... news. Never really care about that.'
                    email = True
            elif int(choice) == 3:
                #Working.
                while True:
                    print '\nWhat do you do?'
                    time.sleep(0.2)
                    print '1 - Review the manual again.'
                    time.sleep(0.2)
                    print '2 - Work! It\'s like a crummy party you get paid to attend.'
                    time.sleep(0.2)
                    
                    choice = raw_input("Pick one:")
                    try:
                        if int(choice) == 1:
                            instructions()
                        elif int(choice) == 2:
                            runSim(18, 4, '#187949')
                            break
                        else:
                            print 'Try again, please. Invalid input.'
                    except ValueError:
                        choice = ord(choice)
                        print 'Try again, please. Invalid input.'
                break
            else:
                print '\nYou got coffee in peace today and still can\'t input numbers?'
        except ValueError:
            choice = ord(choice)
            print '\nYou got coffee in peace today and still can\'t input numbers?'
        
        print '\nWhat do you do next?'


def friends():
    """
    Returns True if Dave is still in player's life at end of module or False
    otherwise.
    """
    word = ['\nTime passes. Universes are born and die.',
            '\nOkay, so that much time hasn\'t actually passed. But the days do',
            'wear on. Romance still isn\'t going that great, but you got a ferret',
            'to keep you company. Didn\'t think too much about the smell before',
            'making that purchase, but... too late now, and you like the little',
            'guy. He\'s a lot more interesting than a cat. And you never wake up',
            'with his butt in your face like Wedge complains about with his cat.',
            '\nYou\'re already to your desk and pushing the power button on your',
            'computer when you realize Dave wasn\'t in the kitchen this morning.',
            '\nWeird. Wanna look into that?']
    text(word)
    
    choice = 0
    while (int(choice) != 1) and (int(choice) != 2):
        chc1 = ['\n1 - Yeah... that\'s so out of character I can only assume aliens',
                '    are involved.',
                '2 - Nah. Dave\'s a great guy but it\'s nice not to have to deal',
                '    with his peppy peppiness sometimes.']
        text(chc1)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                dave = True
                look = ['\nIt doesn\'t take you long to find him. He\'s sitting at his desk.',
                        'Dave\'s not his usual, bubbly self, though. He\'s staring so hard at',
                        'his screen, leaning forward on his elbows, that he doesn\'t even',
                        'hear you say good morning.',
                        '\nSomething is most definitely wrong. Dave saps that greeting up like',
                        'a tree does sunshine.',
                        '\nNeedless to say, he\'s startled when you tap his shoulder. He turns',
                        'to look at you and there are tears in his eyes. He turns back to the',
                        'computer to wipe his face off. You look away akwardly as you inquire',
                        'if something suddenly happened with his wife. (It would have had to',
                        'be VERY suddenly, because they were DEFINITELY on good terms when you',
                        'all went to see the newest Kumoman movie last night.)',
                        '\n"She\'s leaving me."',
                        '\nYou can\'t get a coherent account of what happened out of him, but',
                        'with a bit of work you convince him to go rest at your place. He',
                        'doesn\'t want you to go with him. After making him promise to call you',
                        'if he needs anything, you go to your desk and get to work. It\'s not',
                        'like you have anything better to do. Work will be a nice distraction.']
                text(look)
                loggedIn2()
                print '\nLunch time. You still haven\'t heard from Dave. Time to go check on him.'
                time.sleep(2)
            elif int(choice) == 2:
                dave = False
                print '\nYou sip your coffee obtained in quiet and log in.'
                loggedIn3()
                dont = ['\nAs soon as you finish the simulation, you hear a crash and screaming',
                        'coming from around the corner. When a gust of cold air brings the',
                        'sound of screeching tires and car horns with it, your stomach',
                        'plummets to your knees.',
                        '\nYou\'re one of the last to stick your head out into the aisle to look.',
                        'The hole in the glass -- 7 stories up -- is very, very close to Dave\'s',
                        'cubicle.']
                text(dont)
            else:
                print '\nDrink some of your coffee and try that again.'
        except ValueError:
            choice = ord(choice)
            print '\nDrink some of your coffee and try that again.'
    
    return dave
    
    
def trouble(dave):
    pass
            
    
def spanishInquisition():
    pass