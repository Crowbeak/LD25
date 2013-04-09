import time

import ddisplay
from classes import workclass
from simulation import runSim as runSim
from helpers import *


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
    ddisplay.printFromFile("resources/story/intro/credits.txt")
    raw_input('\n(Press enter key to continue)')
    ddisplay.printFromFile("resources/story/intro/good_morning_dave.txt")
    choice = 0
    again = ['\nCome on, now. I know you haven\'t had your coffee yet, but surely you',
            'can find the 1 and 2 keys on your keyboard.']
    while (int(choice) != 1) and (int(choice) != 2):
        menu = ['\nWhat do you do?',
                '1 - Grunt, wave goodbye, and go to your cubicle.',
                '2 - Ask about his wife.']
        ddisplay.printText(menu)
    
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                ddisplay.printFromFile("resources/story/intro/good_morning_dave_r1.txt")
            elif int(choice) == 2:
                ddisplay.printFromFile("resources/story/intro/good_morning_dave_r2.txt")
            else:
                ddisplay.printText(again)
        except ValueError:
            choice = 0
            ddisplay.printText(again)


def ch01():
    intro = ['\nAfter logging in, you consider your options.',
             '\nWhat do you do?']
    ddisplay.printText(intro)
    
    nosebook = False
    email = False
    again = ['\nNo, no, no, that\'s not a valid choice. Try again!']
    while True:
        menu = ['1 - See what\'s happening on Nosebook.',
                '2 - Check your email.',
                '3 - Do the work they\'re paying you to be here for.']
        ddisplay.printText(menu)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                if nosebook:
                    print '\nYeah... still a lot of nosebook-picking going on here.'
                else:
                    ddisplay.printFromFile("resources/story/ch01/ch01_nosebook.txt")
                    nosebook = True
            elif int(choice) == 2:
                if email:
                    print '\nNo new email. Alas.'
                else:
                    print '\nEarlobe enlargement? Wow, they\'ll try anything these days.'
                    email = True
            elif int(choice) == 3:
                ddisplay.printFromFile("resources/story/ch01/ch01_work.txt")
                while True:
                    menu = ['\nWhat do you do?',
                            '1 - Review the manual again to stave off the inevitable. [How to Play]',
                            '2 - Just do it.']
                    ddisplay.printText(menu)
                    
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
                ddisplay.printText(again)
        except ValueError:
            choice = 0
            ddisplay.printText(again)
        
        print '\nWhat do you do next?'

    lunch = ['You yawn and stretch. Coffee time is past. It\'s snack time now.',
             '\nWhoops!',
             '\nApparently you meant lunch time.']
    ddisplay.printText(lunch)
    
    choice = 0
    again = ['\nYou... wait, what?! Try that again.']
    while (int(choice) != 1) and (int(choice) != 2):
        chc1 = ['\nWhere do you want to go?',
                '1 - The good old cafeteria. Mediocre free food, decent conversation.',
                '2 - Home. Sandwiches and solitude.']
        ddisplay.printText(chc1)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                ddisplay.printFromFile("resources/story/ch01/ch01_cafeteria.txt")
            elif int(choice) == 2:
                ddisplay.printFromFile("resources/story/ch01/ch01_home.txt")
            else:
                ddisplay.printText(again)
        except ValueError:
            choice = 0
            ddisplay.printText(again)
        
        raw_input('\n(Press enter key to continue)')

#TODO: Eliminate lookWork() and justWork() by combining them into one function
#      with if statements based on the dave variable. (Dumbass!)
def ch02():
    """
    Returns True if Dave is still in player's life at end of module or False
    otherwise.
    """
    ddisplay.printFromFile("resources/story/ch02/ch02_intro.txt")
    
    choice = 0
    while (int(choice) != 1) and (int(choice) != 2):
        opts = ['\n1 - Yeah... that\'s so out of character I can only assume aliens',
                '    are involved.',
                '2 - Nah. Dave\'s a great guy but it\'s nice not to have to deal',
                '    with his peppy peppiness sometimes.']
        ddisplay.printText(opts)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                dave = True
                ddisplay.printFromFile("resources/story/ch02/ch02_look.txt")
                lookWork()
                print '\nLunch time. You still haven\'t heard from Dave. Time to go check on him.'
                time.sleep(0.2)
            elif int(choice) == 2:
                dave = False
                print '\nYou sip your coffee obtained in quiet and log in.'
                justWork()
                ddisplay.printFromFile("resources/story/ch02/ch02_worked.txt")
            else:
                print '\nDrink some of your coffee and try that again.'
        except ValueError:
            choice = 0
            print '\nDrink some of your coffee and try that again.'
    
    raw_input('\n(Press enter key to continue)')
    return dave
    
    
def ch03(dave):
    if dave:
        ddisplay.printFromFile("resources/story/ch03/ch03_dave_intro.txt")
        print('\nWhat do you do?')
        time.sleep(0.2)
    
        #Goof off or work.
        nosebook = False
        email = False
        while True:
            opts = ['1 - Pick your Nosebook.',
                    '2 - Check your eternally uninteresting email.',
                    '3 - Slave away.']
            ddisplay.printText(opts)
        
            choice = raw_input("Pick one:")
            try:
                if int(choice) == 1:
                    if nosebook:
                        print '\nOh, why bother.'
                    else:
                        ddisplay.printFromFile("resources/story/ch03/ch03_nosebook.txt")
                        nosebook = True
                elif int(choice) == 2:
                    if email:
                        print '\nNo new email. Again.'
                    else:
                        print '\nNothing.'
                        email = True
                elif int(choice) == 3:
                    #Tries to work.
                    ddisplay.printFromFile("resources/story/ch03/ch03_work.txt")
                    raw_input('\n(Press enter key to continue)')
                    break
                else:
                    print '\nJust put in a correct input so you can get this done and go home.'
            except ValueError:
                choice = 0
                print '\nJust put in a correct input so you can get this done and go home.'
        
            print '\nWhat do you do next?'
    else:
        ddisplay.printFromFile("resources/story/ch03/ch03_nodave_intro.txt")
        
        choice = 0
        while (int(choice) != 1) and (int(choice) != 2):
            opts = ['\nWill you eat with Biggs and Wedge today?',
                    '1 - Yeah.',
                    '2 - No.']
            ddisplay.printText(opts)
        
            choice = raw_input("Pick one:")
            try:
                if int(choice) == 1:
                    ddisplay.printFromFile("resources/story/ch03/ch03_yes.txt")
                    raw_input('\n(Press enter key to continue)')
                elif int(choice) == 2:
                    ddisplay.printFromFile("resources/story/ch03/ch03_no.txt")
                    raw_input('\n(Press enter key to continue)')
                else:
                    print '\nSimple question. He\'s just asking.'
            except ValueError:
                choice = 0
                print '\nSimple question. He\'s just asking.'
        
    
def spanishInquisition():
    ddisplay.printFromFile("resources/story/si/si_intro.txt")
    
    choice = 0
    while (int(choice) != 1) and (int(choice) != 2):
        opts = ['\nWell, do you?',
                '1 - I still don\'t understand what I\'m supposed to have done.',
                '2 - Would it matter if I did?']
        ddisplay.printText(opts)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                pass
            elif int(choice) == 2:
                ddisplay.printFromFile("resources/story/si/si_no_change.txt")
            else:
                print '\n"Have you anything to say in your defense?" he asks again.'
        except ValueError:
            choice = 0
            print '\n"Have you anything to say in your defense?" he asks again.'
    
    ddisplay.printFromFile("resources/story/si/si_verdict.txt")
    raw_input('\n(Press enter key to continue)')
    ddisplay.printFromFile("resources/story/si/si_ending01.txt")
    raw_input('\n(Press enter key to continue)')
    ddisplay.printFromFile("resources/story/si/si_ending02.txt")
    raw_input('\n(Press enter key to continue)')
    ddisplay.printFromFile("resources/story/si/si_ending03.txt")
    
    choice = 0
    again = ['\n"What\'s that?" he asks. I can\'t hear you."',
             '\nHis subordinate snickers.']
    while (int(choice) != 1) and (int(choice) != 2):
        opts = ['1 - You\'re kidding, right? You can\'t be serious.',
                '2 - Say nothing.']
        ddisplay.printText(opts)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                ddisplay.printFromFile("resources/story/si/si_speech.txt")
            elif int(choice) == 2:
                ddisplay.printFromFile("resources/story/si/si_silence.txt")
            else:
                ddisplay.printText(again)
        except ValueError:
            choice = 0
            ddisplay.printText(again)
    
    ddisplay.printFromFile("resources/story/si/si_ending04.txt")
    raw_input('\n(Press enter key to continue)')
    ddisplay.printFromFile("resources/story/si/si_ending05.txt")
    
    raw_input('\n\nTHE END')
