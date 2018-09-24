# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Yuki")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "yuki happy.png" to the images
    # directory.

    show Yuki happy

    # These display lines of dialogue.

    "Hello, my name is Yuki. I'm here to help."

    e "I'm new here, so please bear with me."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return