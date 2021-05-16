# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define N = Character("Narrator")
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

    "What are you talking about?":
        jump chapter2_confused

    "Let's goooooo!!!":
        jump chapter2_pretend

label chapter2_confused:

    G "\"How can you forget about this? It is the L.A versus Liverpool! Let's turn those British man down!\""

    P "Oh my god. Am I crazy? How can the L.A be in the Champions League and face Liverpool? They don't even on the same continent."

    "Also, is she Lyra? I don't remember that Lyra is a soccer fan. Unless...Unless this is a different world?"

    G "\"Hey! What are you waiting for? Grab your jacket and let's go! I don't want to stand in the crowd.\""

    P "\"I think I am better not going to the bar since I haven't reach 21...\""

    G "\"Bro, stop reading those stupid history books. A one-year-old can buy a drink now if they can speak. \""

    jump chapter2_bar

label chapter2_pretend:

    G "\"Don't forget to grab your jacket! It is a little bit cold in the bar. They always set the temperature low. \""

    P "\"Wait are we going to a bar? I haven't reach 21, yet!\""

    G "\"No one cares about age limit! If you can speak, you are legal to get a drink now. By the way, which team has a better chance to win this time? \""

    P "\"Man City is definitely going to win this time. They have the Premier League already and the final is just another hard battle for Chelsea...\""

    G "\"Wait wait wait...Are you from 2021 or something? It is the year (time holder). It's the L.A versus Liverpool! \""

    P "How can the L.A faces Liverpool in Champions League? They are not on the same continent!"

    "And if this is year (time holder), am I in a different world? But look at my table, Lyra, the mirror..."

    G "\"Yo! Stop zoning out! We won't have a place to sit if we are late! \""

    jump chapter2_bar

label chapter2_bar:

    N "(Protagonist's name) and the Guide is on their way to the bar \"Frolic Room\"."

    show Ben

    B "\"Hey you guys! Are you guys also going to watch the final? \""

    G "\"Oh hi Ben! Are you going too? Would you like to joi  n us? We are going to the Forlic Room! \""

    B "\"Sure! Watching soccer game in the Forlic Room could be cool. Do you guys think the L.A can win this final? \""

    P "\"Based on my experience, Liverpool is going to win easily. They were the champion of the last year. The L.A is just a average team in MLS. They are not going to have any chances. \""

    B "\"Dude, the L.A is not like 500 years ago. I am pretty sure the L.A is going to win this because we have best local players in the world. LA players will have incredible power fighting in LA! Liverpool is just a second-rated team in the Europe. The can't even make it to the first four place in the Premier League...\""

    G "\"Time to stop guys. We still have 20 minutes to go. Why don't we slience and see what is going on tonight. \""

    scene bar
    with dissolve


    return
