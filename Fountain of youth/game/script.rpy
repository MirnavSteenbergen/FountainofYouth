# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Father", color="#00FFFF")
define m = Character("Mother", color="#FF00FF")
define p = Character("Priest", color="#00FFFF")
define b = Character("Peter", color="#00FFFF")
define bs = Character("Rowen", color="#00FFFF")
define uf = Character("???", color="#FF00FF")
define um = Character("???", color="#00FFFF")
define w = Character("Edith", color="#FF00FF")
define i = Character("Osbert", color="#00FFFF")
define y = Character("[player_name]")


# transform locations
transform slightleft:
    xalign 0.15
    yalign 1.0

transform slightright:
    xalign 0.85
    yalign 1.0

# The game starts here.

label start:
    $ player_name = ""
    # Define variables for test
    $ logos = 0
    $ ethos = 0
    $ pathos = 0

    scene black

    $ player_name = renpy.input("What is your name adventurer?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "You"


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ renpy.movie_cutscene("Intro_MIND_v03.webm")

    scene home_inside2
    play music roomsound

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show dad_m at slightleft

    # These display lines of dialogue.
    f "I hope he can do something for her. But when and how did she sin so much to deserve this?"
    f "I think she hasn't..."

    "Comfort your father"

    menu:
        "A prayer will help":
            $ pathos += 1
            jump prayer
        "I don't think he can help her, maybe we should look to a witch.":
            $ logos += 1
            $ ethos += 1
            jump magic

label prayer:
    y "We should pray for forgiveness. Maybe the priest can ask the community to pray with us, everybody here knows and loves mother."
    f "But will it help? You have seen how sick she is, her recovery would be a miracle. I will be honest with you, (starts to whisper) I considered looking for a witch for help."
    menu:
        "We just need to have faith":
            jump faith
        "The witch could be our last resort":
            jump magic_lr

label faith:
    y "We just need to have faith father. Maybe this is not just a punishment for mother but a test of faith for us."
    f "Maybe..."
    jump priest_enters

label magic:
    y "I don't think he can help her, maybe we should look to a witch."
    f "(whispering) I'll admit it crossed my mind a couple of times, but it would be against the church."
    menu:
        "The witch could be our last resort.":
            jump magic_lr
        "I don't think prayers will heal mother. Finding a witch is our only chance.":
            jump magic_confirmed

label magic_confirmed:
    y "I don't think prayers will heal mother. Finding a witch is our only chance."
    f "I worry too, let's do it. But we need need to keep this plan quiet, the church will throw us out if they find out."

label magic_lr:
    y "The witch could be our last resort father, if the prayers don't help."
    f "We should keep that idea quiet then, the church would throw us out."
    jump priest_enters

label priest_enters:
    "The priest walks in from the bedroom."
    show priest at slightright
    p "She isn't doing well. But we have to keep faith, I will announce a community prayer to be held for her tonight. God be with her."
    f "Thank you."
    p "I would be able to move her to a hospitality house if you can't take care of her."
    f "Never. I told you this before, I will care for her until the very end."
    "The priest leaves the house."
    hide priest
    f "You should go to work, there is nothing you can do here and you are late already. Peter is probably worried about you."

    stop music fadeout 1.0

label walk_to_work:
    scene townstreets
    play music street_town loop fadein 1.0

    "{i}You walk to work{/i}"

label at_the_blacksmith:
    scene blacksmith_outside
    play sound blacksmith loop fadein 1.0

    show blacksmith at slightright
    b "Here you are! What happened? I was starting to worry you wouldn't show up at all today."

    menu:
        "Sorry I am late, I will go to work right away":
            jump I_am_sorry
        "My mother is gravely ill":
            jump mother_ill

label I_am_sorry:
    y "Sorry I am late, I will go to work right away."
    p "Wait a second, you don't get away with it that easily. You can start cleaning the weapons. Make sure they shine by the end of the day"
    y "But that's Rowen's job, I'm not an apprentice anymore."
    p "You are late, Rowen is doing your job today. You are doing his."

    hide blacksmith
    "{i}You start working, after cleaning a few weapons Peter walks up to you.{/i}"
    show blacksmith at slightright

    p "The church just announced a community prayer for your mother tonight. No wonder you were late, you should have just told me. I'm sorry I was mean earlier, I didn't know. You can leave early today to be there on time."
    p "But about that. Yesterday a group of three people came here to pick up some weapons they had us make. They told me they were on their way to find a magical cure for all ailments. Sounds like something that could help your mother..."

    menu:
        "Please tell me more!":
            jump tell_more
        "Do you think something like that could exist?":
            jump you_sure

label mother_ill:
    y "I am sorry Peter, my mother is gravely ill. The priest came to see her this morning. There will be a community prayer tonight."
    p "Oh no. Poor Mary... and your father... Is he alright?"
    y "He is not sick if that's what you're asking but he surely isn't doing well."

    hide blacksmith
    "{i}You start working, after cleaning a few weapons Peter walks up to you.{/i}"
    show blacksmith at slightright

    p "The church just announced the community prayer for your mother tonight. You can leave early today to be there on time."
    p "But about that. Yesterday a group of three people came here to pick up some weapons they had us make. They told me they were on their way to find a magical cure for all ailments. Sounds like something that could help your mother..."

    menu:
        "Please tell me more!":
            jump tell_more
        "Do you think something like that could exist?":
            jump you_sure

label tell_more:
    y "wow! that would be amazing please tell me more!"
    p "I don't know much more, I only spoke to them briefly. After that they left for the city north of here."
    jump work

label you_sure:
    p "I don't know but the church speaks out against using magic all the time. If magic wouldn't exist then why would they address it so often?"
    p "So I guess a magical cure could definitly exist."

    menu:
        "Please tell me more":
            jump tell_more
        "Start working again":
            jump work

label work:
    hide blacksmith
    "{i} You start cleaning weapons again, after you've cleaned all of them Peter comes to talk to you again.{/i}"
    show blacksmith at slightright
    p "You should go now, it will be evening soon. Go pick up your father for the prayer. You wouldn't want to be late."
    y "Thank you for understanding Peter"

    stop sound
    stop music fadeout 1.0

label tochurch:
    scene townstreets
    play music street_town loop

    "{i}You pick up your father, together you walk to the church.{/i}"
    stop music fadeout 3.0

label calculate_ending:
    scene white
    "You are at the end of your journey, what you probably didn't know is that this was a personality test."
    "For each answer you gave in the game we noted down points for either logos, ethos or pathos."
    "By doing this we now know how to influence you to do or buy something."
    "We bet you are curious already, here are your results."

    if logos > max(ethos, pathos):
        jump logos

    elif ethos > max(logos, pathos):
        jump ethos

    elif pathos > max(logos, ethos):
        jump pathos

    elif pathos == ethos == logos:
        ":o oh my, the ultimate tie. You are very special"
        "About which outcome would you like to read first?"
        menu:
            "logos":
                jump logos
            "ethos":
                jump ethos
            "pahtos":
                jump pathos

    elif logos == ethos:
        "Logos & ethos tie"
        "About which outcome would you like to read first?"
        menu:
            "logos":
                jump logos
            "ethos":
                jump ethos

    elif ethos == pathos:
        "Ethos & pathos tie"
        "About which outcome would you like to read first?"
        menu:
            "ethos":
                jump ethos
            "pahtos":
                jump pathos

    elif logos == pahtos:
        "Logos & pathos tie"
        "About which outcome would you like to read first?"
        menu:
            "logos":
                jump logos
            "pahtos":
                jump pathos

label logos:
    scene logos_result
    $ renpy.pause ()
    menu:
        "read other outcomes":
            jump other_outcomes
        "end the game":
            jump endgame

label ethos:
    scene ethos_result
    $ renpy.pause ()
    menu:
        "read other outcomes":
            jump other_outcomes
        "end the game":
            jump endgame

label pathos:
    scene pathos_result
    $ renpy.pause ()
    menu:
        "read other outcomes":
            jump other_outcomes
        "end the game":
            jump endgame

label other_outcomes:
    "which outcome would you like to read about?"
    menu:
        "logos":
            jump logos
        "ethos":
            jump ethos
        "pahtos":
            jump pathos


# This ends the game.
label endgame:
    "thank you for playing <3"
    return
