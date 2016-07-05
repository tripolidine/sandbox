# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.

init python:

    import random

    def randomize_name():
        return "%s %s" % ( random.choice( [ 'Spunky', 'Ugly', 'Thirsty', 'Wacky', 'Visceral', 'Contagious', 'Sock-Munching' ] ), random.choice( [ 'Badger', 'Hippo', 'Walrus', 'Aardvark', 'Rhino', 'Ocelot', 'Wombat', 'Platypus' ]) )


# The game starts here.
label start:
    define studio_name = randomize_name()

    call onboarding


