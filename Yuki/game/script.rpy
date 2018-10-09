# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yuki")
define m = Character("player_name")


init python:
    import webbrowser

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg stone

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "yuki happy.png" to the images
    # directory.

    show yuki happy

    # These display lines of dialogue.

    "Hello, my name is Yuki. I'm here to help."

  # The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.

    $ player_name = renpy.input("What's your name?")

    $ player_name = player_name.strip()
# The .strip() instruction removes any extra spaces the player 
# may have typed by accident.

#  If the player can't be bothered to choose a name, then we
#  choose a suitable one for them:
    if player_name == "":
        $ m.name="Sakura"

# And get a nostalgic sigh from Seasons of Sakura fans!
    
# Now the other characters in the game can greet the player.
  
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

                jump leave

label chat:

scene bg stone
show yuki happy

y "Would you like to know something?"
m "Sure"
$ import datetime
$ t = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
y "Today's date is %(t)s"
jump yuki_menu

label affirmation:

show yuki happy

y "All things are for the eventual best"
y "You've got this"
y "Focus on what you can do"
y " You can do anything"
y "You are Smaug"
y "Hakuna Matata"
y " It means no worries"
y "Being afraid of things going wrong isn't the way to make things go right"
y " You know this"
y "Remember how far you've come, not just how far you have to go. You are not where you want to be, but neither are you where you used to be"
m "Thank you"
jump yuki_menu

label math:

label yes_no:

label cake: 

label music: 
        menu:

            "What do you feel like?"
            "lofi":

                jump launch_lofi

            "trance":

                jump launch_trance

            "dubstep":

                jump launch_dubstep

            "ghibli":

                jump launch_ghibli

            "samurai":

                jump launch_samurai

            "violin":

                jump launch_violin

            "glitch":

                jump launch_glitch

            "None":

                jump yuki_menu

label launch_lofi:
    $ webbrowser.open("https://www.youtube.com/watch?v=dJhW1J6gIWA&t=766s")
    jump yuki_menu

label launch_trance:
    $ webbrowser.open("https://www.youtube.com/watch?v=buqNTkjTY20")
    jump yuki_menu

label launch_dubstep:
    $ webbrowser.open("https://www.youtube.com/watch?v=a41icW_FtsI")
    jump yuki_menu

label launch_ghibli:
    $ webbrowser.open("https://www.youtube.com/watch?v=YjohMzHkBqI")
    jump yuki_menu

label launch_samurai:
    $ webbrowser.open("https://www.youtube.com/watch?v=jrTMMG0zJyI")
    jump yuki_menu

label launch_violin:
    $ webbrowser.open("https://www.youtube.com/watch?v=jvipPYFebWc&start_radio=1&\list=RDEMzT1XwmFnIup_KYXuc2rUZA")
    jump yuki_menu

label launch_glitch:
    $ webbrowser.open("https://www.youtube.com/watch?v=52Qug_siqKw")
    jump yuki_menu





   



#    y "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
