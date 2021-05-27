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
define LV = Character("Terry")

#music definition

define audio.ominous01 = "audio/BTR-Ominous-01.mp3"

# Custom transitions
define flash = Fade(0.1, 0.0, 0.5, color="#fff")


# The game starts here.
label start:
    # Chapter 1
    stop music fadeout 1.0
    "..."
    "Where...am I?"
    unknown "\"...Look at our baby honey! Isn't it just the most adorable thing?\""
    "Whose voice is that...?"
    unknown "\"Oh look how big our baby is! What should we name it?\""
    "Name..."
    $ Protagonist = renpy.input("What is your name?", length=32)
    $ Protagonist = Protagonist.strip()
    if not Protagonist:
        $ Protagonist = "Player"
    unknown "\"Let’s name it [Protagonist]! Okay baby, you’re [Protagonist] from now on okay?\""
    "That name...isn't that my nam-"
    unknown "\"[Protagonist]!!\""
    scene bedroom with vpunch
    P "\"W-haaa!!\""
    "I'm in my room...?"
    unknown "\"Jeez, I thought you would never wake up. It’s morning y’know?\""
    play music "audio/daytimetheme.mp3"
    show lyra normal with dissolve
    P "\"Lyra...\""
    "Oh right...That was a dream."
    L "\"[Protagonist]?\""
    L "\"Are you still half-asleep? You're spacing out.\""
    P "\"Oh no, don't worry! I was just thinking about my dream. No big deal!\""
    L "\"Dream?\""
    L "\"Well that's fine I guess.\""
    L "\"It's already morning, the beautiful sun's out. Don't you have work today?\""
    "Lyra. My caretaker given by our government."
    "She is a wonderful, caring person who took care of me ever since I was born. I don’t have a family. No one in the city has a family, we are all taken care of by our caretakers. You could say they’re our only family."
    P "\"Oh you're right. I have a meeting today.\""
    L "\"Go on ahead and wash your face whenever you're ready.\""
    L "\"I already prepared breakfast, just come to the living room whenever you're hungry!\""
    hide lyra normal with dissolve
    "Lyra stood up to open the blind next to my bed. A beautiful sunlight shines through the window."
    "Ah. Another bright day."
    "As I look out the window, flying cars zoom by the blue sky."
    P "\"Looks like this is going to be another peaceful day.\""
    P "\"System Theme Activation: Pseudo Change Favorite Sequence 1.\""
    HS "\"System Themes require permission. Grant access?\""
    P "\"Granted.\""
    with flash
    with flash
    HS "\"Request accepted. Changing.\""
    scene bedroomchangeday with pixellate
    HS "\"Theme change complete.\""
    "Perfect"
    show lyra normal at left with moveinleft
    L "\"How come you always like to change the theme of your room into an older-style Japanese theme?\""
    L "\"It looks like the 21st century in here.\""
    P "\"It looks cool doesn't it?\""
    "I've been studying world history, and found great interest in the wooden styles of the 21st centuries."
    "Great architectural designs too."
    L "\"I prefer the look of more modern rooms, but I do agree the vintage atmosphere is very nice.\""
    hide lyra normal with moveoutleft
    "My room is currently holographically mirroring the image of an older-style Japanese-themed room due to one of the systems implemented in this house by the previous owner."
    "Based on my interests, I can remodel my room to be anything I like, and it will shape itself into the splitting image I imagine."
    show lyra normal with dissolve
    L "\"Don’t forget to eat your breakfast! I’m going to go now.\""
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
    unknown "\"Master, I have finished cleaning duties.\""
    P "\"Hm?\""
    show cleanbot normal with moveinright
    "As I looked to my right to where the voice came from, a tall human-like android stood in front of me dressed in a suit."
    "It's the cleaning bot that was included with this house Lyra gave me a few years back."
    show cleanbot talk
    cleanBot "\"Do you have any more requests, sir?\""
    P "\"No, you can rest.\""
    cleanBot "\"Yes, Master.\""
    hide cleanbot talk with dissolve
    "The android makes its way to the wall next to my room and turns itself into a small, circular object tucked neatly away into a shelf."
    P "\"I guess it's time to go to work.\""
    "I put away my plate into the automatic cleaning sink, and head back to my room."
    stop music fadeout 1.0
    scene bedroomchangenightlight with Fade(0.5,2.0,0.5)
    hide diningroom
    play music "audio/night_theme.mp3"
    "It is now 8:30pm in the evening as I call off my job's meeting and shut down my computer."
    "Thinking about nothing, I laid down on my bed."
    P "\"That meeting was longer than I thought...Looks like it will be a busy day tomorrow working on that new website for my client.\""
    "Hmm..."
    P "\"Maybe a little jog wouldn't hurt to keep my blood flowing.\""
    "I stood up to get a hoodie in my closet before heading outside"
    scene bedroomchangenight
    hide bedroomchangenightlight
    scene nightsky with Fade(0.5,2.0,0.5)
    hide bedroomchangenight
    "The night sky was still, and the light from the moon shines down the trail as I jog."
    "I keep my breath steady as the cold wind blow against my face with a freezing touch. The heat generated through my enery extertion slowly warms my face up."
    #scene gardenlandtraillight
    P "\"Wait a minute.\""
    "In the corner of my eye, I saw a faint shimmer of light deep within the hills."
    P "\"What is that...?\""
    #play music enginesound
    "A loud engine starts hovering behind me."
    P "\"What's that soun-\""
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
    P "\"Woahh, look at the size of that thing! It’s the newest truck model! That actually looks so coo-\""
    "My leg slided on a pebble on the edge of the trail."
    P "\"W-woa..h..!!\""
    "I tip over the side of the trail, my body swirling in motion as I roll down the slope of the trail into the bottom of the hill."
    "Everything is spinning."
    "All until it abruptly stop as the impact from the fall forcefully struck a tree."
    #play music THUD
    with vpunch
    P "\"Argh!\""
    "My body jolted in pain as I slam myself into a tree."
    "Haven't felt something like this since the incident of me hitting my funny bone on the edge of a sofa."
    "Wasn't fun."
    P "\"Did I really trip on a rock while sidetracking...\""
    "Well that was an event."
    #light in shack flickers
    P "\"What...is that?\""
    "I slowly stood up, with the pain lingers, as I strive to take a closer look at the flickering light."
    P "\"Is that a shack?\""
    "I move forward towards the light, and what stood upon me was an old, rusty shack."
    P "\"Looks abandoned...Is anyone there?\""
    "...No response."
    P "\"Hm...\""
    menu:
        "Peek between the cracks of the door.":
            "I peeked between the cracks of the door and saw some sort of flickering light emitting from an object."
            jump Ch1_enterShack
        "Knock on the door.":
            #play music knockknockknock
            "I knocked on the door several times."
            P "\"Hm...still no response. I guess it really is abandoned.\""
            jump Ch1_enterShack
        "Open door.":
            jump Ch1_enterShack

label Ch1_enterShack:
    "I opened the door and walked towards the flickering object."
    P "\"A mirror...?\""
    "I looked inside the mirror and the light grew brighter."
    "Then a clear image came to view."




    #Chapter 2
label chapter2_start:
    P "\"What is this thing? It seems like a door that connects to another place. \""

    "\"Let me see if I can push it...\""
    stop music fadeout 1.0
    with flash
    with flash
    scene bedroomchangeday with flash

    "..."

    "\"What happened? Did I just take a nap? \""

    "\"Some strong light is shining on my face that I can't open my eyes.\""

    "\"But the light feels so familiar.\""

    "......"
    play music "audio/BTR-Ominous-01.mp3"

    "\"Isn't it the light in my room?!\""

    "I try to block the light using my hands and finally I can open my eyes just a little bit."

    "\"Brown chairs, empty lockers...\" It seems like I am in my room."

    "\"The blue mirror... Wait! The mirror! \""

    "\"I passed out because I tried to push the mirror! \""

    "I held the bed and got up from the ground."

    stop music fadeout 1.0

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

    "Fans that support the L.A arrived exceptional early. As a result, they occupy ¾ of seats while Liverpool fans can only get about ¼."

    "People start betting on the bar table. Looks like 70 percent of people think the L.A is going to win."

    G "\"Looks like we are late. Ben, can you take [Protagonist] to a spot that we can stand comfortably? I am going to get you some drinks.\""

    B "\"Sure. It would be nice if we have Heineken.\""

    N "10 minutes later, the match officially starts. The [Protagonist] party watches the game in the middle of the bar."

    P "\"I am so excited right now. I hope I can watch every match in this bar starting now. The atmosphere is just so good!\""

    G "\"Told ya.\""

    N "When the time comes to 35 minutes, Gordon scores with a free kick! It is also the first goal that the L.A scores in Champions Final!"

    "Fans of the L.A start cheering. They jump up from chairs and begin playing “waves”. On the other side, Liverpool fans don’t expect this goal. They finish their drinks and start asking the bartender for more beer."

    "One of the Liverpool fan tries to cheer up his companion."

    LV "\"Hey! It is just a lucky goal for them! I believe we are going to in at the end! Let’s go REDS!\""

    N "Some of the L.A fans heard Terry’s talk and start laughing."

    LB "This is LA! No one can beat the L.A in LA!"

    #some transition is needed

    N "Henderson scores for Liverpool just before half time. The score becomes 1-1."

    LV "\"I told you folks. This is the first step to win.\""

    N "The L.A fans look unhappy about the score. They discuss the potential foul that happened before Henderson’s shot while the break."

    G "\"I think the L.A players did a good job in the first half. The manager might need to consider placing one more mid field player to increase the possession.\""

    B "\"Nah. We need to substitute forward players at around 60 minutes. The startups look a little bit tired.\""

    P "\"Liverpool is going to win if they keep playing this counterattack strategy.\""

    LB "\"Hey! You! Little Guy! Stop talking that loser “Liverpoor”! They are not going to beat us! No matter what strategy they are using!\""

    G "\"[Protagonist], they are the gang that controls almost all bars. Let’s just shut up and wait for the second half.\""

    P "Hmm. Then it is not surprise that they always talk like that. "

    # some transition is needed

    N "The second half has started. The L.A choose to replace one of their Midfielder with a Forward to ensure they give enough pressure to Liverpool. At the meantime, Liverpool doesn’t make any changes. It seems like their manager is pretty satisfied with the startups."

    N "After another 45 minutes, the score is still 1-1. In the last attack, Liverpool has its corner. It might be the last chance for Liverpool to end the game here."

    N "Almost everyone in the bar stands up and staring at the screen. Some of the Liverpool fans are so nervous that they turn their face backward and start praying."

    "Goalkeeper Alison from Liverpool side ran across the whole field and see if he can do something in this final attack."

    "The referee blows the whistle. The ball is now flying to the penalty area…"

    "GOALLLLLLLLLLLLLL! Liverpool has scored! Alison gave a powerful header and sent the ball into the net!"

    "Liverpool fans starts cheering. Although they only occupied 1/4 of the bar, the noise they create can actually lift the roof."

    LV "\"YES!!!!!We are the champion folks! This is our 7th Champions League title! I've waited for so many years!\""

    N "On the other hand, all L.A fans are stunned. Some of them use hands to cover their face. They still can't believe this happened."

    LB "\"This is not fair! The L.A can't lose! It must be the referee! They let Liverpool win so that they can put millions of dollars into their pocket! They do this every year! The Champions League is all fake...\""

    LV "\"Yo calm down guys. You guys did great tonight. It is just us being lucky.\""
    #Some bad words are coming out
    LB "\"Shut up, you British pig! You are saying this because Liverpool wins. Just get out of this place! We are not happy to see you! Ugly  Red fans!\""

    LV "\"This is not nice. How about you get off this bar, loser?\""

    LB "\"How dare you! You want a fight? Let's fight!\""

    G "\"Damn. This is not good. We have better leave.\""

    B "\"Yeah. Let's finish our drink fast and go.\""

    P "\"What? Are we leaving now? This fight haven't begun, yet! Don' worry too much. It should be just a normal bar fight.\""

    G "\"No no no. Bar fights are not the normal fight you see on TVs. This is the part you don't want to experience.\""

    "\"Let's just go before we can't.\""

    N "More and more drunk people heard there is a fight in Frolic Room and trying to squeeze in to see what happened."

    B "\"I think we are late. There is no way out now. All of the exits are blocked by crowd. We have better start moving to one of the exits can see if we can go through them.\""

    P "\"Don't think too much. It is just a fight after match. Just enjoy it.\""

    G "\"Let's hope it is a normal fight...\""

    N "Before the Guide finish his words, a giant fire ball pass by and burn the TV out on the wall."

    P "\"Woah. What is that?\""

    B "\"Looks like the fire ball is from the Fire Lizard.\""

    P "Lizard? Isn’t Lizard a kind of animal? How does it relate to fire?"

    "Let me get closer and see…"

    N "While the [Protagonist] is getting closer to the fighting stage, an ice arrow comes out of nowhere and pierces the wall."

    G "\"Yo [Protagonist]! Stop moving backwards!\""

    N "[Protagonist] didn’t hear the Guide because the crowd is getting crazy. Everyone is cheering for the fighters and some friends of Lizardmen Bandits is sniping Terry so that they can win the fight."

    "As [Protagonist] moving, he finds out that the ice arrow is from a semi-transparent frog. "

    P "Wow, I have never seen animals like this. They seem like the minions from movies."

    LB "\"I like your minion. It looks strong. But I am going to kill you and it will be mine! Hahahahahaha…\""

    LV "\"Don’t ever think about it, loser. \""

    N "Suddenly, someone from crowd throws a flash bang and [Protagonist] can’t see anything."

    "After [Protagonist] open his eyes, the fight has already started."

    "Lizardmen Bandits and Terry is fighting in the middle of the bar while their minions are also fighting using their magic power. They use whatever is near them to attack and defense."

    "The bar is completely in chaos. Chairs, knives, and bottles are flying in the Frolic Room."

    "Suddenly, someone catches [Protagonist]’s arm and trying to drag him out of the frontline."

    P "\"It’s you, Ben! I’ve never seen a fight like this! They are so cool!\""

    B "\"Yes they are. But we need to leave. It is unsafe here…\""

    N "While Ben is trying to convince [Protagonist], a stone-made arrow launches and pierces Ben’s body. "

    #Chapter 2 Ends

    #Chapter 3 Begins
label chapter3_start:
    "I couldn’t stop staring at Ben. He was a complete mess, but it went beyond his usual dirt-filled attire."

    "He had collapsed on the floor. His tanned clothes were now stained red. His tousled hair was drenched in sweat. The arrow still pierced through his body."

    "His expression was one I had never seen before. His eyes were barely open, not seeming to be looking at anything at all. His mouth was agape, and his breathing was raspy and uneven."

    "What was wrong with him?"

# choice 1
menu:
    "Continue to Stare":
        jump ch3_con_to_stare

    "Grab the Arrow":
        jump ch3_arrow

    "Talk to Ben":
        jump ch3_talk_to_ben

label ch3_con_to_stare:
    G "What the hell are you standing around for?!"

    P "Huh? I just -"

    jump ch3_endchoice1

label ch3_arrow:
    G "Stop that! Let me handle it."

    P "Oh, sorry, I just-"

    jump ch3_endchoice1

label ch3_talk_to_ben:
    P "Ben? Come on, get up. You're... making me uncomfortable."

    "There was no response. Ben didn't even look at me."

    G "[Protagonist], what are you doing?!"

    P "Huh? I was just -"

label ch3_endchoice1:
    G "Nevermind that. Help me get him out of here."

    "Calliope grabbed Ben by the shoulders, and I grabbed him by the legs. He was much lighter than I expected."

    # ADD BLACK SCENE TRANSITION HERE

    "We took Ben and left the bar quickly and quietly. We looked for a quiet, open space, and finally ducked behind an alley a couple of buildings away."

    # ADD NEW SCENE HERE

    "We laid Ben down on the pavement. I thought about how uncomfortable the cold, hard ground must be, but Ben didn’t seem to notice."

    "Calliope swung her bag out from around her shoulders and placed it on the floor. From the bag she took out a long, ragged piece of cloth."

    "I watched as she carefully removed the arrow from Ben’s body, and then wrapped the cloth around Ben’s stomach. Then, she took out a plastic canteen and held it to his lips."

    G "Come on Ben, you’ll be alright. Everything will be okay. Stay with me now."

    "Calliope’s voice didn’t sound right. Its usual confidence and strength was gone, replaced by something that seemed to be breaking apart."

    "Ben wasn’t acting right either. No responses. No eye contact. He wasn’t even trying to take a sip of water."

# choice 2
menu:
    "Continue to Stare":
        jump ch3_con_to_stare_2

    "Talk to Calliope":
        jump ch3_talk_to_cal_2

    "Talk to Ben":
        jump ch3_talk_to_ben_2

label ch3_con_to_stare_2:
    "I continued to stare at Ben, laying on the ground. His only movement came from his barely noticeable breaths. The look on Calliope’s face was one I had never seen on her before."

    "Her expression was panicked, her eyes were watering, and she kept mumbling, begging Ben to stay here."

    "I didn’t understand. Where was Ben going? How could someone be going somewhere when they didn’t move at all. Nothing was making sense."

    "I suddenly felt very out of place. The reality of being in a completely different world, with completely different rules and ideas began to hit me. What was happening? What was I doing here?"

    "Maybe I need to go. Maybe I wasn’t ever meant to be here."

    "Before I could really consider leaving, Calliope began to cry out."

    jump ch3_endchoice2

label ch3_talk_to_cal_2:
    P "Calliope? What’s going on? I don’t understand."

    "Calliope turned and glared at me."

    G "What’s there not to understand?! Ben is.. He’s…"

    "She stopped talking to me, turning back to Ben."

    G "Please Ben, please just stay a little longer and I can get help."

    jump ch3_endchoice2

label ch3_talk_to_ben_2:
    P "Ben? What’s wrong? Can you get up and talk to us?"

    "Again, Ben was silent. No sign that he even heard me at all."

    "Before I could say another word, Calliope began to cry out."

label ch3_endchoice2:
    G "Ben? Ben!? No no no... Please we need you."

    "Calliope was sobbing now. Tears were running down her face. I looked at Ben again. His raspy breaths had stopped, replaced with nothing but silence. His eyes were glassy, still staring at nothing."

    "Calliope stopped crying out and took a deep breath. She wiped the tears from her face. Then, she took her hand and gently closed Ben’s eyes."

    G "I’m sorry..."

    P "Calliope? What’s going on?"

    "Calliope turned to me suddenly. Immediately, the pain appeared in her face again, mixed in with a fierce anger."

    G "What is wrong with you?!"

    P "Huh? What do you-"

    G "Just GO AWAY! You need to leave."

    "I didn’t have words to respond. Why was she being like this?"

    G "If it weren’t for you, Ben would still be here!"

# Choice 3
menu:
    '"Ben is still here."':
        jump ch3_ben_is_here_3

    '"Fine, I\'ll leave."':
        jump ch3_fine_ill_leave_3

label ch3_ben_is_here_3:
    G "What the hell is wrong with you!? He’s DEAD. Can’t you see that?! He’s DEAD and it’s all YOUR FAULT."

    G "We’ve been risking our lives bringing you along, because you’re too stupid to understand basic common sense. And now enough is enough. You need to leave before you kill someone else too."

    G "Ben would still be here if it weren’t for you — if it weren’t for me bringing you along."

    G "You don’t belong here. Go back to wherever you came from and don’t come back. You’ve done enough here."

    "Calliope stopped looking at me. I thought about responding, but I had no words and I doubted anything I said would make a difference."

    jump ch3_endchoice3

label ch3_fine_ill_leave_3:
    G "Finally. The first reasonable thing you’ve ever said. Now don’t say another word. Just go."

label ch3_endchoice3:
    "There was only one thing to do. It seemed my journey in this world was done now. There was no point in staying around."

    # ADD BLACK SCREEN TRANSITION HERE
    "It was a quiet, lonely walk back to the mirror."

    # End of Chapter 3

    #Chapter 4

label chapter4_start:
    #show home environment

    scene bedroom with dissolve

    "I was home. Despite having seen, heard, and felt things I never had before, I wound up in this familiar place as usual. Here, in my room, with nothing in front of me but my usual daily activities."

    "But one thing was different."

    "I looked at the mirror, still in my hand, and thought about what I had just experienced. This mirror hadn't given me any information about its purpose or where it came from, but it did give me information about myself."

    "I thought about the way my heart started beating faster when Ben fell to the ground. The way my eyes darted around, searching for some way to stop what I was feeling. I didn't like that feeling."

    "And yet... I needed to know more about it."

    scene daysky with dissolve
    hide bedroom

    "I decided to take the mirror to the appeals office located a short walk away from where I lived. I knew how to get there thanks to lessons from when I was younger."

    "Lyra said that if anything went wrong, the appeals office was the place to go. All I would have to do was walk out of my residence, turn left, and keep walking until I got there."

    "I'd never been there before because, well... nothing had ever gone wrong."

    "Once I had been walking for a few minutes, I saw a very small building in front of me, appearing almost out of nowhere."

    "I immediately knew I was in the right place thanks to two things:"

    "a sign that read \"Appeals\" in bold red lettering displayed on the front of the office, and the fact that this building was the only one that looked nothing like the residences scattered throughout the rest of the area."

    scene appeals with fade
    hide daysky
    play music ominous01 loop

    "I walked through the front door and immediately noticed the lack of furnishings inside. In my residence, I have a place to sit, stand, or sleep when I wish."

    "In this appeals office, there wasn't a single chair to be seen, nor a sign directing me to the appropriate place to report the mirror."

    "It was as if this place was designed never to be used, only seen from the outside."

    "I walked a few steps into a narrow hallway filled with nothing but gray walls until I noticed a person sitting behind a desk further down the hall."

    "Their eyes were completely blank, focused on nothing in particular. When I walked up to them, they jumped in their seat, urging me to take a step back myself. My heart started beating just a bit faster, reminding me of my time with the guide."

    P "I'd like to ask you about this strange object I found. I've never been here before, and I'm not sure exactly how this process works, but I've brought it here in the hopes that you can help me with it... whatever it is."

    "I pulled the mirror from my pocket and placed it on the desk, and the person before me almost immediately started breathing heavily. Their eyes widened, their expression changed, and they couldn't say a word for a moment or two."

    "At this point, for a brief moment, I saw a familiar look in their eyes. They looked a bit like Ben did when he became hurt."

    "After some hesitation, they reached over and pressed a small red button. I heard a click and a high-pitched beep, and then waited for a moment. The person behind the desk still hadn't said anything, but I knew that something wasn't quite right."

    "Suddenly, a flash of light appeared and dust was swiftly scattered from the surrounding area. After the light was gone, I saw Lyra standing before me."

    "She looked at the person behind the desk, looking confused."

    L "What's the problem, hmm?"

    "Still refusing to speak, they simply pointed at the mirror I had placed on the desk with that same intense look in their eyes."

    "Lyra looked at the mirror, and immediately became still. There was a long pause before she did anything else, as if the mirror had some kind of hold on her."

    "After a moment, she looked directly at me, and started speaking in her familiarly polite voice."

    L "Where did you get that mirror?"

    "I realized how little I'd been posed with questions throughout my life, but also how little I'd asked them. I'd never needed to find an answer. I found myself unable to speak, as if the same force controlling the employee had suddenly been transferred to me."

    L "Can you hear me? Hello? Where did this come from?"

menu:

    "Say Nothing":
        jump chapter4_saynothing

    "Lie":
        jump chapter4_lie

label chapter4_saynothing:

    "I said nothing."

    "She picked up the mirror and took a few steps toward me, holding the object in front of my face."

    L "At least tell me this... Have you... used this mirror? Did anything happen while it was in your possession?"

    "For the first time in my life, I saw the plain, simple smile that Lyra always wore leave her face... replaced by something I could just barely recognize."

    L "Answer me!"

    "She reminded me of the guide I'd met before. Looking at me with a narrow gaze, asking me something I couldn't quite bring myself to answer, disturbed by my lack of cooperation, and refusing to put up with it for much longer."

    "All I could do was shake my head. The feeling she gave me wasn't pleasant, and I wanted it to be gone quickly."

    "She had an expression on her face that spelled out her displeasure in waiting for me, but I knew that if I told Lyra my story, I likely would only make the feeling worse."

    "After finally getting an answer, she quickly sped up the conversation."

    jump chapter4_end

label chapter4_lie:

    P "I... umm... just found it a few minutes ago...I brought it here as soon as I did."

    L "Well where did you find it?"

    P "It was... just laying on the street. I didn't think much of it, but I brought it here just to be safe."

    "I don't know what made me want to lie. But I somehow knew things would've gone bad quickly had I told Lyra everything I had seen through the mirror."

    "I could feel my hand shaking, which startled me. Nothing had ever had quite the same effect on me."

    "I couldn't tell what Lyra would do next, but I knew I just wanted to go home as soon as possible."

    "I wanted to be away from this place, away from this sinking feeling in the pit of my stomach, away from any consequences Lyra would have for me if she found out I had lied to her."

    "After what seemed like an eternity, she finally spoke, and I couldn't describe with words how relieved I was once my hands stopped trembling."

    jump chapter4_end

label chapter4_end:

    stop music fadeout 2.0

    L "Okay! Well, I'm glad you found my mirror! If you have no further appeals to make, then I'll just take it back with me and send you on your way!"

    "Without a moment's notice, Lyra waved her hand in a fluid motion towards me, and now I was the one engulfed in a flash of light."

    scene bedroom with dissolve
    hide appeals

    "After it disappeared, I found myself back in my room once again."

    "I was tempted to resume my daily activities now that the mirror was in its proper place, but I couldn't help but wonder about what would happen next."

    "I'd used the mirror to see people and places I never had before, and wondered if Lyra had been using the mirror in that way. If so, for how long? And more importantly, why?"

    "I sat at my desk and let myself take in all that had happened recently. For the first time, I had serious questions on my mind."

    "For the first time, I wasn't sure how everything would turn out. And for the first time, I felt this strange desire take over my body."

    "Before all of this, I had gone through every day knowing how it would turn out, and never wondered about any other possibilities."

    "But sitting in my room, thinking about Ben, the guide, and Lyra's expressions throughout these events, I knew I wanted more."

    "I had felt things I liked, and many things I didn't like. But knowing that there could be more, that my guide was still out there, along with all of their associates and enemies, it caused something in me to change."

    "I wanted to see them again."

    #Chapter 4 END.





    return
