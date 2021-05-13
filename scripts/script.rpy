# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define L = Character("Lyra")
define G = Character("The Guide")
define LB = Character("Lizardmen Bandits")
define B = Character("Ben")
define P = Character("Protagonist")
#define N = Character("Narrator")

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
    
    #Chapter 2
label chapter2_start:
    P "\"What is this thing? It seems like a door that connects another place. \""

    "\"Let me see if I can push it...\""
    
    "..."

    "\"What happened? Did I just take a nap?\""
    
    "\"Some strong light is shining on my face that I can't open my eyes.\"" 
    
    "\"But the light feels so familiar.\""

    "......"
    
    "\"Isn't it the light in my room?!\""

    "I try to block the light using my hands and finally I can open my eyes just a little bit."

    "\"Brown chairs, empty lockers...\" It seems like I am in my room." 

    "\"The blue mirror... Wait! The mirror!\""

    "\"I passed out because I tried to push the mirror! \""

    "I held the bed and got up from the ground."

    "\"blzzzz blzzzzzz blzzzzzzzz\" The door bell starts screaming"

    "\"Who is this? I don't remember someone is going to see me at this time.\" I start become curious while I open the door"

    G "\"What's up (Protagonist's name)! Are you ready for the Champions League Final? We gotta go fast before the seats run out!\""
    
menu:

    P "\"What are you talking about?\"":
        jump chapter2_confused
    
    P "\"Let's goooooo!!!\"":
        jump chapter2_pretend

label chapter2_confused:
    
    G "\"How can you forget about this? It is the L.A versus Liverpool! Let's turn those British man down!\""

    P "Oh my god. Am I crazy? How can the L.A be in the Champions League and face Liverpool? They don't even on the same continent."

    "ALso, is she Lyra? I don't remember that Lyra is a soccer fan. Unless...Unless this is a different world?"
    
    G "\"Hey! What are you waiting for? Grab your jacket and let's go! I don't want to stand in the crowd.\"" 

    jump chapter2_bar

label chapter2_pretend:

    G "\"Don't forget to grab your jacket! It is a little bit cold in the bar. They always set the temperature low. \""

    P "\"Sure. Man City is definitely going to win this time. They have the Premier League already and the final is just another hard battle for Chelsea...\"

    G "\"Wait wait wait...Are you from 2021 or something? It is the year (time holder). It's the L.A versus Liverpool! \""

    P "How can the L.A faces Liverpool in Champions League? They are not on the same continent!"

    "And if this is year (time holder), am I in a different world? But look at my table, Lyra, the mirror..."

    G "\"Yo! Stop zoning out! We won't have a place to sit if we are late! \""

    jump chapter2_bar

    
    return
