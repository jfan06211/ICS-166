# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define L = Character("Lyra")


# The game starts here.

label start:
    stop music fadeout 1.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show victoria_guide3

    # These display lines of dialogue.

    L "You've created a new Ren'Py game."

    L "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
