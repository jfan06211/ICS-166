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
define audio.ominous02 = "audio/BTR-Ominous-02.mp3"

# Custom transitions
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define fadehold = Fade(1.0, 1.0, 1.0)
define slowfade = Fade(3.0, 1.0, 3.0)
define slowfadehold = Fade(5.0, 1.0, 1.0)


# The game starts here.
label start:
    # Chapter 1
    stop music fadeout 1.0
    "..."
    scene dream_blur with dissolve
    "Where...am I?"
    scene dream_blur_sil1 with dissolve
    unknown "\"...Look at our baby honey! Aren't they just the most adorable thing?\""
    "Whose voice is that...?"
    scene dream_blur_sil2 with dissolve
    unknown "\"Oh look how big our baby is! What should we name them?\""
    "Name..."
    $ Protagonist = renpy.input("What is your name?", length=32)
    $ Protagonist = Protagonist.strip()
    if not Protagonist:
        $ Protagonist = "Player"
    unknown "\"Let’s name them [Protagonist]! Okay baby, you’re [Protagonist] from now on okay?\""
    "That name...isn't that my nam-"
    unknown "\"[Protagonist]!!\""
    scene bedroom with vpunch
    P "\"W-haaa!!\""
    "I'm in my room...?"
    unknown "\"Jeez, I thought you would never wake up. It’s morning y’know?\""
    play music "audio/daytimetheme.mp3" volume 0.8
    show lyra normal with dissolve
    P "\"Lyra...\""
    "Oh right...That was a dream."
    L "\"[Protagonist]?\""
    L "\"Are you still half-asleep? You're spacing out.\""
    P "\"Oh no, don't worry! I was just thinking about my dream. No big deal!\""
    L "\"Dream?\""
    L "\"Well that's fine I guess.\""
    L "\"It's already morning, the beautiful sun's out. Don't you have work today?\""
    "Lyra. My caretaker assigned by our government."
    "She is a wonderful, caring person who took care of me ever since I was born. I don’t have a family. No one in the city does. We are all taken care of by our caretakers. You could say they’re our only family."
    P "\"Oh you're right. I have a meeting today.\""
    L "\"Go on ahead and wash your face whenever you're ready.\""
    L "\"I already prepared breakfast, just come to the living room whenever you're hungry!\""
    hide lyra normal with dissolve
    "Lyra stood up to open the blinds next to my bed. A beautiful ray of sunlight shone through the window."
    "Ah. Another bright day."
    "As I looked out the window, flying cars zoomed by the blue sky."
    P "\"Looks like this is going to be another peaceful day.\""
    P "\"System Theme Activation: Pseudo Change Favorite Sequence 1.\""
    HS "\"System Themes require permission. Grant access?\""
    P "\"Granted.\""
    with flash
    with flash
    HS "\"Request accepted. Changing.\""
    scene bedroomchangeday with pixellate
    HS "\"Theme change complete.\""
    "Perfect."
    show lyra normal at left with moveinleft
    L "\"How come you always like to change the theme of your room into an older-style Japanese theme?\""
    L "\"It looks like the 21st century in here.\""
    P "\"It looks cool doesn't it?\""
    "I've been studying world history, and found great interest in the wooden styles of the 21st centuries."
    "Great architectural designs too."
    L "\"I prefer the look of more modern rooms, but I do agree the vintage atmosphere is very nice.\""
    hide lyra normal with moveoutleft
    "My room holographically mirrored the image of an older-style Japanese-themed room due to one of the systems implemented in this house by the previous owner."
    "Based on my interests, I could remodel my room to be anything I liked, and it would shape itself into anything I could imagine."
    show lyra normal with dissolve
    L "\"Don’t forget to eat your breakfast! I’m going to go now.\""
    show lyra normal at right with move
    hide lyra normal with dissolve
    "I nodded, and we waved goodbye to each other. Lyra’s face smiled brightly as she departed."
    scene diningroom with fade
    "I came out to the living room, and ate the breakfast Lyra cooked for me."
    "Blueberry pancakes with sunny side up eggs and bacon. Classic."
    "I was currently living in a house near Garden Land Trailhead, one of the quietest parts of the city with its famous hiking trails."
    "It was a one-story house, big enough for 2 residents, but maybe a little too big for one. The best feature of this house was its ability to stay warm throughout the year. Never too cold. Never too hot."
    "Its walls were made with a mixture of cement and pserium, a magical powder developed by the Governmental Laboratory used to maintain stability and give it ideal conditions throughout the season."
    "We were really living it up with technology these days."
    unknown "\"Master, I have finished cleaning duties.\""
    P "\"Hm?\""
    show cleanbot normal with moveinright
    "As I looked to my right to where the voice came from, a tall human-like android stood in front of me dressed in a suit."
    "It was the cleaning bot that Lyra gave me a few years back."
    show cleanbot talk
    cleanBot "\"Do you have any more requests, Master?\""
    P "\"No, you can rest.\""
    cleanBot "\"Yes, Master.\""
    hide cleanbot talk with dissolve
    "The android made its way to the wall next to my room and turned itself into a small, circular object tucked neatly away into a shelf."
    P "\"I guess it's time to go to work.\""
    "I put away my plate into the automatic cleaning sink, and headed back to my room."
    stop music fadeout 1.0
    scene bedroomchangenightlight with Fade(0.5,2.0,0.5)
    play music "audio/night_theme.mp3"
    "It was now 8:30 in the evening as I called off my job's meeting and shut down my computer."
    "Thinking about nothing, I laid down on my bed."
    P "\"That meeting was longer than I thought...Looks like it will be a busy day tomorrow working on that new website for my client.\""
    "Hmm..."
    P "\"Maybe a little jog wouldn't hurt to keep my blood flowing.\""
    "I stood up to get a hoodie in my closet before heading outside"
    play sound "audio/doorOpened.mp3"
    scene bedroomchangenight
    scene nightsky with Fade(0.5,2.0,0.5)
    "The night sky was still, and the light from the moon shone down the trail as I jogged."
    "I kept my breath steady as the cold wind blew against my face with a freezing touch. The heat generated through my energy exertion slowly warmed up my face."
    P "\"Wait a minute.\""
    "In the corner of my eye, I saw a faint shimmer of light deep within the hills."
    P "\"What is that...?\""
    play sound "audio/hover_over.mp3" volume 0.8
    "A loud engine started hovering behind me."
    P "\"What's that soun-\""
    menu:
        "Turn around":
            play sound "audio/hover_over.mp3" volume 0.8
            "As I turned to look back, a truck flew over me at high velocity."
            "Its generated wind blew at me with full force."
            jump Ch1_continue
        "Keep running":
            "...Maybe it's nothing."
            play sound "audio/hover_over.mp3" volume 0.8
            "A truck flew over me at high velocity."
            "Its generated wind blew at me with full force."
            jump Ch1_continue
        "Stop":
            "I halted my jog and turned to where the sound came from."
            play sound "audio/hover_over.mp3" volume 0.8
            "To my surprise, a huge truck flew over me with great velocity."
            "Its generated wind blew at me with full force."
            "Taken by surprise, I stepped back."
            jump Ch1_continue

label Ch1_continue:
    scene nightsky_truckhover with dissolve
    P "\"Woahh, look at the size of that thing! It’s the newest truck model! That actually looks so coo-\""
    stop music fadeout 1.0
    "My foot slid on a pebble on the edge of the trail."
    P "\"W-woa..h..!!\""
    with vpunch
    play sound "audio/fallDown.mp3"
    scene black
    "I tipped over the side of the trail, my body swirling in motion as I rolled down the slope of the trail down to the bottom of the hill."
    play sound "audio/fallDown.mp3"
    "Everything was spinning."
    play sound "audio/fallDown.mp3"
    with vpunch
    P "\"Argh!\""
    play music "audio/night_ambience.mp3" fadein 1.0 volume 0.8
    scene forest with fade
    "My body jolted in pain as I slammed myself into a tree."
    "Haven't felt something like this since I hit my funny bone on the edge of a sofa."
    "Wasn't fun."
    P "\"Did I really tripped on a rock while sidetracking...\""
    "Well that was an event."
    scene forest_light_flicker with dissolve
    scene forest with dissolve
    P "\"What...is that?\""
    play sound "audio/leave_rustle.mp3" volume 0.8
    "I slowly stood up, with the pain lingering, as I strived to take a closer look at the flickering light."
    scene shack_bg with fade
    P "\"Is that a shack?\""
    "I moved forward towards the light, and what stood upon me was an old, rusty shack."
    P "\"Looks abandoned...Is anyone there?\""
    "...No response."
    P "\"Hm...\""
    menu:
        "Peek between the cracks of the door.":
            "I peeked between the cracks of the door and saw some sort of flickering light emitting from an object."
            jump Ch1_enterShack
        "Knock on the door.":
            play sound "audio/door_knock.mp3"
            "I knocked on the door several times."
            P "\"Hm...still no response. I guess it really is abandoned.\""
            jump Ch1_enterShack
        "Open door.":
            jump Ch1_enterShack

label Ch1_enterShack:
    play sound "audio/doorOpened.mp3"
    "I opened the door and walked towards the flickering object."
    P "\"A mirror...?\""
    "I looked inside the mirror and the light grew brighter."
    "Then a clear image came to view."




    #Chapter 2
label chapter2_start:
    P "\"What is this thing?\""

    "Visually, it seemed like an ordinary handheld mirror, but there was something special about it."

    "As I peered through the mirror, it seemed like there was something beyond the reflection."

    P "\"It almost seems like… a door to another place.\""

    "I placed my hand over the mirror, and I was pulled through."

    stop music fadeout 1.0
    with flash
    with flash
    scene shack_bg with flash

    "..."

    "What just happened?"

    "Moonlight crept through the crevices of the shack."

    "......"
    play music "audio/BTR-Ominous-01.mp3" fadein 1.0

    "What just happened…?"

    "I stepped outside and took a look around."

    "The blue mirror... Wait! The mirror!"

    "Did something happen because I touched the mirror?"

    "Curious, I walked back to my house."
    stop music fadeout 1.0
    scene nightsky with fade

    play music "audio/night_theme.mp3"
    scene diningroom with dissolve
    play sound "audio/doorOpened.mp3"
    "As I stepped in front of my house, I heard movement from within."

    P "\"Who’s in my house? I don't remember inviting anyone over...\""
    "Oh it must be Lyra! She’s probably over to check up on me. Gotta tell her I was just out on a short jog."
    "A strange, but familiar figure rushed out as I entered the house."
    show calliope shocked with vpunch
    L "\"[Protagonist]...! Is that really you?\""
    "Lyra...?"
    play music "audio/BTR-Ominous-01.mp3" fadein 1.0
    show calliope concerned
    L "\"You’ve been gone for so long! Where have you been?\""
    P "\"Just...a little jog...\""
    "Come to think of it, my whole house looks a bit...old? That can’t be right..."
    L "\"Just a jog? You’ve been gone for days! I’m so glad you’re alright.\""
    L "\"What happened to you?\""

menu:
    "I was just out on a jog.":
        L '"A jog? That\'s it? A jog couldn\'t have made you disappear for days."'
        P '"..."'
        P '"I was just out on a jog..."'
        show calliope normal
        L "\"[Protagonist]? If you don't want to tell me that's fine. I'm just glad you're okay.\""
        P '"Everything does feel a bit off though..."'
        jump ch2_jogchoice_end

    "I went through this mirror.":
        P '"While I was out on my jog, I slipped and fell down this hill."'
        P '"I found this shack, and there was a glowing mirror inside."'
        P '"When I touched it, there were these flashes of blinding light."'
        P '"And now I\'m here."'
        P '"Everything feels a bit off... Even you..."'
        jump ch2_jogchoice_end

label ch2_jogchoice_end:
    P '"Are you really Lyra?"'
    show calliope concerned
    L '"Lyra? Who\'s Lyra?"'
    P '"You\'re not Lyra?"'
    L '"Do you not even remember my name, [Protagonist]? I\'m Calliope."'
    show calliope angry3
    G '"Ever since your sorry butt went missing, I\'ve been putting the group\'s survival on my back."'
    G '"It\'s my job to take care of your guys and when you went missing, I felt like I\'d failed."'
    show calliope angry1
    G '"We had that whole plan figured out and ready to go, and then you disappeared!"'
    P '"What plan?"'
    show calliope angry3
    G '"The plan was for you, Ben, and me to go to the Frolic Room Bar to restock on supplies."'
    P '"Supplies?"'
    show calliope normal
    G '"Here, I\'m going to call Ben now that you\'re back, so we can continue the plan."'
    scene black with fade
    stop music fadeout 2.0

    hide calliope normal with dissolve
    scene nightsky with fade
    play music "audio/night_theme.mp3"

    P "\"I don't understand... Why are we going to this bar again? Supplies for who?\""
    show calliope concerned at right with dissolve
    G "\"Did you hit your head while you were out? We're sending Ben in there to grab some supplies for the group.\""

    P "\"The group?\""
    show calliope angry1 at right
    G "\"Okay [Protagonist], I'm glad you're okay and all, but you seriously need to get it together before we get to the bar!\""
    show ben normal at left with dissolve
    B "\"Don't worry Calliope, I'll explain everything to our forgetful friend here. Things must've happened when [Protagonist] was gone.\""
    show ben normal talk at left with dissolve
    show calliope at right

    "I'm guessing this Ben guy is a close friend of ours. He seems nice, but..."

    B "\"Calliope, the leader of our little band of misfits, sent you to an outpost to grab some supplies a few days back. You didn't come back, so we sent some of the group to go looking for you. We got worried when we went a few days without hearing from you, and we'd assumed the worst.\""

    "Do these people know who I am? I've never seen them in my life, but they're treating me so kindly..."

    "Wait... \"assumed the worst\"?"
    show ben smile at left
    B "\"Anyway, now that you're back, we can go through with our plan to pay the bar a visit and uhh... borrow a few things. But regardless, we're glad you're okay.\""
    show ben normal at left
    show calliope normal at right with vpunch

    "This \"Calliope\"... she looks exactly like Lyra... but instead of being my personal caretaker... she seems to be the caretaker for this whole \"group\" thing that was mentioned."

    G "\"Anyway, once we get to the bar, you and I will stand by while Ben snags some stuff we could use.\""

    P "\"Why are you taking things from someone else? Don't you have everything you need at your residences?\""
    show calliope concerned at right
    G "\"I really wish that were the case, buddy. But unfortunately, the people around here don't exactly like to give out treats to those in need. That's why I do my best to look after all of you.\""

    jump chapter2_bar

label chapter2_bar:

    scene frolic room front door
    with dissolve

    "Calliope, Ben, and I made our way to a bar known as the \"Frolic Room\"."

    show ben serious talk

    B "\"Alright, I’m going to head around the back. You guys hang around, don’t look suspicious, and if there’s any trouble I’ll come running.\""

    G "\"You don’t get into any trouble either, okay?\""
    show ben smile
    B "\"Please, there's not a chance.\""
    hide ben smile with dissolve
    "As Ben turned the corner, he pulled his hood up and gave us a quick thumbs up before becoming buried by shadows."

    P "\"So, what exactly is a bar? What do people do here?\""
    show calliope concerned with dissolve
    G "\"Oh you know… rich folk with nothing to do sitting around, getting drunk, and throwing fists at each other.\""

    P "\"Geting drunk?\""

    "Calliope turned to me with an amused smile."
    show calliope normal
    G "\"You really don’t know anything, do you?\""

    G "\"Come on. You can just see for yourself.\""
    hide calliope normal with dissolve

    scene frolic room inside
    with dissolve

    "When we entered the bar, most of the seats were already taken. Calliope and I managed to find space tucked in the dark corner of the room."

    "It was very noisy inside, more commotion than I had ever seen or heard in my life."

    "People were drinking from large mugs, clanking them on the table, laughing and shouting about a game or something."
    show calliope serious with dissolve
    G "\"See those guys over there?\""

    "She nodded towards a group of people near the front of the bar. Their backs were turned to us. They wore long cloaks with dark hoods. They were tossing coins around the table back and forth."

    show calliope serious at right with move
    show lizardmen bandits at left with dissolve

    "Despite being a very loud bunch, their words were hard to make out. They seemed to speak with some sort of lisp."

    "Before I could ask Calliope what was so interesting about them, one turned around to lean against the table."
    show lizardmen bandits
    "His skin was covered in green scales, and I finally noticed the long, green tail peeking out from underneath his cloak."

    P "\"What in the world… What happened to him?\""

    G "\"That’s one of the lizardmen bandits. He hangs around the bar pretty often. Just a normal guy like you or me, but obviously covered in scales not skin. And there’s something else.\""

    G "\"Lizardmen, and any half-beast person, can use magic.\""

    P "\"Whaa.. Magic?\""

    G "\"Yup, real bonafide magic. It can be real dangerous too, so you have to be careful.\""

    "Part of me wanted to see this magic right away, and another part of me knew to heed Calliope’s warning."
    hide calliope serious with dissolve
    hide lizardmen bandits

    with fade

    "The second half of what seems to be a gladiator fight has started on the television. One of the team, the L.A, chose to replace one of their fighters with a big, heavy-weapon wielder so they can give enough pressure to Hollywood, the opposing team. In the meantime, Hollywood didn’t make any changes. It seemed like their faction leader was pretty satisfied with the current fighter."

    "After 45 minutes, the score is 1-1. Almost everyone in the bar stood up and stared at the screen. Some of the Hollywood fans were so nervous that they turned their faces away and started praying."

    "\"Headshot! Hollywood has scored! Hollywood fighter, Alison, gave a powerful swing and sent the L.A fighter’s head flying!\""

    "Hollywood fans started cheering. Although they only occupied a quarter of the bar, the noise they created roared throughout the bar room"

    show terry with dissolve

    LV "\"YES!!!!! We are the champion folks! I've waited for so many years!\""

    "On the other hand, all L.A fans were stunned. Some of them use their hands to cover their face. They still couldn't believe this happened."

    show terry at right with move
    show lizardmen bandits at left with dissolve
    with hpunch

    LB "\"This is not fair! The L.A can't lose! The L.A fighter must’ve been poisoned! They let Hollywood win so that they can put millions of dollars into their pocket! They do this every year! The Champions League is all fake...\""

    LV "\"Yo calm down guys. Just admit the loss.\""

    stop music fadeout 1.0

    LB "\"Shut up, you British pig! You are saying this because Hollywood won. Just get out of this place! We are not happy to see you! Ugly Red fans!\""

    LV "\"You got a problem? How about you get off this bar, loser?\""

    play music "audio/BTR-Ominous-01.mp3" fadein 1.0 volume 0.8

    LB "\"How dare you! You want a fight?\""

    hide terry with dissolve
    hide lizardmen bandits with dissolve

    show calliope serious with dissolve
    G "\"Damn. This is not good. We'd better leave.\""

    "Suddenly, a loud voice spoke up over the rest of the room."

    hide calliope serious with dissolve
    show lizardmen bandits with vpunch

    LB "\"Hey! Watcha got there? A little present for me?\""

    "One of the lizardmen bandits were bellowing at someone, but we couldn’t see them from our corner of the room."

    LB "Come on, little guy, you know better than to mess around with us."

    G "\"Oh no… is that…\""

    "Two of the lizardmen walked over to the ‘little guy’ and shoved him towards the middle of the bar."

    "As he stumbled into the middle of the room, his red hair came into view."

    show lizardmen bandits at left with move

    show ben serious at right with dissolve

    "It was Ben, caught red-handed, still clutching a bag presumably full of food and drinks."

    LB "\"Alright little guy, hand over the bag and we’ll try not to kill you.\""

    hide lizardmen bandits with dissolve
    hide ben serious with dissolve

    show calliope angry3 with dissolve
    with hpunch

    G "\"Crap… we need to get him out and fast. Stay here. Lay low and don’t do anything stupid.\""

    P "\"Let me help!\""

    G "\"No no no. Bar fights are not the normal fights you see on TVs. This is the part you don't want to experience. Just STAY THERE!\""

    hide calliope angry3 with dissolve

    "More and more drunk people heard that there was a fight in the Frolic Room and tried to squeeze in to see what happened."

    "Calliope managed to pick up Ben and ran out away from Terry and the two lizardmen"
    show ben serious talk at left with dissolve
    show calliope serious at right with dissolve
    B "\"We're too late. There is no way out now. All of the exits are blocked by crowds. We'd better start moving to one of the exits and see if we can get through them.\""

    G "\"They’re going to chase us. We need to get a move o-\""
    scene frolic room inside with vpunch
    "Before Calliope finished her words, a giant fireball passed by and burnt the TV on the wall."

    P "\"Woah. What is that?\""
    show ben serious talk with dissolve
    B "\"Looks like the fire ball is from the Lizardmen.\""

    hide ben serious talk with dissolve

    "Let me get closer and see…"
    show frolic room inside with hpunch
    "While I got closer to the fighting stage, an ice arrow came out of nowhere and pierced the wall."
    show calliope shocked at right with vpunch
    G "\"Yo [Protagonist]! Stop moving backwards!\""
    hide calliope shocked with dissolve

    "I didn’t hear Calliope because the crowd was getting crazy. Everyone was fighting each other."

    "As I was moving, I found out that the ice arrow is from a semi-transparent frog. "

    P "Wow, I have never seen animals like this."
    show lizardmen bandits at left with dissolve
    show terry at right with dissolve
    show lizardmen bandits at left with vpunch
    LB "\"I like your minion. It looks strong. But I am going to kill you and it will be mine! Hahahahahaha…\""

    LV "\"Don’t ever think about it, loser.\""
    show terry at right with hpunch
    show lizardmen bandits at left with hpunch

    with flash
    with flash
    hide terry
    hide lizardmen bandits
    "Suddenly, a flash appeared in the middle of the room and I couldn’t see anything."

    "After I opened my eyes, the fight became more chaotic."

    "Lizardmen Bandits and Terry were fighting in the middle of the bar while their minions were also fighting using their magic power. They use whatever is near them to attack and defend."

    "The bar is completely in chaos. Chairs, knives, and bottles are flying around the bar."

    "Suddenly, someone caught my arm and tried to drag me out of the frontline."

    show ben serious with move

    P "\"It’s you, Ben! I’ve never seen a fight like this! They are so cool!\""

    B "\"Yes they are. But we need to leave. It is unsafe here…\""

    stop music fadeout 1.0

    "While Ben was trying to convince me, a stone-made arrow pierced through Ben’s body."
    with hpunch

    #Chapter 2 Ends

#Chapter 3 Begins
    play music audio.ominous02 fadein 5.0 volume 0.8

    hide ben

    "I couldn’t stop staring at Ben. He was a complete mess, but it went beyond his usual dirt-filled attire."

    "He had collapsed on the floor. His tanned clothes were now stained red. His tousled hair was drenched in sweat. The arrow still pierced through his body."

    "His expression was one I had never seen before. His eyes were barely open, not seeming to be looking at anything at all. His mouth was agape, and his breathing was raspy and uneven."

    "What was wrong with him?"

# choice 1
menu:
    "Continue to Stare":
        #label ch3_con_to_stare:
        show calliope angry3 at right with vpunch
        G "What the hell are you standing around for?!"

        P "Huh? I just -"

        jump ch3_endchoice1
        #jump ch3_con_to_stare

    "Grab the Arrow":
        # label ch3_arrow:
        show calliope angry3 at right with vpunch
        G "Stop that! Let me handle it."

        P "Oh, sorry, I just-"

        jump ch3_endchoice1
        #jump ch3_arrow

    "Talk to Ben":
        # label ch3_talk_to_ben:
        P "Ben? Come on, get up. You're... making me uncomfortable."

        "There was no response. Ben didn't even look at me."

        show calliope angry3 at right with vpunch
        G "[Protagonist], what are you doing?!"

        P "Huh? I was just -"
        #jump ch3_talk_to_ben


label ch3_endchoice1:
    hide calliope angry3 at right
    show calliope angry1 at right
    G "Nevermind that. Help me get him out of here."

    "Calliope grabbed Ben by the shoulders, and I grabbed him by the legs. He was much lighter than I expected."

    scene black with fade

    "We took Ben and left the bar quickly and quietly. We looked for a quiet, open space, and finally ducked behind an alley a couple of buildings away."

    scene alley_night with fade

    "We laid Ben down on the pavement. I thought about how uncomfortable the cold, hard ground must be, but Ben didn’t seem to notice."

    "Calliope swung her bag out from around her shoulders and placed it on the floor. From the bag she took out a long, ragged piece of cloth."

    "I watched as she carefully removed the arrow from Ben’s body, and then wrapped the cloth around Ben’s stomach. Then, she took out a plastic canteen and held it to his lips."

    show calliope concerned at left with dissolve

    G "Come on Ben, you’ll be alright. Everything will be okay. Stay with me now."

    "Calliope’s voice didn’t sound right. Its usual confidence and strength was gone, replaced by something that seemed to be breaking apart."

    hide calliope concerned at left with dissolve

    "Ben wasn’t acting right either. No responses. No eye contact. He wasn’t even trying to take a sip of water."

# choice 2
menu:
    "Continue to Stare":
        #label ch3_con_to_stare_2:
        "I continued to stare at Ben, laying on the ground. His only movement came from his barely noticeable breaths. The look on Calliope’s face was one I had never seen on her before."

        "Her expression was panicked, her eyes were watering, and she kept mumbling, begging Ben to stay here."

        "I didn’t understand. Where was Ben going? How could someone be going somewhere when they didn’t move at all. Nothing was making sense."

        "I suddenly felt very out of place. The reality of being in a completely different world, with completely different rules and ideas began to hit me. What was happening? What was I doing here?"

        "Maybe I need to go. Maybe I wasn’t ever meant to be here."

        "Before I could really consider leaving, Calliope began to cry out."

        jump ch3_endchoice2
        #jump ch3_con_to_stare_2

    "Talk to Calliope":
        # label ch3_talk_to_cal_2:
        P "Calliope? What’s going on? I don’t understand."

        show calliope angry2 at left with dissolve
        "Calliope turned and glared at me."

        hide calliope angry2 at left
        show calliope angry3 at left
        G "What’s there not to understand?! Ben is.. He’s…"

        hide calliope angry2 at left
        show calliope concerned at left
        "She stopped talking to me, turning back to Ben."

        G "Please Ben, please just stay a little longer and I can get help."

        hide calliope concerned at left
        jump ch3_endchoice2
        #jump ch3_talk_to_cal_2

    "Talk to Ben":
        #label ch3_talk_to_ben_2:
        P "Ben? What’s wrong? Can you get up and talk to us?"

        "Again, Ben was silent. No sign that he even heard me at all."

        "Before I could say another word, Calliope began to cry out."
        #jump ch3_talk_to_ben_2

label ch3_endchoice2:
    show calliope shocked at left
    G "Ben? Ben!? No no no... Please we need you."

    "Calliope was sobbing now. Tears were running down her face. I looked at Ben again. His raspy breaths had stopped, replaced with nothing but silence. His eyes were glassy, still staring at nothing."

    "Calliope stopped crying out and took a deep breath. She wiped the tears from her face. Then, she took her hand and gently closed Ben’s eyes."

    hide calliope shocked at left
    show calliope upset at left
    G "I’m sorry..."

    P "Calliope? What’s going on?"

    hide calliope upset at left
    show calliope angry2 at left
    "Calliope turned to me suddenly. Immediately, the pain appeared in her face again, mixed in with a fierce anger."

    hide calliope angry2 at left
    show calliope angry3 at left
    G "What is wrong with you?!"

    P "Huh? What do you-"

    G "Just GO AWAY! You need to leave."

    "I didn’t have words to respond. Why was she being like this?"

    G "If it weren’t for you, Ben would still be here!"

# Choice 3
menu:
    '"Ben is still here."':
        #label ch3_ben_is_here_3:
        with hpunch
        G "What the hell is wrong with you!? He’s DEAD. Can’t you see that?! He’s DEAD and it’s all YOUR FAULT."

        G "We’ve been risking our lives bringing you along, because you’re too stupid to understand basic common sense. And now enough is enough. You need to leave before you kill someone else too."

        G "Ben would still be here if it weren’t for you — if it weren’t for me bringing you along."

        G "You don’t belong here. Go back to wherever you came from and don’t come back. You’ve done enough here."
        hide calliope angry3 at left with dissolve

        "Calliope stopped looking at me. I thought about responding, but I had no words and I doubted anything I said would make a difference."

        jump ch3_endchoice3
        #jump ch3_ben_is_here_3

    '"Fine, I\'ll leave."':
        #label ch3_fine_ill_leave_3:
        show calliope angry1 at left
        G "Finally. The first reasonable thing you’ve ever said. Now don’t say another word. Just go."
        hide calliope angry1 at left with dissolve
        #jump ch3_fine_ill_leave_3


label ch3_endchoice3:
    "There was only one thing to do. It seemed my journey in this world was done now. There was no point in staying around."

    scene black with fade
    stop music fadeout 2.0

    "I returned through the mirror, and it was a quiet, lonely walk back home."

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
    play music "audio/daytimetheme.mp3" loop volume 0.7

    "I decided to take the mirror to the appeals office located a short walk away from where I lived. I knew how to get there thanks to lessons from when I was younger."

    "Lyra said that if anything went wrong, the appeals office was the place to go. All I would have to do was walk out of my residence, turn left, and keep walking until I got there."

    "I'd never been there before because, well... nothing had ever gone wrong."

    "Once I had been walking for a few minutes, I saw a very small building in front of me, appearing almost out of nowhere."

    "I immediately knew I was in the right place thanks to two things:"

    "a sign that read \"Appeals\" in bold red lettering displayed on the front of the office, and the fact that this building was the only one that looked nothing like the residences scattered throughout the rest of the area."

    scene appeals with fade
    hide daysky
    play sound "audio/doorOpened.mp3"

    "I walked through the front door and immediately noticed the lack of furnishings inside. In my residence, I have a place to sit, stand, or sleep when I wish."

    "In this appeals office, there wasn't a single chair to be seen, nor a sign directing me to the appropriate place to report the mirror."

    stop music fadeout 3.0

    "It was as if this place was designed never to be used, only seen from the outside."

    "I walked a few steps into a narrow hallway filled with nothing but gray walls until I noticed a person sitting behind a desk further down the hall."

    "Their eyes were completely blank, focused on nothing in particular. When I walked up to them, they jumped in their seat, urging me to take a step back myself. My heart started beating just a bit faster, reminding me of my time with the guide."

    P "I'd like to ask you about this strange object I found. I've never been here before, and I'm not sure exactly how this process works, but I've brought it here in the hopes that you can help me with it... whatever it is."

    play music ominous01 loop volume 0.8

    "I pulled the mirror from my pocket and placed it on the desk, and the person before me almost immediately started breathing heavily. Their eyes widened, their expression changed, and they couldn't say a word for a moment or two."

    "At this point, for a brief moment, I saw a familiar look in their eyes. They looked a bit like Ben did when he became hurt."

    "After some hesitation, they reached over and pressed a small red button. I heard a click and a high-pitched beep, and then waited for a moment. The person behind the desk still hadn't said anything, but I knew that something wasn't quite right."

    with flash
    with flash

    "Suddenly, a flash of light appeared and dust was swiftly scattered from the surrounding area. After the light was gone, I saw Lyra standing before me."

    show lyra serious at right with moveinright

    "She looked at the person behind the desk, looking confused."

    L "What's the problem, hmm?"

    "Still refusing to speak, they simply pointed at the mirror I had placed on the desk with that same intense look in their eyes."

    hide lyra serious
    show lyra surprised at right

    "Lyra looked at the mirror, and immediately became still. There was a long pause before she did anything else, as if the mirror had some kind of hold on her."

    "After a moment, she looked directly at me, and started speaking in her familiarly polite voice."

    show lyra surprised at center with move

    L "Where did you get that mirror?"

    hide lyra surprised
    show lyra angry3

    "I realized how little I'd been posed with questions throughout my life, but also how little I'd asked them. I'd never needed to find an answer. I found myself unable to speak, as if the same force controlling the employee had suddenly been transferred to me."

    L "Can you hear me? Hello? Where did this come from?"

    hide lyra angry3

menu:

    "Say Nothing":
        jump chapter4_saynothing

    "Lie":
        jump chapter4_lie

label chapter4_saynothing:

    "I said nothing."

    show lyra angry2 with dissolve

    "She picked up the mirror and took a few steps toward me, holding the object in front of my face."

    L "At least tell me this... Have you... used this mirror? Did anything happen while it was in your possession?"

    "For the first time in my life, I saw the plain, simple smile that Lyra always wore leave her face... replaced by something I could just barely recognize."

    hide lyra angry2
    show lyra angry3 with vpunch

    L "Answer me!"

    "She reminded me of Calliope. Looking at me with a narrow gaze, asking me something I couldn't quite bring myself to answer, disturbed by my lack of cooperation, and refusing to put up with it for much longer."

    "All I could do was shake my head. The feeling she gave me wasn't pleasant, and I wanted it to be gone quickly."

    "She had an expression on her face that spelled out her displeasure in waiting for me, but I knew that if I told Lyra my story, I likely would only make the feeling worse."

    "After finally getting an answer, she quickly sped up the conversation."

    hide lyra angry3

    jump chapter4_end

label chapter4_lie:

    show lyra angry2 with dissolve

    P "I... umm... just found it a few minutes ago...I brought it here as soon as I did."

    L "Well where did you find it?"

    P "It was... just laying on the street. I didn't think much of it, but I brought it here just to be safe."

    "I don't know what made me want to lie. But I somehow knew things would've gone bad quickly had I told Lyra everything I had seen through the mirror."

    "I could feel my hand shaking, which startled me. Nothing had ever had quite the same effect on me."

    "I couldn't tell what Lyra would do next, but I knew I just wanted to go home as soon as possible."

    "I wanted to be away from this place, away from this sinking feeling in the pit of my stomach, away from any consequences Lyra would have for me if she found out I had lied to her."

    "After what seemed like an eternity, she finally spoke, and I couldn't describe with words how relieved I was once my hands stopped trembling."

    hide lyra angry2

    jump chapter4_end

label chapter4_end:

    stop music fadeout 2.0

    show lyra angry1

    L "Okay! Well, I'm glad you found my mirror! If you have no further appeals to make, then I'll just take it back with me and send you on your way!"

    "Without a moment's notice, Lyra waved her hand in a fluid motion towards me, and now I was the one engulfed in a flash of light."

    hide lyra angry1 with dissolve
    with flash
    scene bedroom with dissolve
    with flash
    hide appeals

    "After it disappeared, I found myself back in my room once again."

    "I was tempted to resume my daily activities now that the mirror was in its proper place, but I couldn't help but wonder about what would happen next."

    "I'd used the mirror to see people and places I never had before, and wondered if Lyra had been using the mirror in that way. If so, for how long? And more importantly, why?"

    "I sat at my desk and let myself take in all that had happened recently. For the first time, I had serious questions on my mind."

    "For the first time, I wasn't sure how everything would turn out. And for the first time, I felt this strange desire take over my body."

    "Before all of this, I had gone through every day knowing how it would turn out, and never wondered about any other possibilities."

    "But sitting in my room, thinking about Ben, Calliope, and Lyra's expressions throughout these events, I knew I wanted more."

    "I had felt things I liked, and many things I didn't like. But knowing that there could be more, that Calliope was still out there, along with all of their associates and enemies, it caused something in me to change."

    "I needed to know more. More about the things they showed me... more about the way it made me feel..."

    "More about myself."

    #Chapter 4 END.



    #Chapter 5
label chapter5_start:
    scene black with fade
    "... ... ..."
    "The sun had set a while ago but that didn’t deter me."
    play music "audio/night_theme.mp3" loop volume 0.85
    scene firstscene with fade



    "Walking with no clear direction or goal, and with no leads to follow up on, I eventually found myself walking a familiar dirt path."
    "Looking up, I saw the rusty shack from what seemed to be a lifetime ago."
    scene shack_bg with dissolve
    "With a hint of melancholy nostalgia, I opened the door and went inside."
    "Something was immediately off however."
    "What was once a dimly lit shack was now lit with a faint light blue glow."
    scene glowingblue with dissolve
    "There was no primary source."
    "Instead, it appeared to be a trail of some sort of light, snaking its way out of the shack, and pulsing occasionally."

    scene shack_bg with dissolve
    "There was no way I had missed this before. Perhaps it had always been here, and only after my experience with the mirror had I been attuned to it."
    "Magical residue perhaps?"
    scene black with fade
    "I felt a small flicker of hope. This was the lead I had been searching for!"
    scene trail with fade
    "Without hesitation, I followed the trail out of the shack, and into the night."
    scene black
    "Unbeknownst to me, a dark figure slipped out from the treeline."
    show resize at right with moveinright
    unknown "(Radio Static) Check in Dispatch ... ... Target … … walking … … will pursue … ..."
    hide resize with moveoutright
    "..."
    "... ..."
    "... ... ..."
    "It must have been at least midnight. With no phone, and fatigue beginning to set in, I had lost track of how long I had been walking. I could barely see 10 feet ahead of me."
    "Without warning, a giant rock face loomed out of the dark at me."
    scene rockwall with fade
    "The magic trail went straight into the rock and disappeared."
    "Now what was I supposed to do?"
default menuset = set()

label begin:
    menu:
        set menuset
        "Look for an entrance":
            "I walked around the wall, searching for a hidden entrance, or something I had missed. But nothing stood out to me."
            "I felt this wasn't the right way, so I headed back to my original spot."
            jump begin

        "Walk straight into the wall":
            "If the light went straight into the wall, then so would I."
            "With a little nervous hesitation, I walked full speed into the wall."
            "I braced myself for a painful impact..."
            "...and to my surprise, I walked cleanly through the rock. It was as if the rock wasn't there at all."
            jump endchoice
label endchoice:
    scene firstcave with fade
    play music ominous01 loop volume 0.3 fadeout 1.0 fadein 1.0
    "I followed the only path available, walking and climbing constantly downwards."
    "Occasionally, I would come to branching paths. Without my guiding light, I would have been hopelessly lost in the labyrinth of subterranean corridors."
    "What is this place?"
    "The uncomfortable feeling I had since entering underground was growing, but now I was sure it wasn’t just in my head."
    "There was something intangible in the air."
    "A buzz? Almost like electricity crackling through the air."
    "I could feel the hairs rising on my neck and arms. Something was down here, and it exuded power."

    scene secondcave with dissolve
    "The corridor opened up into a larger clearing. For the first time, I could hear a deep humming noise, coming from even deeper."
    "The air felt even more restrictive now, like it was slightly pushing me away from whatever was down here."
    scene black with dissolve
    show doors2 with fade

    "Before me lay a pair of colossal doors, stretching from the ground into the darkness of the ceiling."
    "The sheer size made me dizzy looking up at it."

    P "How am I supposed to move something like this?"
menu:
    "Test Your Strength":
        "Bracing against the doors, I pushed with everything I had."
        "Nothing."
        "The doors pulsed a magical neon red, as if it disapproved."
        "It was like trying to move a mountain."
        "With no other option, I tried again. And again. And again."
        "I sank to the ground, sweating and breathing hard, defeated."
        "Then, the faintest sound of sliding stone. I looked up."
        "The doors had slightly opened, not very much at all, but almost as if in respect to the effort I had given."
        "One more time, I stood up and placed my hands against the stone."
        "It was still incredibly heavy, but not as daunting as before and after considerable effort..."
        scene doors with fade
        "...the doors opened enough to move through."
        jump enddoorchoice

    "Ask Politely For Them To Open":
        "I walked up to the unfathomably large doors."
        "No way was I able to get through this with physical effort."
        "There must be a trick to it."
        P "Hello? Could you open up please?"
        "The doors pulsed a magical blue, as if acknowledging my strategy of not trying to muscle it open."
        scene doors with fade
        "The doors slowly and smoothly opened."
        jump enddoorchoice
label enddoorchoice:
    "The path opened up to a large cavern."
    scene finalcave with dissolve
    stop music fadeout 1.0

    "The deep humming was very audible at this point. It reminded me of the now-archaic nuclear engines commonly used long ago."
    play music "audio/A Better Place [wav].wav" fadein 3.0 volume 0.5
    "Directly across from me, was another mirror."

    "Almost exact in design to the one I had confiscated from me, but scaled a thousand times larger."

    "My clothes gently swayed as if in a breeze, but there was no air current this deep down."
    "The magical blue hue of the mirror lit up the cave with a beautiful glow."

    "This was it. This was what the magic trail had been leading to."
    stop music fadeout 2.0
    #Chapter 5 END

#Chapter 6
label ch6_start:
    "Before I knew it, I was running straight for the mirror, my legs practically moving on their own."
    play sound "audio/cave_running.mp3" loop
    "I knew what I wanted, but for the first time, I felt a real sense of excitement."
    scene finalcave_closer with fade
    "The buzz from the mirror began to take over my thoughts as I got closer and closer, even drowning out the sound of my feet hitting the hard floor."
    scene finalcave_closest with fade
    show lyra angry3 at right with hpunch
    L '"STOP!!!"'
    hide lyra angry3 with moveoutright

    "I could faintly hear someone calling out to me, but I didn’t care."
    "I was already close enough to the mirror where I could look in and see the scenery of the other world."

    stop sound

    "But every muscle in my body suddenly froze, and the sound of my last footstep echoed throughout the cave."

    show lyra serious at right with dissolve
    play music "audio/BTR-Ominous-01.mp3" loop volume 0.5
    L "\"[Protagonist], honey, where do you think you're going? Did you not hear me?\""

    "I could feel my neck loosen up. I turned my head around to see Lyra walking towards me with her arm outstretched."

    L "\"Tell me what you know. It's okay if you hid something from me earlier.\""
    L "\"I get that things you don't understand can be pretty overwhelming.\""

    "She didn't have her usual smile, and her voice had a coldness to it despite addressing me in an endearing way."
    "There's no way around it now. I have to come clean...but it should be fine."
    "Lyra did take care of me for my whole life."

    P "\"I’m sorry Lyra. I wasn’t sure how you’d react; I didn’t even understand what had happened to me, so I hid the truth.\""
    P "\"When I found the mirror, I ended up in a strange place that looked entirely different from here.\""
    P "\"I was confused, so I immediately grabbed the mirror and appeared right back in the same place as if nothing had happened.\""
    P "\"I only found this place because I saw this weird blue light and followed it here.\""

    "Lyra seemed to accept my story, and the serious look on her face faded away."
    hide lyra serious at right
    show lyra normal at right
    stop music fadeout 3.0
    "However, I got the feeling that I should still keep quiet about what I saw and the people I met."

    L "\"Well, I can't blame you for being a little curious.\""
    L "\"This isn't exactly something you see every day.\""
    L "\"You need to be more careful though...especially when I'm not around.\""
    L "\"There are a lot of dangerous people and things beyond that mirror that will hurt you without a second thought.\""
    L "\"Understand?\""

    "I nodded as much as I could with Lyra holding me in place."

    L "\"Although that won't really matter once we get rid of all those barbarians.\""

    "..."

    hide lyra normal at right
    show lyra surprised at right
    L "\"Oh! I forgot that you can't move at all. I'll let you go right away.\""
    hide lyra surprised at right
    show lyra happy at right
    L "\"Hehe...sorry about that.\""

    "Did I hear that correctly? Lyra just said that the government wants to \'get rid\'' of the people in the other world."
    "I remembered how Ben looked right before I came back, how angry Calliope was."
    "I remembered the sinking feeling in my chest when it happened."
    "I didn't want anyone else to have to feel that way."

    "My emotions were buzzing, and the sound from the mirror grew louder and louder in my head."
    "Anger? Frustration? Confusion?"
    "I felt all of it."
    "How could I stop the government's plan when I'm so powerless?"
    "As thoughts were racing through my head, I could feel a tingling sensation building up within my body and spreading to the tips of my fingers."
    "Could it be...that?"
    "People here don't use magic like those fireballs I saw before, but it's worth a shot."

    "Lyra released me, and I swung to the side."
    hide lyra happy at right
    show lyra surprised at right

menu:
    "Destroy the mirror":
        jump break_mirror_choice

    "Attack Lyra":
        jump keep_mirror_choice

label break_mirror_choice:
    "I threw my arms in the direction of the mirror, and a blast of magical energy barreled towards it."
    hide lyra surprised at right with moveoutright
    "Almost immediately, I felt someone hit my neck, and I fell to the ground."
    "As my vision faded, I could see the see the shattered pieces of the mirror next to me."
    scene finalcave_closest_blurred with fadehold
    scene black with fadehold

    L "\"Good morning [Protagonist]. Did you sleep well?\""

    scene reflection with fade
    show lyra normal with dissolve
    play music "audio/daytimetheme.mp3" volume 0.8

    P "\"I did. Thank you Lyra.\""

    "That was some dream. It felt so realistic."
    "There were so many things I've never seen before."
    "And I think there was someone who looked a lot like Lyra?"
    "However strange it was, my memory of the dream faded just like any other, and it was as if it had never happened."
    "As I got up out of bed, I caught sight of something weird in the corner of my eye."

    stop music fadeout 5.0
    scene reflection_blurred with dissolve

    "Lyra's reflection looked...different."
    scene black with slowfadehold
    play audio [ "<silence 3.0>", "audio/dragon_roar.mp3" ]
    scene mirror_dragon with slowfade
    scene black with slowfade
    stop audio
    return

label keep_mirror_choice:
    show lyra surprised at right
    "I threw my arms in the direction of Lyra, and a blast of magical energy barreled towards her."
    "She would normally easily be able to avoid something like that, but I think she was frozen with shock."
    "The blast knocked her to the ground. I'd never seen her this angry before, but I didn't even care as she started shouting at me."
    with vpunch
    hide lyra surprised at right with moveoutright
    "I was already running towards the mirror."

    hide lyra surprised at right
    show lyra angry3 at right with hpunch
    L "\"HOW DARE YOU?!\""
    L "\"We gave you a perfect life, and you're willing to just throw it all away?\""
    L "\"Remember this. Your worthless life will be anything but perfect from this point on.\""
    L "\"I will personally make sure that it's even more of a living hell than that wretched place you're going.\""

    scene black with flash

    "..."
    play music "audio/daytimetheme.mp3" volume 0.8
    "It's been a year since I left my \'perfect\' life."
    "They began their attacks months ago, but we were prepared."
    "As soon as I got here, I found Calliope and told her about the government's plans."
    "We traveled all over this world and somehow convinced people that they should be worried."

    scene end_scene with dissolve
    show calliope normal with dissolve
    G "\"[Protagonist], come on! We gotta get going to the next town. They're running low on supplies.\""

    "My life has definitely been turned upside down, but there's excitement every day. I'd say that's something worth fighting for."
    stop music fadeout 5.0
    scene black with slowfadehold
    play audio [ "<silence 3.0>", "audio/dragon_roar.mp3" ]
    scene mirror_dragon with slowfade
    scene black with slowfade
    stop audio

    return

    #end ch6
