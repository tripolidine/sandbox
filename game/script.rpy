# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.

init python:

    import random

    def randomize_name():
        return "%s %s" % ( random.choice( [ 'Spunky', 'Ugly', 'Thirsty', 'Wacky', 'Visceral', 'Contagious', 'Sock-Munching' ] ), random.choice( [ 'Badger', 'Hippo', 'Walrus', 'Aardvark', 'Rhino', 'Ocelot', 'Wombat', 'Platypus' ]) )

    def char_name(real_name, vague_name, is_known):
        if is_known:
            return real_name
        return vague_name

# The game starts here.
label start:

    $ calDate = calDate.replace(second=10, hour=12, minute=30, day=2, month=7, year=2012)
    define studio_name = randomize_name()

#    call calendar(1)

    call onboarding


