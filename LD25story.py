def sCredits():
    print "Made for Ludum Dare 25 by Lena LeRay."
    print "Theme: You Are the Villain"
    print "Please play through to the end."
    print "You won't see how it connects to the theme if you stop early."

def intro():
    choice = 0
    
    print '\n\n"Good morning!"\n'
    print 'Dave is as cheerful as ever. Does he really not drink coffee?\n'
    print '"I really don\'t drink coffee," he says with a grin.\n'
    print 'Before you can ask how he knew what you were thinki--\n'
    print '"You\'ve asked me that question so many times now," he says, "that I'
    print 'can see it in your face."\n'
    
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