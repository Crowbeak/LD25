import ddisplay
from classes import workclass
from simulation import runSim as runSim


def instructions():
    """
    Displays the employee "manual", which is actually tips for playing.
    """
    ddisplay.printFromFile("resources/story/instructions.txt")


def lookWork():
    intro = ['Confronted with the usual options...',
             '\nWhat do you do?']
    ddisplay.printText(intro)
    
    #Goof off or work.
    nosebook = False
    email = False
    while True:
        opts = ['1 - See what\'s happening on Nosebook.',
                '2 - Check your email.',
                '3 - Work. Maybe it\'ll take your mind off things.']
        ddisplay.printText(opts)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                if nosebook:
                    noseSeen = ['\nEven scoffing at the nosebook-picking can\'t cheer you up.',
                                'The term "nosebook-picking" isn\'t even funny right now.']
                    ddisplay.printText(noseSeen)
                else:
                    ddisplay.printFromFile("resources/story/ch02/ch02_nosebook.txt")
                    ddisplay.printText(['\nThis isn\'t helping.\n'])
                    nosebook = True
            elif int(choice) == 2:
                if email:
                    print '\nNo new email. Not that you did a good job reading the first two.'
                else:
                    newEmail = ['\nSomething from Biggs about a party... don\'t care right now.',
                                'And... news. Noone cares about that.']
                    ddisplay.printText(newEmail)
                    email = True
            elif int(choice) == 3:
                #Working.
                while True:
                    workopts = ['\nWhat do you do?',
                                '1 - Review the manual again.',
                                '2 - Work. Or try to.']
                    ddisplay.printText(workopts)
                    
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


def justWork():
    intro = ['Confronted with the usual options...',
             '\nWhat do you do?']
    ddisplay.printText(intro)
    
    nosebook = False
    email = False
    while True:
        opts = ['1 - See what\'s happening on Nosebook.',
                '2 - Check your email.',
                '3 - Do the work they\'re paying you to be here for.']
        ddisplay.printText(opts)
        
        choice = raw_input("Pick one:")
        try:
            if int(choice) == 1:
                if nosebook:
                    noseSeen = ['\nMore nosebook-picking. Ah, nosebook-picking.',
                                'Just the term makes you happy. How do you visualize that?']
                    ddisplay.printText(noseSeen)
                else:
                    ddisplay.printFromFile("resources/story/ch02/ch02_nosebook.txt")
                    ddisplay.printText(['\nYou should probably work. Probably.\n'])
                    nosebook = True
            elif int(choice) == 2:
                if email:
                    print '\nNo new email. Who\'s surprised?'
                else:
                    newEmail = ['\nSomething from Biggs about a party... don\'t care right now.',
                                'And... news. Noone cares about that.']
                    ddisplay.printText(newEmail)
                    email = True
            elif int(choice) == 3:
                #Working.
                while True:
                    workopts = ['\nWhat do you do?',
                                '1 - Review the manual again.',
                                '2 - Work! It\'s like a crummy party you get paid to attend.']
                    ddisplay.printText(workopts)
                    
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


if __name__ == '__main__':
    print("Testing instructions()")
    instructions()
    raw_input('\nPress enter to test lookWork()')
    lookWork()
    raw_input('\nPress enter to test justWork()')
    justWork()
    print("\nTesting successfully completed.")