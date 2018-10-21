define y = Character("Yuki", image="yuki")
define m = Character("Sakura")

init python:
    import webbrowser
    import subprocess
    import datetime
    import random
#    from pprint import pprint
#    import requests
#    import sys, os
#    import Profile


transform taller:
    xalign 0.5
    yalign 0.8

transform side:
    xalign 0.1
    yalign 0.8

define config.main_menu_music = "music.mp3"

# The game starts here.
label start:
    scene bg stone
    show yuki happy at taller

    "Hello, my name is Yuki. I'm here to help. {image=heart3.png}"
    $ player_name = renpy.input("What's your name?")
    $ player_name = player_name.strip()

# I'd put the default name in the definition (set to "player_name" right now) and if player_name isn't blank, then override it (see kyles.example
    if player_name == "":
        $ m.name="Sakura"

    y "Pleased to meet you, %(player_name)s!"
# should show miru before you announce otherwise shes not there for a click
    show lucy happy at side
    y "and this is Miru"
    hide lucy happy
    y "I'm new here, so please bear with me. What would you like to do?"
    label yuki_menu:
        scene bg stone
        show yuki happy at taller
        
        menu:

            "I would like to..."
            "chat":
                jump chat

            "math":
                jump math

            "music":
                jump music

            "affirmation":
                jump affirmation

            "cake":
                jump cake


            "leave":
                #you need to either make a label leave, or just have this option return or quit
                jump leave

label chat:
    scene bg stone
    show yuki happy at taller

    y vhappy "Would you like to know something?"
    m "Sure"
    $ t = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    y happy "It is curently %(t)s"
    jump yuki_menu

label affirmation:
    scene bg solace
    show yuki happy at taller

    $ nice = [ "All things are for the eventual best", "You've got this!", "Focus on what you can do, and you can do anything.", "You are Smaug", "Hakuna Matata: \nIt means No Worries!", "Being afraid of things going wrong isn't the way to make things go right. \nYou know this.", "Remember how far you've come, not just for far you have to go. \nYou are not where you want to be, but neither are you where you used to be", "Optimism is the faith that leads to achievement.", "Failure will never overtake me if my determination to succeed is strong enough.", "Good, better, best. Never let it rest 'til your good is better and your better is best.", "I love you", "It always seems impossible until it's done.", "It does not matter how slowly you go as long as you do not stop.", "We may encounter many defeats but we must not be defeated.", "I believe in you.", "You have already won. \nEverything else is extra."]
    $ n = random.choice(nice)
    y "%(n)s"
    menu:
        y "Another?"
        "yes":
             jump affirmation
        "no":
            m "Thank you"
            jump yuki_menu

label math:
    $ number = renpy.input("What's your favourite number between 0 and 10?", allow='0123456789', exclude='qwertyuiopasdfghjklzxcvbnm,/;')
    $ number = int(number)
    #this bit should all be in a python module not in yuki_renpy (returning the string y should say)
    if number == 0:
        y "Of course YOU would choose such a fancy number"
    elif number > 0 and number <= 1: 
        y "Because you're the best!"
    elif number > 1 and number <= 2: 
        y "Even Steven?"
    elif number > 2 and number <= 3: 
        y "You're an odd one, aren't you?"
    elif number > 3 and number <= 4: 
        y "Even Steven?"
    elif number > 4 and number <= 5: 
        y "Right in the middle, best of both!"
    elif number > 5 and number <= 6: 
        y "Even Steven?"
    elif number > 6 and number <= 7: 
        y "Feeling lucky, huh?"
    elif number > 7 and number <= 8: 
        y "Even Steven?"
    elif number > 8 and number <= 9: 
        y "You're an odd one, aren't you?"
    elif number > 9 and number <= 10: 
        y "Of course YOU would choose such a fancy number"
    else:
        y "That's not a number between 0 and 10!"
    jump yuki_menu

# this should not be a renpy label. maybe have it as a python funtion in a custom module?
label yes_no:
    jump yuki_menu
    
label cake: 
    scene bg tree
    show yuki mischief at taller
    y "do you like cake?"
    menu:
        "yes":
            y "The cake is a lie"
            y "But you already knew that."
            jump yuki_menu


        "no":
            y "The cake is a lie anyway."
            y "Which do you like?"
            menu: 
                "Pie":
                    show yuki vhappy at taller
                    y "Pie is a fantastic choice!"
                "Ice Cream":
                    show yuki vhappy at taller
                    y "Ice Cream is so cold!"
                "Cookies":
                    show yuki vhappy at taller
                    y "Anzac, chocolate chip, coconut... There are so many!"
                "Candy":
                    show yuki vhappy at taller
                    y "Too many varieties of sweets to list, too many to try!"
    y "I like that too!"            
    jump yuki_menu
    
label music: 
    show yuki happy at taller
    menu:
        y "What do you feel like?"
        "lofi":
            $ subprocess.call(["xdg-open", "https://www.youtube.com/watch?v=dJhW1J6gIWA"])

        "trance":
            $ webbrowser.open("https://www.youtube.com/watch?v=buqNTkjTY20")

        "dubstep":
            $ webbrowser.open("https://www.youtube.com/watch?v=a41icW_FtsI")
            
        "ghibli":
            $ webbrowser.open("https://www.youtube.com/watch?v=YjohMzHkBqI")

        "samurai":
            $ webbrowser.open("https://www.youtube.com/watch?v=jrTMMG0zJyI")
    
        "violin":
            $ webbrowser.open("https://www.youtube.com/watch?v=jvipPYFebWc&start_radio=1&\list=RDEMzT1XwmFnIup_KYXuc2rUZA")

        "glitch":
            $ webbrowser.open("https://www.youtube.com/watch?v=52Qug_siqKw")

        "None":
            pass
    jump yuki_menu

label leave: 
    show yuki sad at taller
    y "It will be lonely without you here"
    y "But if you must..."
    y "must you?" 
    menu:
        "yes":
            show yuki vsad at taller
            y "Goodbye then, I'm glad you stopped by"
            $ renpy.quit(0)
        "no":
            show yuki vhappy at taller
            y "I'm glad you can stay with me for a little longer."
            y "What would you like to do now?"
            jump yuki_menu

