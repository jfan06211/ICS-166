# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define N = Character("Narrator")
define L = Character("Lyra")
define G = Character("Calliope")
define LB = Character("Lizardmen Bandits")
define B = Character("Ben")
define P = Character("[Protagonist]")
define unknown = Character("???")
define N = Character("Narrator")
define HS = Character("House System")
define cleanBot = Character("Clean Bot")
define LV = Character(“Terry”)

# Custom transitions
define flash = Fade(0.1, 0.0, 0.5, color="#fff")


# The game starts here.
label start:
    # Chapter 1
    stop music fadeout 1.0
    "..."
    "Where...am I?"
    unknown "...Look at our baby honey! Isn't it just the most adorable thing?"
    "Whose voice is that...?"
    unknown "Oh look how big our baby is! What should we name it?"
    "Name..."
    $ Protagonist = renpy.input("What is your name?", length=32)
    $ Protagonist = Protagonist.strip()
    if not Protagonist:
        $ Protagonist = "Player"
    unknown "Let’s name it [Protagonist]! Okay baby, you’re [Protagonist] from now on okay?"
    "That name...isn't that my nam-"
    unknown "[Protagonist]!!"
    scene bedroom with vpunch
    P "W-haaa!!"
    "I'm in my room...?"
    unknown "Jeez, I thought you would never wake up. It’s morning y’know?"
    show lyra normal with dissolve
    P "Lyra..."
    "Oh right...That was a dream."
    L "[Protagonist]?"
    L "Are you still half-asleep? You're spacing out."
    P "Oh no, don't worry! I was just thinking about my dream. No big deal!"
    L "Dream?"
    L "Well that's fine I guess."
    L " It's already morning, the beautiful sun's out. Don't you have work today?"
    "Lyra. My caretaker given by our government."
    "She is a wonderful, caring person who took care of me ever since I was born. I don’t have a family. No one in the city has a family, we are all taken care of by our caretakers. You could say they’re our only family."
    P "Oh you're right. I have a meeting today."
    L "Go on ahead and wash your face whenever you're ready."
    L "I already prepared breakfast, just come to the living room whenever you're hungry!"
    hide lyra normal with dissolve
    "Lyra stood up to open the blind next to my bed. A beautiful sunlight shines through the window."
    "Ah. Another bright day."
    "As I look out the window, flying cars zoom by the blue sky."
    P "Looks like this is going to be another peaceful day."
    P "System Theme Activation: Pseudo Change Favorite Sequence 1."
    HS "System Themes require permission. Grant access?"
    P "Granted."
    with flash
    with flash
    HS "Request accepted. Changing."
    scene bedroomchangeday with pixellate
    HS "Theme change complete."
    "Perfect"
    show lyra normal at left with moveinleft
    L "How come you always like to change the theme of your room into an older-style Japanese theme?"
    L "It looks like the 21st century in here."
    P "It looks cool doesn't it?"
    "I've been studying world history, and found great interest in the wooden styles of the 21st centuries."
    "Great architectural designs too."
    L "I prefer the look of more modern rooms, but I do agree the vintage atmosphere is very nice."
    hide lyra normal with moveoutleft
    "My room is currently holographically mirroring the image of an older-style Japanese-themed room due to one of the systems implemented in this house by the previous owner."
    "Based on my interests, I can remodel my room to be anything I like, and it will shape itself into the splitting image I imagine."
    show lyra normal with dissolve
    L "Don’t forget to eat your breakfast! I’m going to go now."
    show lyra normal at right with move
    hide lyra normal with dissolve
    "I nod, and we waved goodbye to each other. Lyra’s face smiles brightly as she departs."
    scene diningroom with fade
    hide bedroomchangeday
    "I came out to the living room, and ate the breakfast Lyra cooked for me."
    "Blueberry pancakes with sunny side up eggs and bacon. Classic."
    "I’m currently living in a house near Garden Land Trailhead, one of the quietest parts of the city with its famous hiking trails."
    "It’s a one-story house, big enough for 2 residents, but maybe a little too big for one. The best feature of this house is its ability to stay warm throughout the year. Never too cold. Never too hot."
    "Its walls are made with a mixture of cement and pserium, a magical powder developed by the Governmental Laboratory used to maintain stability and give it ideal conditions throughout the season."
    "We are really living up to the technologies these days."
    unknown "Master, I have finished cleaning duties."
    P "Hm?"
    show cleanbot normal with moveinright
    "As I looked to my right to where the voice came from, a tall human-like android stood in front of me dressed in a suit."
    "It's the cleaning bot that was included with this house Lyra gave me a few years back."
    show cleanbot talk
    cleanBot "Do you have any more requests, sir?"
    P "No, you can rest."
    cleanBot "Yes, Master."
    hide cleanbot talk with dissolve
    "The android makes its way to the wall next to my room and turns itself into a small, circular object tucked neatly away into a shelf."
    P "I guess it's time to go to work."
    "I put away my plate into the automatic cleaning sink, and head back to my room."
    scene bedroomchangenightlight with Fade(0.5,2.0,0.5)
    hide diningroom
    "It is now 8:30pm in the evening as I call off my job's meeting and shut down my computer."
    "Thinking about nothing, I laid down on my bed."
    P "That meeting was longer than I thought...Looks like it will be a busy day tomorrow working on that new website for my client."
    "Hmm..."
    P "Maybe a little jog wouldn't hurt to keep my blood flowing."
    "I stood up to get a hoodie in my closet before heading outside"
    scene bedroomchangenight
    hide bedroomchangenightlight
    scene nightsky with Fade(0.5,2.0,0.5)
    hide bedroomchangenight
    "The night sky was still, and the light from the moon shines down the trail as I jog."
    "I keep my breath steady as the cold wind blow against my face with a freezing touch. The heat generated through my enery extertion slowly warms my face up."
    #scene gardenlandtraillight
    P "Wait a minute."
    "In the corner of my eye, I saw a faint shimmer of light deep within the hills."
    P "What is that...?"
    #play music enginesound
    "A loud engine starts hovering behind me."
    P "What's that soun-"
    menu:
        "Turn around":
            #play music whoosh
            "As I turned to look back, a truck flew over me at high velocity."
            "Its generated wind blew at me with full force."
            jump Ch1_continue
        "Keep running":
            "...Maybe it's nothing."
            #play music engineroarslouder
            "A truck flew over me at high velocity."
            "Its generated wind blew at me with full force."
            jump Ch1_continue
        "Stop":
            "I halted my jog and turned to where the sound came from."
            "To my surprise, a huge truck flew over me with great velocity."
            "Its generated wind blew at me with full force."
            "Taken by surprise, I stepped back."
            jump Ch1_continue

label Ch1_continue:
    P "Woahh, look at the size of that thing! It’s the newest truck model! That actually looks so coo-"
    "My leg slided on a pebble on the edge of the trail."
    P "W-woa..h..!!"
    "I tip over the side of the trail, my body swirling in motion as I roll down the slope of the trail into the bottom of the hill."
    "Everything is spinning."
    "All until it abruptly stop as the impact from the fall forcefully struck a tree."
    #play music THUD
    with vpunch
    P "Argh!"
    "My body jolted in pain as I slam myself into a tree."
    "Haven't felt something like this since the incident of me hitting my funny bone on the edge of a sofa."
    "Wasn't fun."
    P "Did I really trip on a rock while sidetracking..."
    "Well that was an event."
    #light in shack flickers
    P "What...is that?"
    "I slowly stood up, with the pain lingers, as I strive to take a closer look at the flickering light."
    P "Is that a shack?"
    "I move forward towards the light, and what stood upon me was an old, rusty shack."
    P "Looks abandoned...Is anyone there?"
    "...No response."
    P "Hm..."
    menu:
        "Peek between the cracks of the door.":
            "I peeked between the cracks of the door and saw some sort of flickering light emitting from an object."
            jump Ch1_enterShack
        "Knock on the door.":
            #play music knockknockknock
            "I knocked on the door several times."
            P "Hm...still no response. I guess it really is abandoned."
            jump Ch1_enterShack
        "Open door.":
            jump Ch1_enterShack

label Ch1_enterShack:
    "I opened the door and walked towards the flickering object."
    P "A mirror...?"
    "I looked inside the mirror and the light grew brighter."
    "Then a clear image came to view."




    #Chapter 2
label chapter2_start:
    P "\"What is this thing? It seems like a door that connects to another place. \""

    "\"Let me see if I can push it...\""

    "..."

    "\"What happened? Did I just take a nap? \""

    "\"Some strong light is shining on my face that I can't open my eyes.\""

    "\"But the light feels so familiar.\""

    "......"

    "\"Isn't it the light in my room?!\""

    "I try to block the light using my hands and finally I can open my eyes just a little bit."

    "\"Brown chairs, empty lockers...\" It seems like I am in my room."

    "\"The blue mirror... Wait! The mirror! \""

    "\"I passed out because I tried to push the mirror! \""

    "I held the bed and got up from the ground."

    "\"blzzzz blzzzzzz blzzzzzzzz\" The doorbell starts screaming"

    "\"Who is this? I don't remember someone is going to see me at this time.\" I start become curious while I open the door"

    G "\"What's up [Protagonist]! Are you ready for the Champions League Final? We gotta go fast before the seats run out!\""

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

    P "\"I think I am better not going to the bar since I haven't been to any bar…\""

    G "\"Bro, you should really try some good drinks in the bar. I guarantee you’ll love the place once you get there. \""

    jump chapter2_bar

label chapter2_pretend:

    G "\"Don't forget to grab your jacket! It is a little bit cold in the bar. They always set the temperature low. \""

    P "\"Wait are we going to a bar? It there a age limit here?\""

    G "\"No one cares about the age limit! If you can speak, you are legal to get a drink now. By the way, which team has a better chance to win this time? \""

    P "\"Man City is definitely going to win this time. They have the Premier League already and the final is just another hard battle for Chelsea...\""

    G "\"Wait wait wait...Are you from 2021 or something? It is the year (time holder). It's the L.A versus Liverpool! \""

    P "How can the L.A faces Liverpool in Champions League? They are not on the same continent!"

    "And if this is year (time holder), am I in a different world? But look at my table, Lyra, the mirror..."

    G "\"Yo! Stop zoning out! We won't have a place to sit if we are late! \""

    jump chapter2_bar

label chapter2_bar:

    N "[Protagonist] and the Guide is on their way to the bar \"Frolic Room\"."

    show ben normal

    B "\"Hey you guys! Are you guys also going to watch the final? \""

    G "\"Oh hi Ben! Are you going too? Would you like to join us? We are going to the Forlic Room! \""

    B "\"Sure! Watching soccer game in the Forlic Room could be cool. Do you guys think the L.A can win this final? \""

    P "\"Based on my experience, Liverpool is going to win easily. They were the champion of the last year. The L.A is just an average team in MLS. They are not going to have any chances. \""

    B "\"Dude, the L.A is not like 500 years ago. I am quite sure the L.A is going to win this because we have best local players in the world. LA players will have incredible power fighting in LA! Liverpool is just a second-rated team in the Europe. They can't even make it to the first four place in the Premier League...\""

    G "\"Time to stop guys. We still have 20 minutes to go. Why don't we silence and see what is going on tonight. \""

    scene bar
    with dissolve

    N "[Protagonist], the Guide, and Ben has arrived \"Frolic Room\"."

    "Although they arrived at the bar 10 minutes earlier than the match starts, the seats are already full."

     “Fans that support the L.A arrived exceptional early. As a result, they occupy ¾ of seats while Liverpool fans can only get about ¼.”
     
     “People start betting on the bar table. Looks like 70% of people think the L.A is going to win.”
     
     G “\”Looks like we are late. Ben, can you take [Protagonist] to a spot that we can stand comfortably? I am going to get you some drinks.\””
     
     B “\”Sure. It would be nice if we have Heineken.\”” 
     
     N “10 minutes later, the match officially starts. The [Protagonist] party watches the game in the middle of the bar.”
     
     P “\”I am so excited right now. I hope I can watch every match in this bar starting now. The atmosphere is just so good!\””
     
     G “\”Told ya.\””
     
     N “When the time comes to 35 minutes, Gordon scores with a free kick! It is also the first goal that the L.A scores in Champions Final!”
     
     “Fans of the L.A start cheering. They jump up from chairs and begin playing “waves”. On the other side, Liverpool fans don’t expect this goal. They finish their drinks and start asking the bartender for more beer.”
     
     “One of the Liverpool fan tries to cheer up his companion.”
     
     LV “\”Hey! It is just a lucky goal for them! I believe we are going to in at the end! Let’s go REDS!\””
     
     N “Some of the L.A fans heard Terry’s talk and start laughing.”
     
     LB “This is LA! No one can beat the L.A in LA!”
     
     #some transition is needed
     
     N “Henderson scores for Liverpool just before half time. The score becomes 1-1.”
     
     LV “\”I told you folks. This is the first step to win.\””
     
     N “The L.A fans look unhappy about the score. They discuss the potential foul that happened before Henderson’s shot while the break.”
     
     G “\”I think the L.A players did a good job in the first half. The manager might need to consider placing one more mid field player to increase the possession.\”
     
     B “\”Nah. We need to substitute forward players at around 60 minutes. The startups look a little bit tired.\””
     
     P “\”Liverpool is going to win if they keep playing this counterattack strategy. 
     
     LB “\”Hey! You! Little Guy! Stop talking that loser “Liverpoor”! They are not going to beat us! No matter what strategy they are using!\””
     
     G “\”[Protagonist], they are the gang that controls almost all bars. Let’s just shut up and wait for the second half.\”” 
     
     P “Hmm. Then it is not surprise that they always talk like that. “
     
     # some transition is needed
     
     N “The second half has started. The L.A choose to replace one of their Midfielder with a Forward to ensure they give enough pressure to Liverpool. At the meantime, Liverpool doesn’t make any changes. It seems like their manager is pretty satisfied with the startups.”
     
     N “After another 45 minutes, the score is still 1-1. In the last attack, Liverpool has its corner. It might be the last chance for Liverpool to end the game here.”
     
     N “Almost everyone in the bar stands up and staring at the screen. Some of the Liverpool fans are so nervous that they turn their face backward and start praying.”
     
     “Goalkeeper Alison from Liverpool side ran across the whole field and see if he can do something in this final attack.”
     
     “The referee blows the whistle. The ball is now flying to the penalty area…”
     
     “GOALLLLLLLLLLLLLL! Liverpool has scored! Alison gave a powerful header and sent the ball into the net!”
     
     
    return
