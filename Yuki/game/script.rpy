define y = Character("Yuki", image="yuki")
define m = Character("player_name")

init python:
    import webbrowser

# The game starts here.
label start:
    scene bg stone
    show yuki happy

    "Hello, my name is Yuki. I'm here to help."
    $ player_name = renpy.input("What's your name?")
    $ player_name = player_name.strip()

# I'd put the default name in the definition (set to "player_name" right now) and if player_name isn't blank, then override it (see kyles.example
    if player_name == "":
        $ m.name="Sakura"

    y "Pleased to meet you, %(player_name)s!"
    y "I'm new here, so please bear with me. What would you like to do?"
    label yuki_menu:
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
    show yuki happy

    y vhappy "Would you like to know something?"
    m "Sure"
    $ import datetime
    $ t = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    y happy "It is curently %(t)s"
    jump yuki_menu

label affirmation:
    scene bg solace
    show yuki happy

    y "All things are for the eventual best"
    y "You've got this"
    y "Focus on what you can do"
    y " You can do anything"
    y "You are Smaug"
    y "Hakuna Matata"
    show yuki vhappy
    y " It means no worries"
    y "Being afraid of things going wrong isn't the way to make things go right"
    y " You know this"
    y "Remember how far you've come, not just how far you have to go. You are not where you want to be, but neither are you where you used to be"
    m "Thank you"
    jump yuki_menu

label math:
    jump yuki_menu

# this should not be a renpy label. maybe have it as a python funtion in a custom module?
label yes_no:
    jump yuki_menu
    
label cake: 
    show yuki mischief
    jump yuki_menu
    
label music: 
    show yuki happy
    menu:
        "What do you feel like?"
        "lofi":
            $ webbrowser.open("https://www.youtube.com/watch?v=dJhW1J6gIWA")

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
    show yuki sad
    "It will be lonely without you here"
    "But if you must..."
    "must you?" 
    menu:
        "yes":
            show yuki vsad
            "Goodbye then, I'm glad you stopped by"
            $ renpy.quit(0)
        "no":
            "I'm glad you can stay with me for a little longer."
            "What would you like to do now?"
            jump yuki_menu

