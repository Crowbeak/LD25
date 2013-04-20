import time

from displays import *
from classes import workclass
from simulation import run_sim as run_sim


def instructions():
    """
    Displays the employee "manual", which is actually tips for playing.
    """
    print_from_file("resources/story/instructions.txt")


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
    print_from_file("resources/story/intro/credits.txt")
    raw_input('\n(Press enter key to continue)')
    print_from_file("resources/story/intro/good_morning_dave.txt")
    choice = 0
    again = ['\nCome on, now. I know you haven\'t had your coffee yet, but surely you',
            'can find the 1 and 2 keys on your keyboard.']
    while (int(choice) != 1) and (int(choice) != 2):
        menu = ['\nWhat do you do?',
                '1 - Grunt, wave goodbye, and go to your cubicle.',
                '2 - Ask about his wife.']
        print_text(menu)
    
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                print_from_file("resources/story/intro/good_morning_dave_r1.txt")
            elif int(choice) == 2:
                print_from_file("resources/story/intro/good_morning_dave_r2.txt")
            else:
                print_text(again)
        except ValueError:
            choice = 0
            print_text(again)


def ch01():
    intro = ['\nAfter logging in, you consider your options.',
             '\nWhat do you do?']
    print_text(intro)
    
    nosebook = False
    email = False
    again = ['\nNo, no, no, that\'s not a valid choice. Try again!']
    while True:
        menu = ['1 - See what\'s happening on Nosebook.',
                '2 - Check your email.',
                '3 - Do the work they\'re paying you to be here for.']
        print_text(menu)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                if nosebook:
                    print '\nYeah... still a lot of nosebook-picking going on here.'
                else:
                    print_from_file("resources/story/ch01/ch01_nosebook.txt")
                    nosebook = True
            elif int(choice) == 2:
                if email:
                    print '\nNo new email. Alas.'
                else:
                    print '\nEarlobe enlargement? Wow, they\'ll try anything these days.'
                    email = True
            elif int(choice) == 3:
                print_from_file("resources/story/ch01/ch01_work.txt")
                while True:
                    menu = ['\nWhat do you do?',
                            '1 - Review the manual again to stave off the inevitable. [How to Play]',
                            '2 - Just do it.']
                    print_text(menu)
                    
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
                            run_sim(workplacesToBe, 2, '#135466')
                            break
                        else:
                            print 'Try again, please. Invalid input.'
                    except ValueError:
                        choice = 0
                        print 'Try again, please. Invalid input.'
                break
            else:
                print_text(again)
        except ValueError:
            choice = 0
            print_text(again)
        
        print '\nWhat do you do next?'

    lunch = ['You yawn and stretch. Coffee time is past. It\'s snack time now.',
             '\nWhoops!',
             '\nApparently you meant lunch time.']
    print_text(lunch)
    
    choice = 0
    again = ['\nYou... wait, what?! Try that again.']
    while (int(choice) != 1) and (int(choice) != 2):
        chc1 = ['\nWhere do you want to go?',
                '1 - The good old cafeteria. Mediocre free food, decent conversation.',
                '2 - Home. Sandwiches and solitude.']
        print_text(chc1)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                print_from_file("resources/story/ch01/ch01_cafeteria.txt")
            elif int(choice) == 2:
                print_from_file("resources/story/ch01/ch01_home.txt")
            else:
                print_text(again)
        except ValueError:
            choice = 0
            print_text(again)
        
        raw_input('\n(Press enter key to continue)')


def ch02():
    """
    Returns True if Dave is still in player's life at end of module or False
    otherwise.
    """
    print_from_file("resources/story/ch02/ch02_intro.txt")
    
    choice = 0
    while (int(choice) != 1) and (int(choice) != 2):
        opts = ['\n1 - Yeah... that\'s so out of character I can only assume aliens',
                '    are involved.',
                '2 - Nah. Dave\'s a great guy but it\'s nice not to have to deal',
                '    with his peppy peppiness sometimes.']
        print_text(opts)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                dave = True
                print_from_file("resources/story/ch02/ch02_look.txt")
            elif int(choice) == 2:
                dave = False
                print '\nYou sip your coffee obtained in quiet and log in.'
            else:
                print '\nDrink some of your coffee and try that again.'
        except ValueError:
            choice = 0
            print '\nDrink some of your coffee and try that again.'
    
    intro = ['Confronted with the usual options...',
             '\nWhat do you do?']
    print_text(intro)
    
    #Goof off or work.
    nosebook = False
    email = False
    while True:
        opts = ['1 - See what\'s happening on Nosebook.',
                '2 - Check your email.']
        if dave:
            opts.append('3 - Work. Maybe it\'ll take your mind off things.')
        else:
            opts.append('3 - Do the work they\'re paying you to be here for.')
        print_text(opts)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                if nosebook:
                    if dave:
                        noseSeen = ['\nEven scoffing at the nosebook-picking can\'t cheer you up.',
                                    'The term "nosebook-picking" isn\'t even funny right now.']
                    else:
                        noseSeen = ['\nMore nosebook-picking. Ah, nosebook-picking.',
                                    'Just the term makes you happy. How do you visualize that?']
                    print_text(noseSeen)
                else:
                    print_from_file("resources/story/ch02/ch02_nosebook.txt")
                    if dave:
                        print('\nThis isn\'t helping.')
                    else:
                        print('\nYou should probably work. Probably.')
                    nosebook = True
            elif int(choice) == 2:
                if email:
                    if dave:
                        print('\nNo new email. Not that you did a good job reading the first two.')
                    else:
                        print('\nNo new email. Who\'s surprised?')
                else:
                    newEmail = ['\nSomething from Biggs about a party... don\'t care right now.',
                                'And... news. Noone cares about that.']
                    print_text(newEmail)
                    email = True
            elif int(choice) == 3:
                #Working.
                while True:
                    opts = ['\nWhat do you do?',
                            '1 - Review the manual again.']
                    if dave:
                        opts.append('2 - Work. Or try to.')
                    else:
                        opts.append('2 - Work! It\'s like a crummy party you get paid to attend.')
                    print_text(opts)
                    
                    choice = raw_input("Pick one:")
                    try:
                        if int(choice) == 1:
                            instructions()
                        elif int(choice) == 2:
                            workplacesToBe = []
                            workplacesToBe.append(workclass.WorkplaceToBe(7, True, workclass.Farm,
                                                                          "FARM #512", "A512"))
                            workplacesToBe.append(workclass.WorkplaceToBe(5, True, workclass.Factory,
                                                                          "FACTORY #110", "C110"))
                            workplacesToBe.append(workclass.WorkplaceToBe(6, True, workclass.Factory,
                                                                          "FACTORY #112", "C112"))
                            workplacesToBe.append(workclass.WorkplaceToBe(4, False, workclass.Unassigned,
                                                                          "UNASSIGNED", "NONE"))
                            run_sim(workplacesToBe, 4, '#187949')
                            break
                        else:
                            print 'Try again, please. Invalid input.'
                    except ValueError:
                        choice = 0
                        print 'Try again, please. Invalid input.'
                break
            else:
                if dave:
                    print('\nI know you\'re distracted, but please use proper input.')
                else:
                    print('Have a sip of carefree coffee and try again.')
        except ValueError:
            choice = 0
            if dave:
                print('\nI know you\'re distracted, but please use proper input.')
            else:
                print('Have a sip of carefree coffee and try again.')
        
        print '\nWhat do you do next?'
    
    if dave:
        print('\nLunch time. You still haven\'t heard from Dave. Time to go check on him.')
    else:
        print_from_file("resources/story/ch02/ch02_worked.txt")
    
    raw_input('\n(Press enter key to continue)')
    return dave
    
    
def ch03(dave):
    if dave:
        print_from_file("resources/story/ch03/ch03_dave_intro.txt")
        print('\nWhat do you do?')
        time.sleep(0.2)
    
        #Goof off or work.
        nosebook = False
        email = False
        while True:
            opts = ['1 - Pick your Nosebook.',
                    '2 - Check your eternally uninteresting email.',
                    '3 - Slave away.']
            print_text(opts)
        
            choice = raw_input("Pick one:")
            try:
                if int(choice) == 1:
                    if nosebook:
                        print '\nOh, why bother.'
                    else:
                        print_from_file("resources/story/ch03/ch03_nosebook.txt")
                        nosebook = True
                elif int(choice) == 2:
                    if email:
                        print '\nNo new email. Again.'
                    else:
                        print '\nNothing.'
                        email = True
                elif int(choice) == 3:
                    #Tries to work.
                    print_from_file("resources/story/ch03/ch03_work.txt")
                    raw_input('\n(Press enter key to continue)')
                    break
                else:
                    print '\nJust put in a correct input so you can get this done and go home.'
            except ValueError:
                choice = 0
                print '\nJust put in a correct input so you can get this done and go home.'
        
            print '\nWhat do you do next?'
    else:
        print_from_file("resources/story/ch03/ch03_nodave_intro.txt")
        
        choice = 0
        while (int(choice) != 1) and (int(choice) != 2):
            opts = ['\nWill you eat with Biggs and Wedge today?',
                    '1 - Yeah.',
                    '2 - No.']
            print_text(opts)
        
            choice = raw_input("Pick one:")
            try:
                if int(choice) == 1:
                    print_from_file("resources/story/ch03/ch03_yes.txt")
                    raw_input('\n(Press enter key to continue)')
                elif int(choice) == 2:
                    print_from_file("resources/story/ch03/ch03_no.txt")
                    raw_input('\n(Press enter key to continue)')
                else:
                    print '\nSimple question. He\'s just asking.'
            except ValueError:
                choice = 0
                print '\nSimple question. He\'s just asking.'
        
    
def spanishInquisition():
    print_from_file("resources/story/si/si_intro.txt")
    
    choice = 0
    while (int(choice) != 1) and (int(choice) != 2):
        opts = ['\nWell, do you?',
                '1 - I still don\'t understand what I\'m supposed to have done.',
                '2 - Would it matter if I did?']
        print_text(opts)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                pass
            elif int(choice) == 2:
                print_from_file("resources/story/si/si_no_change.txt")
            else:
                print '\n"Have you anything to say in your defense?" he asks again.'
        except ValueError:
            choice = 0
            print '\n"Have you anything to say in your defense?" he asks again.'
    
    print_from_file("resources/story/si/si_verdict.txt")
    raw_input('\n(Press enter key to continue)')
    print_from_file("resources/story/si/si_ending01.txt")
    raw_input('\n(Press enter key to continue)')
    print_from_file("resources/story/si/si_ending02.txt")
    raw_input('\n(Press enter key to continue)')
    print_from_file("resources/story/si/si_ending03.txt")
    
    choice = 0
    again = ['\n"What\'s that?" he asks. I can\'t hear you."',
             '\nHis subordinate snickers.']
    while (int(choice) != 1) and (int(choice) != 2):
        opts = ['1 - You\'re kidding, right? You can\'t be serious.',
                '2 - Say nothing.']
        print_text(opts)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                print_from_file("resources/story/si/si_speech.txt")
            elif int(choice) == 2:
                print_from_file("resources/story/si/si_silence.txt")
            else:
                print_text(again)
        except ValueError:
            choice = 0
            print_text(again)
    
    print_from_file("resources/story/si/si_ending04.txt")
    raw_input('\n(Press enter key to continue)')
    print_from_file("resources/story/si/si_ending05.txt")
    
    raw_input('\n\nTHE END')
