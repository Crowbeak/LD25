import time
from LD25display import printText
from LD25display import printFromFile
from LD25simulate import *
from classes import workclass


def instructions():
    """
    Displays the employee "manual", which is actually tips for playing.
    """
    printFromFile("resources/story/instructions.txt")


def intro():
    """
    The story introduction. Introduces Dave, has first story choice.
    
    Choices: 1
    Simulations: 0
    
    TODO: Have choice of asking about wife or not indicate interest or lack
          thereof in Dave's personal life. Eventually to impact ability to
          prevent Dave's suicide and its impact on the story.
    TODO: Make coffee intake a relevant stat somehow.
    """
    printFromFile("resources/story/intro/credits.txt")
    raw_input('\n(Press any key to continue)')
    printFromFile("resources/story/intro/good_morning_dave.txt")
    choice = 0
    again = ['\nCome on, now. I know you haven\'t had your coffee yet, but surely you',
            'can find the 1 and 2 keys on your keyboard.']
    while (int(choice) != 1) and (int(choice) != 2):
        menu = ['\nWhat do you do?',
                '1 - Grunt, wave goodbye, and go to your cubicle.',
                '2 - Ask about his wife.']
        printText(menu)
    
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                printFromFile("resources/story/intro/good_morning_dave_r1.txt")
            elif int(choice) == 2:
                printFromFile("resources/story/intro/good_morning_dave_r2.txt")
            else:
                printText(again)
        except ValueError:
            choice = 0
            printText(again)

def ch01():
    intro = ['\nAfter logging in, you consider your options.',
             '\nWhat do you do?']
    printText(intro)
    
    nosebook = False
    email = False
    again = ['\nNo, no, no, that\'s not a valid choice. Try again!']
    while True:
        menu = ['1 - See what\'s happening on Nosebook.',
                '2 - Check your email.',
                '3 - Do the work they\'re paying you to be here for.']
        printText(menu)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                if nosebook:
                    print '\nYeah... still a lot of nosebook-picking going on here.'
                else:
                    printFromFile("resources/story/ch01/ch01_nosebook.txt")
                    nosebook = True
            elif int(choice) == 2:
                if email:
                    print '\nNo new email. Alas.'
                else:
                    print '\nEarlobe enlargement? Wow, they\'ll try anything these days.'
                    email = True
            elif int(choice) == 3:
                printFromFile("resources/story/ch01/ch01_work.txt")
                while True:
                    menu = ['\nWhat do you do?',
                            '1 - Review the manual again to stave off the inevitable. [How to Play]',
                            '2 - Just do it.']
                    printText(menu)
                    
                    choice = raw_input("Pick one:")
                    try:
                        if int(choice) == 1:
                            instructions()
                        elif int(choice) == 2:
                            workplacesToBe = []
                            workplacesToBe.append(workclass.WorkplaceToBe(7, True, workclass.Farm,
                                                                          "FARM #216", "A216"))
                            workplacesToBe.append(workclass.WorkplaceToBe(5, True, workclass.Factory,
                                                                          "FACTORY #139", "C139"))
                            workplacesToBe.append(workclass.WorkplaceToBe(2, False, workclass.Unassigned,
                                                                          "UNASSIGNED", "NONE"))
                            runSim(workplacesToBe, 2, '#135466')
                            break
                        else:
                            print 'Try again, please. Invalid input.'
                    except ValueError:
                        choice = 0
                        print 'Try again, please. Invalid input.'
                break
            else:
                printText(again)
        except ValueError:
            choice = 0
            printText(again)
        
        print '\nWhat do you do next?'

    lunch = ['You yawn and stretch. Coffee time is past. It\'s snack time now.',
             '\nWhoops!',
             '\nApparently you meant lunch time.']
    printText(lunch)
    
    choice = 0
    again = ['\nYou... wait, what?! Try that again.']
    while (int(choice) != 1) and (int(choice) != 2):
        chc1 = ['\nWhere do you want to go?',
                '1 - The good old cafeteria. Mediocre free food, decent conversation.',
                '2 - Home. Sandwiches and solitude.']
        printText(chc1)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                printFromFile("resources/story/ch01/ch01_cafeteria.txt")
            elif int(choice) == 2:
                printFromFile("resources/story/ch01/ch01_home.txt")
            else:
                printText(again)
        except ValueError:
            choice = 0
            printText(again)
        
        raw_input('\n(Press any key to continue)')
            

def loggedIn2():
    intro = ['Confronted with the usual options...',
             '\nWhat do you do?']
    printText(intro)
    
    #Goof off or work.
    nosebook = False
    email = False
    while True:
        opts = ['1 - See what\'s happening on Nosebook.',
                '2 - Check your email.',
                '3 - Work. Maybe it\'ll take your mind off things.']
        printText(opts)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                if nosebook:
                    noseSeen = ['\nEven scoffing at the nosebook-picking can\'t cheer you up.',
                                'The term "nosebook-picking" isn\'t even funny right now.']
                    printText(noseSeen)
                else:
                    noseNew = ['\nAsh is talking about how awesome it is to be a fireman. Again.',
                               'Wedge renamed his cat? What the hell?',
                               'Everyone thinks the new Kumoman is better than the last one.',
                               'Didn\'t the last one only come out like five years ago?',
                               'Neither Dave nor his wife have posted anything since yesterday.',
                               'This isn\'t helping.']
                    printText(noseNew)
                    nosebook = True
            elif int(choice) == 2:
                if email:
                    print '\nNo new email. Not that you did a good job reading the first two.'
                else:
                    newEmail = ['\nSomething from Biggs about a party... don\'t care right now.',
                                'And... news. Noone cares about that.']
                    printText(newEmail)
                    email = True
            elif int(choice) == 3:
                #Working.
                while True:
                    workopts = ['\nWhat do you do?',
                                '1 - Review the manual again.',
                                '2 - Work. Or try to.']
                    printText(workopts)
                    
                    choice = raw_input("Pick one:")
                    try:
                        if int(choice) == 1:
                            instructions()
                        elif int(choice) == 2:
                            workplacesToBe = []
                            workplacesToBe.append(workclass.WorkplaceToBe(7, True, workclass.Farm,
                                                                          "FARM #10", "A010"))
                            workplacesToBe.append(workclass.WorkplaceToBe(5, True, workclass.Factory,
                                                                          "FACTORY #10", "C010"))
                            workplacesToBe.append(workclass.WorkplaceToBe(6, True, workclass.Factory,
                                                                          "FACTORY #12", "C012"))
                            workplacesToBe.append(workclass.WorkplaceToBe(4, False, workclass.Unassigned,
                                                                          "UNASSIGNED", "NONE"))
                            runSim(workplacesToBe, 4, '#187949')
                            break
                        else:
                            print 'Try again, please. Invalid input.'
                    except ValueError:
                        choice = 0
                        print 'Try again, please. Invalid input.'
                break
            else:
                print '\nI know you\'re distracted, but please use proper input.'
        except ValueError:
            choice = 0
            print '\nI know you\'re distracted, but please use proper input.'
        
        print '\nWhat do you do next?'


def loggedIn3():
    intro = ['Confronted with the usual options...',
             '\nWhat do you do?']
    printText(intro)
    
    nosebook = False
    email = False
    while True:
        opts = ['1 - See what\'s happening on Nosebook.',
                '2 - Check your email.',
                '3 - Do the work they\'re paying you to be here for.']
        printText(opts)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                if nosebook:
                    noseSeen = ['\nMore nosebook-picking. Ah, nosebook-picking.',
                                'Just the term makes you happy. How do you visualize that?']
                    printText(noseSeen)
                else:
                    noseNew = ['\nAsh is talking about how awesome it is to be a fireman. Again.',
                               'Wedge renamed his cat? What the hell?',
                               'Everyone thinks the new Kumoman is better than the last one.',
                               'Didn\'t the last one only come out like five years ago?',
                               'Neither Dave nor his wife have posted anything since yesterday.',
                               'You should probably work. Probably.']
                    printText(noseNew)
                    nosebook = True
            elif int(choice) == 2:
                if email:
                    print '\nNo new email. Who\'s surprised?'
                else:
                    newEmail = ['\nSomething from Biggs about a party... don\'t care right now.',
                                'And... news. Noone cares about that.']
                    printText(newEmail)
                    email = True
            elif int(choice) == 3:
                #Working.
                while True:
                    workopts = ['\nWhat do you do?',
                                '1 - Review the manual again.',
                                '2 - Work! It\'s like a crummy party you get paid to attend.']
                    printText(workopts)
                    
                    choice = raw_input("Pick one:")
                    try:
                        if int(choice) == 1:
                            instructions()
                        elif int(choice) == 2:
                            workplacesToBe = []
                            workplacesToBe.append(workclass.WorkplaceToBe(13, True, workclass.Farm,
                                                                          "FARM #87", "A087"))
                            workplacesToBe.append(workclass.WorkplaceToBe(5, True, workclass.Factory,
                                                                          "FACTORY #60", "C060"))
                            workplacesToBe.append(workclass.WorkplaceToBe(4, False, workclass.Unassigned,
                                                                          "UNASSIGNED", "NONE"))
                            runSim(workplacesToBe, 4, '#187949')
                            break
                        else:
                            print 'Try again, please. Invalid input.'
                    except ValueError:
                        choice = 0
                        print 'Try again, please. Invalid input.'
                break
            else:
                print '\nYou got coffee in peace today and still can\'t input numbers?'
        except ValueError:
            choice = 0
            print '\nYou got coffee in peace today and still can\'t input numbers?'
        
        print '\nWhat do you do next?'


def ch02():
    """
    Returns True if Dave is still in player's life at end of module or False
    otherwise.
    """
    intro = ['\nTime passes. Universes are born and die.',
             '\nOkay, so that much time hasn\'t actually passed. But the days do',
             'wear on. Romance still isn\'t going that great, but you got a ferret',
             'to keep you company. Didn\'t think too much about the smell before',
             'making that purchase, but... too late now, and you like the little',
             'guy. He\'s a lot more interesting than a cat. And you never wake up',
             'with his butt in your face like Wedge complains about with his cat.',
             '\nYou\'re already to your desk and pushing the power button on your',
             'computer when you realize Dave wasn\'t in the kitchen this morning.',
             '\nWeird. Wanna look into that?']
    printText(intro)
    
    choice = 0
    while (int(choice) != 1) and (int(choice) != 2):
        opts = ['\n1 - Yeah... that\'s so out of character I can only assume aliens',
                '    are involved.',
                '2 - Nah. Dave\'s a great guy but it\'s nice not to have to deal',
                '    with his peppy peppiness sometimes.']
        printText(opts)
        
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
                printText(look)
                loggedIn2()
                print '\nLunch time. You still haven\'t heard from Dave. Time to go check on him.'
                time.sleep(2)
            elif int(choice) == 2:
                dave = False
                print '\nYou sip your coffee obtained in quiet and log in.'
                loggedIn3()
                dontLook = ['\nAs soon as you finish the simulation, you hear a crash and screaming',
                            'coming from around the corner. When a gust of cold air brings the',
                            'sound of screeching tires and car horns with it, your stomach',
                            'plummets to your knees.',
                            '\nYou\'re one of the last to stick your head out into the aisle to look.',
                            'The hole in the glass -- 7 stories up -- is very, very close to Dave\'s',
                            'cubicle.']
                printText(dontLook)
            else:
                print '\nDrink some of your coffee and try that again.'
        except ValueError:
            choice = 0
            print '\nDrink some of your coffee and try that again.'
    
    raw_input('\n(Press any key to continue)')
    return dave
    
    
def loggedIn4():
    print '\nWhat do you do?'
    time.sleep(0.2)
    
    #Goof off or work.
    nosebook = False
    email = False
    while True:
        opts = ['1 - Pick your Nosebook.',
                '2 - Check your eternally uninteresting email.',
                '3 - Slave away.']
        printText(opts)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                if nosebook:
                    print '\nOh, why bother.'
                else:
                    noseNew = ['\nAsh is talking about how depressing it is to be a fireman. Again.',
                            'And... oh. Nosebook has reached a new low.',
                            'People are now posting pictures of themselves picking their noses.']
                    printText(noseNew)
                    nosebook = True
            elif int(choice) == 2:
                if email:
                    print '\nNo new email. Again.'
                else:
                    print '\nNothing.'
                    email = True
            elif int(choice) == 3:
                #Tries to work.
                uhoh = ['\nYou\'re about to type RUN when the door to the stairwell',
                        'bangs open. A troop of policeman run in, guns at the ready,',
                        'yelling and looking ready to shoot any and all of the employees',
                        'at the slightest provocation.',
                        '\nAnd they come straight to your desk.',
                        '"You\'re under arrest for criminal negligence tantamount to',
                        'treason," states the woman with a gun pointed directly at your',
                        'face. She says a lot of other things, too, but so quickly you',
                        'you don\'t quite understand.',
                        '\nAs they drag you away, the last thing you see is Dave gaping',
                        'at you from his cubicle entrance.']
                printText(uhoh)
                raw_input('\n(Press any key to continue)')
                break
            else:
                print '\nJust put in a correct input so you can get this done and go home.'
        except ValueError:
            choice = 0
            print '\nJust put in a correct input so you can get this done and go home.'
        
        print '\nWhat do you do next?'
    
    
def trouble(dave):
    if dave:
        intro = ['\nIt\'s been over three months and Dave is still a mess. At least',
                 'he\'s able to work, now. For a bit there it looked like he was going',
                 'to lose the job, too, which he definitely didn\'t need. You\'ve',
                 'been doing everything in your power to try to help him through',
                 'this, but there\'s only so much you can do. Staying up late to',
                 'console him or keep him company has really been a drain of late.',
                 '\nBut your ferret still loves you!',
                 '\nEven if he does keep ferreting your house keys away.',
                 '\nAfter making sure Dave gets back to his desk on time, you sit',
                 'down at your own. You really don\'t want to be here today, but',
                 'your choices are limited.',
                 '\nLimited to three.']
        printText(intro)
        loggedIn4()
    else:
        intro = ['\nA few minutes before lunch, Biggs drops by your desk.',
                 '\n"You gonna eat with us today?" he asks.',
                 '\nIt\'s been over three months since Dave threw his chair through',
                 'the glass and dived after it, but the memory of that gap and the',
                 'sounds of cars stopping suddenly still haunts you. Could you have',
                 'saved Dave? The therapist tells you not to blame yourself, but it\'s',
                 'still hard to face your mutual friends sometimes.']
        printText(intro)
        
        choice = 0
        while (int(choice) != 1) and (int(choice) != 2):
            opts = ['\nWill you eat with Biggs and Wedge today?',
                    '1 - Yeah.',
                    '2 - No.']
            printText(opts)
        
            choice = raw_input("Pick one:")
            try:
                if int(choice) == 1:
                    yeah = ['\nBigg grins. "Glad to hear it." He waves and walks off.',
                            '\nEven though you blamed yourself for Dave\'s death at the time,',
                            'your friends never did. They were a big help in getting you',
                            'back in good enough mental shape to at least be able to work.',
                            'You\'re always in a slightly better mood after hanging out with',
                            'them.',
                            '\nYou get to the cafeteria first, for once, and on a whim you pick',
                            'that table in the middle Dave always seemed to like. Biggs and',
                            'Wedge show up a few minutes later, and you all talk about that',
                            'sporting event that happened last night.',
                            '\nEveryone in the cafeteria is surprised when all the doors bust',
                            'open at once. A troop of policeman run in, guns at the ready,',
                            'yelling and looking ready to shoot any and all of the employees',
                            'at the slightest provocation.',
                            '\nThey examine everyone\'s faces one at a time, comparing their',
                            'faces to a picture. No one seems to match.',
                            '\nThen they come to you.',
                            '\n"You\'re under arrest for criminal negligence tantamount to',
                            'treason," states the woman with a gun pointed directly at your',
                            'face. She says a lot of other things, too, but so quickly you',
                            'you don\'t quite understand.',
                            '\nAs they drag you away, everyone is gaping in shock.']
                    printText(yeah)
                    raw_input('\n(Press any key to continue)')
                elif int(choice) == 2:
                    nope = ['\nBiggs nods a little sadly. "If you change your mind..."',
                            '\nYou thank him politely and he leaves. He and Wedge don\'t seem',
                            'to blame you for Dave\'s death at all, and they keep trying to',
                            'drag you out of your personal misery. It\'s great of them, and',
                            'usually you really appreciate it but some days...',
                            '\nYou just want to be alone.',
                            '\nYou walk to your apartment, ignoring the almost leafless trees.',
                            'When you arrive, your ferret greets you. Plopping him on your',
                            'shoulder, you rummage through the fridge. No sandwich meat',
                            'again. You take the bread and cheese to the couch and eat them',
                            'cold and plain.',
                            '\nYou\'re almost done eating when the doorbell rings. Wondering',
                            'who it could be, you check the peephole. It\'s a police officer.',
                            'You open the door, but before you can even finish saying hello,',
                            'there are what seems like a hundred guns pointed at your face.']
                    printText(nope)
                    raw_input('\n(Press any key to continue)')
                else:
                    print '\nSimple question. He\'s just asking.'
            except ValueError:
                choice = 0
                print '\nSimple question. He\'s just asking.'
        
    
def spanishInquisition():
    intro = ['\nBy the time you\'re taken before a judge, you\'ve been in police',
             'custody for... a while. You\'re not sure how long. The way they\'ve',
             'been treating you, it just feels like... too long.',
             '\nMuch to your dismay, you\'re not taken to a courtroom. You get to',
             'sit down, but it\'s across a table from a judge in what looks like an',
             'informal meeting room.',
             '\n"Have you anything to say in your defense?" he asks simply.']
    printText(intro)
    
    choice = 0
    while (int(choice) != 1) and (int(choice) != 2):
        opts = ['\nWell, do you?',
                '1 - I still don\'t understand what I\'m supposed to have done.',
                '2 - Would it matter if I did?']
        printText(opts)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                pass
            elif int(choice) == 2:
                question = ['\n"It wouldn\'t change the verdict," he replied, "but it',
                            'could affect your sentence."',
                            '\nHe doesn\'t stop there.']
                printText(question)
            else:
                print '\n"Have you anything to say in your defense?" he asks again.'
        except ValueError:
            choice = 0
            print '\n"Have you anything to say in your defense?" he asks again.'
    
    cont = ['\n"The evidence against you is clear. Government records indicate that',
            'you made the decision to decommission this robot," he says, pointing',
            'to the document in question. "Do you deny it?"',
            '\nThe documents appear to be in order. Your name and employee ID are',
            'attached to it... and a very, very good robot was marked for',
            'decommissioning. You would never decommission such a good robot, but',
            'you haven\'t been at your best lately. It could have been a typo.',
            '\nThe judge shakes his head. "By the power vested in me by the',
            'government of our nation, I hereby declare you guilty. Your',
            'punishment is demotion to labor so that you can attempt to make up',
            'for lost production."',
            '\nWhat does THAT mean?',
            '\nThe judge\'s parting wishes, clearly sincere, are not comforting.',
            '\n"I wish you the best in your new life."']
    printText(cont)
    raw_input('\n(Press any key to continue)')
    
    cont2 = ['\nA sharp jolt rouses you. You\'re in a vehicle of some kind, travelling',
             'down the absolute bumpiest road you\'ve ever encountered in your life.',
             'As you raise your head, a policeman sitting across from you turns and',
             'yells towards the front of the vehicle.',
             '\n"He\'s awake, sarge."',
             '\n"Damn," comes a muffled voice, "I was looking forward to waking him',
             'myself."',
             '\nYour mouth feels funny. When you try to lift your hands to feel it, you',
             'discover that your hands are chained to the floor. There are straps',
             'holding you up against the wall of the vehicle, and you couldn\'t reach',
             'the buckles to make an escape attempt if you tried.']
    
    cont3 = ['\nThe discomfort of your mouth and your grogginess are making it hard to',
             'process much, but you\'re slowly becoming more aware of your surroundings.',
             'While you\'re opening and closing your mouth to test it out -- your jaw',
             'seems to be working fine, but your tongue is just not with the program --',
             'another policeman sits next to the first opposite you.',
             '\n"Hmm," he says. "Don\'t see eyes that color often out here. He\'ll be',
             'good breeding stock."',
             '\n"I dunno, sir," replied the first man. "He seems kinda scrawny to me."',
             '\n"Yeah, but genetic diversity is important, too."',
             '\nAre they... are they seriously discussing you as if you were livestock?',
             '\nApparently the \'sarge\' notices your reaction. The smile he gives',
             'in response is NOT a friendly one.']
    
    cont4 = ['"All right, then," the sargeant says, addressing you directly. "here\'s',
             'your orientation. You are the newest \'robot\' on farm #512. This," he',
             'continues, attaching something to your wrist, "is your ID bracelet. It',
             'contains all your data -- your ID number and your stats. The stats are:',
             'your \'age\', or years in labor service; the amount you can carry in',
             'tens of pounds; your \'battery life\', or how many hours of work we can',
             'get out of you in a day; your utility rating, which is assigned by',
             'sargeants like myself; how much it costs us to feed you; and the number',
             'of times you\'ve gotten sick or injured -- \'broken down\'."',
             '\n"Your performance is closely monitored and evaluated on a regular',
             'basis, especially when new \'robots\' become operational."',
             '\nHe grins, and this time it looks downright nasty. "Oh yeah... you',
             'already know that part."',
             '\n"Now, this is where I normally tell new \'bots that if they work long',
             'and hard enough, they might get to join proper society. But I think you',
             'know that society class folk like your-former-self believe the farms',
             'and factories are worked by actual robots. So I won\'t insult you with',
             'that pep talk."',
             '\n"Any questions?"']
            
    printText(cont2)
    raw_input('\n(Press any key to continue)')
    printText(cont3)
    raw_input('\n(Press any key to continue)')
    printText(cont4)
    
    choice = 0
    again = ['\n"What\'s that?" he asks. I can\'t hear you."',
             '\nHis subordinate snickers.']
    while (int(choice) != 1) and (int(choice) != 2):
        opts = ['1 - You\'re kidding, right? You can\'t be serious.',
                '2 - Say nothing.']
        printText(opts)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                talk = ['\nYou try to respond, but only gibberish comes out of your mouth.',
                        '\nThe two men laugh.',
                        '\n"I love watching the ones with their tongues out try to talk,"',
                        'says the sargeant."']
                printText(talk)
            elif int(choice) == 2:
                dontTalk = ['\nAfter waiting for several moments with one eyebrow cocked, the',
                            'sargeant clicks his tongue and makes a face.',
                            '\n"Damn," he says, "I like it when the ones with their tongues out',
                            'try to talk.']
                printText(dontTalk)
            else:
                printText(again)
        except ValueError:
            choice = 0
            printText(again)
    
    cont5 = ['\n"Anyway," he goes on, "Your tongue has been removed to prevent you from',
             'trying to tell any of your fellow laborers about the fact that no one',
             'in society knows they exist. You will be watched, and if you look like',
             'you\'re even thinking about trying to communicate what you know to the',
             'native laborers, you will be punished. Nor may you attempt to teach',
             'them to read or write."',
             '\n"Do I make myself clear?" he asks.',
             '\nUnable to do anything else, you nod.']
            
    cont6 = ['\nThe vehicle makes a turn and slows to a stop.',
             '\nThe policemen bundle you out of the car and shove you to your knees in the',
             'mud before undoing your wrists. When your eyes adjust to the light and',
             'catch up to your nose, you can see that the horrible smell is animal dung',
             'strewn about the yard.',
             '\nThe sargeant points to a solitary goat in one corner.',
             '\n"That goat is your charge until you\'re told otherwise."',
             '\nHe then points to a girl nearby.',
             '\n"She\'ll teach you everything you need to know." He grins another one of',
             'his horrible grins. "You\'d best learn quickly. Your utility stat depends',
             'on it."',
             '\nThe girl comes over to help you up, smiling, as the policemen drive away.',
             '\nIf none of this had happened to you, would her fate have been in your',
             'hands tomorrow?']
    
    printText(cont5)
    raw_input('\n(Press any key to continue)')
    printText(cont6)
    
    raw_input('\n\nTHE END')