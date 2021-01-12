# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Father")
define m = Character("Mother")
define p = Character("Priest")
define b = Character("Peter")
define bs = Character("Rowen")
define u = Character("???")
define w = Character("Edith")
define i = Character("Osbert")
define y = Character("You")


# transform locations
transform slightleft:
    xalign 0.15
    yalign 1.0

transform slightright:
    xalign 0.85
    yalign 1.0

# The game starts here.

label start:
    # Define variables for test
    $ logos = 0
    $ ethos = 0
    $ pathos = 0


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ renpy.movie_cutscene("Intro_MIND_v02.webm")

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show dad at slightleft

    # These display lines of dialogue.
    f "I hope he can do something for her. But when and how did she sin so much to deserve this?"
    f "I think she hasn't..."

    "Comfort your father"

    menu:
        "A prayer will help":
            $ pathos += 1
            jump prayer
        "I don't think he can help her, maybe we should look to a witch":
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
    y "I don't think he can help her, maybe we should look to a witch"
    f "(whispering) I'll admit it crossed my mind a couple of times, but it would be against the church."
    menu:
        "The witch could be our last resort":
            jump magic_lr
        "I don't think prayers will heal mother. Finding a witch is our only chance.":
            jump magic_confirmed

label magic_confirmed:
    y "I don't think prayers will heal mother. Finding a witch is our only chance."
    f "I worry too, let's do it. But we need need to keep this plan quiet, the church will throw us out if they find out."

label magic_lr:
    y "The witch could be our last resort father, if the prayers don't help"
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
    f "You should go to work, there is nothing you can do here and you are late already. Peter is probably worried about you."



label calculate_ending:
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
    "You are a logos person yay"
    menu:
        "read other outcomes":
            jump other_outcomes
        "end the game":
            jump endgame

label ethos:
    "You are an ethos person yay"
    menu:
        "read other outcomes":
            jump other_outcomes
        "end the game":
            jump endgame

label pathos:
    "You are a pathos person yay"
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
