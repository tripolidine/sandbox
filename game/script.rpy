# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.

define debug_skip_bullshit = True

init python:

    import random

    def randomize_name():
        return "%s %s" % ( random.choice( [ 'Spunky', 'Ugly', 'Thirsty', 'Wacky', 'Visceral', 'Contagious', 'Sock-Munching' ] ), random.choice( [ 'Badger', 'Hippo', 'Walrus', 'Aardvark', 'Rhino', 'Ocelot', 'Wombat', 'Platypus' ]) )

    def char_name(real_name, vague_name, is_known):
        if is_known:
            return real_name
        return vague_name

    def get_player_name(prompt):
        name = renpy.input(prompt)
        name = name.strip()

        if not name:
            return ""

        return name

    register_stat("Skepticism", "skepticism", 0, 100)
    register_stat("Pessimism", "pessimism", 0, 100)
    register_stat("Fear", "fear", 0, 100)
    register_stat("Fatigue", "fatigue", 0, 100)
    register_stat("Artistry", "artistry", 0, 100)
    register_stat("Diligence", "diligence", 0, 100)
    register_stat("Courage", "courage", 0, 100)
    register_stat("Fitness", "fitness", 0, 100)
    register_stat("Anxiety", "anxiety", 0, 100)
    register_stat("Obsequiousness", "obsequiousness", 0, 100)
    register_stat("Charisma", "charisma", 0, 100)
    register_stat("Alcoholism", "alcoholism", 0, 100)

    dp_period("Morning", "morning_act")
    dp_choice("Get down to business.", "getbusy")
    dp_choice("Socialize in the break room.", "socialize")

    dp_period("Evening", "evening_act")
    dp_choice("Play video games.", "video_games")
    dp_choice("Go out drinking.", "drinksocially")
    dp_choice("Drink alone.", "drinkalone", show="alcoholism > 20 and charisma < 20")
    
# The game starts here.
label start:

    $ days_total = 0

    $ salary = 35000.0

    $ calDate = calDate.replace(second=10, hour=12, minute=30, day=2, month=7, year=2012)

    define studio_name = randomize_name()

    scene black

    if not debug_skip_bullshit:
        call onboarding

    jump new_day

label new_day:

    $ days_total += 1
#    call calendar(1)

    $ morning_act = None
    $ evening_act = None

    $ narrator("What should I do this morning?", interact=False)


label morning:

    "Morning"

    call screen day_planner(["Morning"])

    $ period = "morning"
    $ act = morning_act

    call events_run_period

label evening:


    "Evening"

    call screen day_planner(["Evening"])

    $ period = "evening"
    $ act = evening_act


    call events_run_period

label night:

    "Night"

    "Time for go to bed."

    call events_end_day

    jump new_day

label dp_callback:

    $ narrator("What should I do today?", interact=False)

    return
