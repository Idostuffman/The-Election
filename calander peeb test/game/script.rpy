# Define variables
define days = ["Day 1", "Day 2", "Day 3"]  # List of days
default current_day = 0  # Start with Day 1 (index 0)
default choices = {}  # Dictionary to store player choices
define maya = Character("Maya",color="#B4321C")
define kiki = Character("Kiki",color="#BC4C41")
define mymy = Character("Mymy", color="#FF8822")
define coco = Character("Coco", color="#FFD9AD")
define vera = Character("Vera", color= "#BF9CBC")
define sjef = Character("Sjef",color="#84A3B8")
define ilse = Character("Ilse",color="#1C1F30")
define rens = Character("Rens", color="#A84559")
define yfke = Character("{color=#87FBDC}Y{/color}{color=#FFABEC}fk{/color}{color=#87FBDC}e{/color}")
define zoey = Character("Zoey", color= "#D5B4D1")
define roos = Character("Roos", color="#E2A14F")
define cleo = Character("Cleo", color="#BB7734")
define tryn = Character("{color=#AE1C28}Tr{/color}{color=#21468B}yn{/color}")
define both = Character("{color=#FF8822}Mymy{/color} {color=#FFFFFF}and{/color} {color=#BC4C41}Kiki{/color}")
default talked_to_char1 = False
default talked_to_char2 = False
default talked_to_char3 = False
default talked_to_char = False
default ongezellig = False

image coco = "coco.png"
image vera = "vera.png"
image mymy = "mymy.png"
image kiki = "kiki.png"
image cleo = "cleo.png"
image sjef = "sjef.png"
image ilse = "ilse.png"
image rens = "rens.png"
image rensgaming = "rens2.png"
image roos = "roos.png"
image tryn = "tryn.png"
image yfke = "yfke.png"
image zoey = "zoey.png"
image zoeybook = "zoey2.png"
image class = im.Scale("class.png", 1920, 1080)
image school = im.Scale("school.png", 1920, 1080)
image class1 = im.Scale("class1.png", 1920, 1080)
image screen calendar = im.Scale("date.png", 1920, 1080)
image screen2 = im.Scale("date2.png", 1920, 1080)
image screen22 = im.Scale("date22.png", 1920, 1080)
image screen3 = im.Scale("date3.png", 1920, 1080)
image screen33 = im.Scale("date33.png", 1920, 1080)
image rensgaming2 = "rens3.png"
image credits = Movie(play="audio/Credits.webm",delay=2, stop_music=True)

# Start of the game
label start:
    play music "class.mp3" loop
    scene class with dissolve
    maya "Maybe those four hours of sleep weren’t the best idea... or biking here..."
    "Maya rose from her desk, looking around groggily, her eyes still foggy from sleep."
    show coco with dissolve
    coco "Hoi, Maya! Didn’t expect you to be here so early."
    maya "{i}Am I still dreaming? Why does Coco look so... weird?{/i}"
    "Maya rubbed her eyes, hoping it would make Coco look less... weird, but sadly, to no avail."
    maya "Uh... yeah, I just got here early to do some... stuff... yeah, stuff."
    coco "Ah, okay. Well, you know those neat things that tell you the day and date?"
    maya "Uh... calendars?"
    coco "Yeah, those! They’re super neat. They tell you what day it is and what you have to do."
    coco "Well, I accidentally bought two, and I was wondering if you might want one?"
    coco "With all the meetings and appointments I have, it’s such a handy tool!"
    maya "{i}Of course the princess has...{/i}"
    maya "Yeah... thanks, Coco, but I don’t need it. My phone has something like that."
    coco "Oh, that’s nice! Technology has really come a long way. Well, use it responsibly!"
    maya "Yeah...\n{i}What day is it even today?{/i}"
    "She pulled out her phone, searching for her calendar app. After three minutes of looking, she finally found it. Maya never bothered to use it since her phone screen always showed the date."
    scene screen calendar with dissolve
    pause 1.0
    maya "{i}Monday? This day is going to suck...{/i}"
    jump day_1

# Label for Day 1
label day_1:
    scene class with fade
    maya "{i}First Period...homeroom with Ms. Mid Life Crises.{/i}"
    maya "{i}I hate that ha-{/i}{p=1}{nw} "
    stop music fadeout 1.0
    play sound "bell.mp3"
    "RRRRRRRRRRRRRRRIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNGGGGGGGGGGGGGGGGGGGGGGGGG"
    scene class1 with dissolve
    show vera with dissolve
    vera "Hello, class. Let's get to the first item on my list: class president. There are still two slots open for those who want to run. The vote will be held on Wednesday."
    vera "Now, is there anyone among you buggers who wants to-{p=1}{nw}"
    both "I want to do it, Ms. Persijn!"
    "Mymy and Kiki both looked at each other with suspicion, scanning the room to figure out who would certainly vote for them, who they still needed to convince, and how to triumph over the other."
    vera "Sure, why not."
    vera "Anyways, moving on to the second item on my list: keep yourselves busy. So yeah, do that while I... scroll through my... emails."
    hide vera with dissolve
    "Finishing her little monologue, Vera sat down in her chair and booted up her computer, scrolling through her \"emails\" while sipping fresh coffee from her cup."
    scene class with fade
    play music "class.mp3"
    "While Vera was busy with her \"work,\" Maya decided it was a good time to drift off to dream island... if it weren't for Mymy."


    show mymy
    mymy "MAYA!"
    mymy "I need your help! Your dirty little Belgian hands need to help me become class president! You still owe me for that wonderful presentation I did about your hometown, remember?"
    maya "But I don't come from Braba-{p=1}{nw}"
    "Mymy laid her hand on Maya's shoulder, squeezing it hard and making Maya uncomfortable in the process."
    mymy "It won't be anything special, Maya. You just need to convince some of the... nice people in our class to vote for me. I'll give you a Stroopwafel juice box!"
    "The ginger-haired girl looked at her and talked with such confidence that Maya almost believed her."
    mymy "So, will you help me?"
    menu:
        "I guess...":
            $ choices["Day 1"] = "Mymy"
            maya "I guess...if you leave me alone for a month."
            mymy "Mhm...I'll take that deal! Well, we will talk tomorrow!"
            hide mymy with dissolve
            "{i}The Date for the Vote has been saved in your calendar.{/i}"
            pause 1.0
            jump next_day

        "No...":
            maya "No...I can't sorry..."
            mymy "It's alright...but just so you know, when I get into power, you will be {b}begging for mercy.{/b}"

    hide mymy with dissolve
    "Before Maya could go back to sleep, another Person came to annoy her."
    show kiki
    kiki "Ahoy Maya!"
    kiki "Would ya' like to help a \"soon to be captain of a ship\"?"
    maya "With what?"
    kiki "Oh, I need help with becomin' class president! I think I won't beat yer sister, so could ya' please help a poor little pirate like me?"
    menu:
        "I guess...":
            $ choices["Day 1"] = "Kiki"
            maya "I guess...why not?\n{i}Altough Pipi probably won't leave me alone for the coming months if I do that...altough it's always fun to see her mad.{/i}"
            kiki "Glad to have you in my crew! See ya' tomorrow!"
            hide kiki with dissolve
            "{i}The Date for the Vote has been saved in your calendar.{/i}"
            pause 1.0
            jump next_day

        "No...":
            maya "No...I can't...sorry Kiki."
            kiki "Oh that's ok, and no worries, when I take over, I'll make sure you won't ever walk the plank."
            hide kiki with dissolve
            pause 1.0
            jump next_day
# Label for Day 2
label day_2:
    stop music fadeout 1.0
    # Check the choice from Day 1
    if choices.get("Day 1") in ["Kiki", "Mymy"]:
        scene screen22 with dissolve
        pause 1.0
    else:
        scene screen2 with dissolve
        pause 1.0
    play music "class.mp3" loop
    scene class with dissolve
    maya "{i}Should I get \"City Living\" or \"Seasons\"? Maybe if I skip lunch a few times, I could maybe get both...{/i}" 
    # Conditional dialogue based on the choice
    if choices.get("Day 1") == "Kiki":
        "Before Maya could decide which Sims 4 DLC she should get, she was interupted by her name being called."
        show kiki with dissolve
        kiki "Ahoy Maya! Before we start, I wanna thank ya' for helping me! Anyways, I know that three people in the class definitely won’t vote for me. Can ya’ maybe talk to ‘em and try to convince ‘em? You know?"    
        maya "Talk? {i}Jesus, why did I agree to this? All of these fucks hate the living shit out of me...{/i}"
        kiki "Yeah just use some of yer'...Maya charm or whatever...you got this!"
        maya "Ok...I guess, who do you want me to convience?"
        kiki "Sjef, Rens and Ilse, can you do that?"
        maya "I guess..."
        kiki "Alright, I'll leave it to ya' matey"
        hide kiki with dissolve
        "After she left, Maya got up from her desk and scanned the Classroom."
        maya "{i}Sigh...who to talk first...{/i}"
        jump char1

    elif choices.get("Day 1") == "Mymy":
        "Before Maya could decide which Sims 4 DLC she should get, she was interupted by her name being called."
        show mymy with dissolve
        mymy "Maya! So, here's the plan, there's a few non-believers here, who think, that I'm not fit for the job, could you maybe talk some sense into them?"    
        maya "Talk? {i}Jesus, why did I agree to this? All of these fucks hate the living shit out of me...{/i}"
        mymy "Yeah just use some of your inferior belgian autistic talking skills."
        maya "Ok...I guess, who do you want me to convience?"
        mymy "Cloe, Zoey and Yfke, can you do that?"
        maya "I guess..."
        mymy "Alright, I'll leave it to you."
        hide mymy with dissolve
        "After she left, Maya got up from her desk and scanned the Classroom."
        maya "{i}Sigh...who to talk first...{/i}"
        jump char2
    else:
        jump mayasthoughts
# Label for Day 3
label day_3:
    window hide
    stop music fadeout 1.0
    if choices.get("Day 1") in ["Kiki", "Mymy"]:
        scene screen33 with dissolve
        pause 1.0
    else:
        scene screen3 with dissolve
        pause 1.0

    scene class1 with dissolve
    show vera with dissolve
    window show
    vera "Welp here are the results...the class president is..."  

    scene class with dissolve
    show mymy with dissolve
    mymy "{i}Onegai desu, kamisama, moshi hontoni sonzai suru nara, watashi ga kateru yo ni shite kudasai. Soshite, rainen wa sutooropuwafuru o issai tabemasen.{/i}" 
    hide mymy with dissolve
    show kiki with dissolve
    kiki "{i}Please Neptune, let me win, if I win I'll stop reading all those Jack Sparrow fanfictions.{/i}" 

    window hide
    scene class1 with dissolve
    show vera with dissolve
    pause 2.0
    window show
    vera "Tryn" 
    play sound "wat.mp3"
    maya "What."
    both "What."
    
    scene class with dissolve
    show tryn with dissolve
    tryn "Yippe! Ik heb gewonnen! Dit is waarschijnlijk de gelukkigste dag van mijn leven!"

    vera "and Vice President is Roos, congratulations or something."  

    show roos with dissolve
    roos "Yay!"

scene class with dissolve
if choices.get("Day 1") == "Kiki":
    stop music fadeout 1.0
    play music "mymylooses.mp3" loop
    show kiki with dissolve

    if not ongezellig:
        kiki "Well, I at least got 3 Votes, thanks to you... thanks Maya, I owe ya'!"
        maya "No problem... happy to... help."
        hide kiki with dissolve
        maya "{i}This was...kinda nice...talking with people...{/i}"
        maya "{i}But I'm never doing that ever again.{/i}"
        jump end_game
    else:
        kiki "Maya...you didn't...ehm...yeah it's alright! But no worries, if I take over, you still won't walk the plank!"
        hide kiki with dissolve
        maya "{i}...{/i}"
        maya "{i}I feel like shit...{/i}"
        maya "{i}Whatever...I don't need to talk to anyone, anyways...it's better that way...{/i}"
        jump end_game

elif choices.get("Day 1") == "Mymy":
    stop music fadeout 1.0
    play music "mymylooses.mp3" loop
    show mymy with dissolve

    if not ongezellig:
        mymy "Looks like your autistic Charm did work, but only on 3 People...but a deal is a deal, take this."
        maya "It's...it's empty..."
        mymy "Upps...welp, see you later Belge."
        hide mymy with dissolve
        maya "{i}I hope you get run over by a truck...{/i}"
        maya "{i}But...this was...kinda nice...talking with people...{/i}"
        maya "{i}But I'm never doing that ever again.{/i}"
        jump end_game
    else: 
        mymy "Maya! You didn't help at all, I knew your autistic ass couldn't handle that. Thanks for nothing."
        hide mymy with dissolve
        maya "{i}I hope you get run over by a truck...{/i}"
        maya "{i}I don't need to talk to anyone...it's better that way...{/i}"
        jump end_game

else:
    maya "{i}Meh, better than Pipi. I'm happy with that.{/i}"
    
    jump end_game

# Handle advancing the day
label next_day:
    $ current_day += 1
    if current_day < len(days):
        if current_day == 1:
            jump day_2
        elif current_day == 2:
            jump day_3
    else:
        jump end_game

# End of the game
label end_game:
    $ renpy.movie_cutscene("videos/Credits.webm", delay=19, stop_music=True) 
    scene black
    if choices.get("Day 1") == "Kiki":
        maya "{i}Maybe I should have helped Mymy...{/i}"
        return

    elif choices.get("Day 1") == "Mymy":
        maya "{i}Maybe I shouldn't have helped Mymy...{/i}"
    else:
        maya "{i}Maybe I should have talked with someone...{/i}"
    return


label char1:
        window hide
        scene class
        menu:
            "Talk to Sjef" if not talked_to_char1:
                $ talked_to_char1 = True
                jump Sjef

            "Talk to Rens" if not talked_to_char2:
                $ talked_to_char2 = True
                jump Rens

            "Talk to Ilse" if not talked_to_char3:
                $ talked_to_char3 = True
                jump Ilse

            "Go back to your seat":
                window show
                if talked_to_char1 and talked_to_char2 and talked_to_char3:
                    maya "{i}Well that was everyone...it was kinda...nice...{/i}"
                    jump day_3
                else:
                    maya "{i}I can't do this...sorry...{/i}"
                    "Maya returned to her seat and settled into her trademark sleeping pose once again."
                    $ ongezellig = True
                    jump mayasthoughts



label char2:
        window hide
        scene class
        menu:
            "Talk to Zoey" if not talked_to_char1:
                $ talked_to_char1 = True
                jump Zoey

            "Talk to Yfke" if not talked_to_char2:
                $ talked_to_char2 = True
                jump Yfke

            "Talk to Cleo" if not talked_to_char3:
                $ talked_to_char3 = True
                jump Cleo

            "Go back to your seat":
                window show
                if talked_to_char1 and talked_to_char2 and talked_to_char3:
                    maya "{i}Well that was everyone...it was kinda...nice...{/i}"
                    jump day_3
                else:
                    maya "{i}I can't do this...sorry...{/i}"
                    "Maya returned to her seat and settled into her trademark sleeping pose once again."
                    $ ongezellig = True
                    jump mayasthoughts

label Zoey:
    scene class
    "After searching for her for four minutes, she found her behind a huge book, peeking her hair and eyes out. Maya trembled as she got near her."
    maya "{i}How do I approach someone who doesn't even talk to anyone...{/i}"
    show zoeybook with dissolve
    window hide
    pause 2.0
    window show
    zoey "..."
    maya "..."
    zoey "..."
    hide zoeybook
    show zoey
    window hide
    pause 2.0
    window show
    zoey "..."
    maya "..."
    zoey "..."
    hide zoey
    show zoeybook
    window hide
    pause 2.0
    window show
    maya "{i}Fuck...this is going to be harder than I expected.{/i}"
    zoey "What do you want, Maya?"
    maya "{i}Oh that was easy...{/i}"
    maya "Ehm... I wanted to ask if you might want to... if you could maybe vote for Mymy in the upcoming election?"
    zoey "Yeah, whatever."
    maya "Oh ok...thanks. {i}It was that easy?{/i}"    
    hide zoeybook with dissolve
    jump char2

label Yfke:
    scene class
    "Yfke was hard to ignore, she was the tallest in the class, after all... and probably one of the highest too."
    show yfke with dissolve
    yfke "Neayh..."
    jump yfkeq
label yfkeq:
        scene class
        show yfke
        menu:
            "Hey Yfke...I wanted to ask...":
                if not talked_to_char:
                    maya "Hey Yfke...I wanted to ask...if you maybe could..."
                    yfke "..."
                    maya "Hello?"
                    yfke "..."
                    $ talked_to_char = True
                else:
                    maya "What I wanted to say is..."
                    yfke "..."
                jump yfkeq

            "Neayh...":
                maya "Neayh..."
                yfke "Neayh?"
                maya "Neayh!" 
                yfke "Neayh neayh neayh?"  
#Idostuff made this game, hello programmers, if you see this you're epic and cool!
                maya "Neeeeaayyyhhh."  
                yfke "Neayhehehe..." 
                hide yfke with dissolve
                "Maya walked away from the conversation, her eyes wide with surprise. She had amazed even herself, she had mastered the language of the Stoners."
                jump char2

label Cleo:
    scene class
    "The biggest Goth in the city, was currently just chilling in the classroom, scribbling in her notebook what Maya presumed to be lyrics."
    show cleo with dissolve
    cleo "Ok, I’ll cut straight to the chase."
    "The girl said without looking up from her notebook."
    cleo "I hate that ginger idiot as much as the next person here, but I’ll vote for her under one condition."
    maya "...and that is?"
    cleo "Let us practice in peace! Last time, she waltzed in and wanted us to play some music by Andre Hazes. It was anoying as fuck. If you can promise me to keep her out for the coming months, I'll give her my vote."
    maya "I'll do my best."
    hide cleo with dissolve
    jump char2

label Sjef:
    scene class
    "Sjef, a Guy you never really saw without a sketchbook in his hands. He drew some posters for Coco's band if Maya remembered correctly."
    show sjef with dissolve
    sjef "...pizza man fights a...pizza with a...pizza face..."
    "Also he might be a bit insane, but Maya didn't bother to think about that right now."
    maya "Ehm...hey Sjef, would you maybe, like vote for Kiki ehm...in the coming up election?"
    sjef "KIKI!? OH FIDDLE STICKS, I STILL NEED TO DO HER PIRATES OF THE CARIBBEAN SHIP COMMISION!!! Thanks for reminding me!"
    hide sjef with dissolve
    "And of he went, back to his sketchbook, back to drawing cheese people, pizzas and strange looking pizza bakers."
    jump char1

label Rens:
    scene class
    "If you ever wanted to talk about anything Nintendo or Video game related, Rens was your man. Whether it was a Game Boy Advance SP or a Nintendo 3DS, he always had a console with him."
    show rensgaming with dissolve
    play sound "chibirobo.mp3"
    pause 1.0
    "And of course today was no exception."
    maya "Hey Rens, I was wondering... Kiki is running for class president..."
    rens "Uh-huh... sure, sounds cool."
    maya "Ehm...and it would be very...ehm epic? If you could vote for her."
    rens "Yeah, yeah... but not right now, I’m busy with beating this level. This game’s so messed up."
    maya "What? It can't be that bad...it’s just a game, right?"
    hide rensgaming
    stop sound fadeout 1.0
    show rensgaming2
    window hide
    pause 2.0
    window show
    rens "Just a game?"
    rens "JUST A GAME?!?"
    rens "Sweetie, this is Chibi Robo Zip Lash and it shows exactly what's wrong with today's games."
    rens "Just because a game doesn't inherently have terrible level design or any major bugs or glitches, that doesn't mean it's fine! It just means it works!"
    rens "Just because a game works doesn't mean it's good. I don't like playing this game! I hate what it stands for! I don't like that they made fans of Chibi-Robo buy this with the hope of Chibi-Robo having a future!"
    rens "I don't like that they thought so low of people and consumers, thinking that they'll LOVE this generic, TERRIBLE, 2D platformer!"
    rens "I."
    rens "Don't."
    rens "Like."
    rens "This."
    rens "Game!"
    stop music
    play sound "ren crash out.mp3"
    show rens
    window hide
    pause 4.0
    window show
    rens "If you would excuse me, I need to go to the bathroom and cry."
    hide rensgaming2
    hide rens with dissolve
    window hide
    pause 1.0
    play sound "wat.mp3"
    window show
    maya "{i}What.{/i}"
    play music "class.mp3" loop
    jump char1

label Ilse:
    scene class
    "Next to Coco, Ilse was one of the nicest people in this class. It didn't matter whose birthday it was or what holiday it was; she would always bring a homemade cake or cookies, to which Maya never said no."
    show ilse with dissolve
    ilse "Hi Maya, how are you doing?"
    maya "Hey...I'm alright...I wanted to ask if you could maybe vote for Kiki on Wednesday?"
    ilse "Oh, sorry Maya, but I already promised someone that I would vote for them. However, I'll vote for her as vice president if that's alright!"
    maya "Ehm...yeah...good enough...thanks."
    ilse "Bye Maya, see you later!"
    hide ilse with dissolve
    jump char1

label mayasthoughts:
        scene class
        pause 4.0
        maya "{i}\"I wonder what clothes you wear to school\"\n\"I wonder how you decorate your room\"\n\"I wonder how you\"...\nI wonder if anyone on this earth would love me...{/i}"
        pause 4.0
        maya "{i}I hope they make Season 2 of \"Bokuno Senpai\"...{/i}"
        pause 4.0
        maya "{i}\"Oh Coco you're so great!\", \"Omg your sister is so hot!\", \"Coco you're so talanted!\"\nWhat am {b}I{/b} missing?{/i}"  
        pause 4.0
        maya "{i}...{/i}"    
        pause 4.0
        maya "{i}Hehehe....{/i}" 
        pause 4.0
        maya "{i}\"Sayonara\"? WHAT WAS I THINKING!?{/i}" 
        pause 4.0
        maya "{i}I'm a lot like you...{/i}"
        pause 4.0 
        maya "{i}Today is such a bore...{/i}"
        jump next_day
