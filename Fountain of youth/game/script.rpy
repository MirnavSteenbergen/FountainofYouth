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

transform slightleft:
    xalign 0.15
    yalign 1.0

transform slightright:
    xalign 0.85
    yalign 1.0



# The game starts here.

label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ renpy.movie_cutscene("Intro_MIND_v02.webm")

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show dad at slightleft
    show mom at slightright
    f "You've created a new Ren'Py game."
    m "yh amazing"



    # These display lines of dialogue.

    f "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
