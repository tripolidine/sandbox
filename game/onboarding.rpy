image bg office_exterior = "office_genericRoom.jpg"
image bg hr_office = "office_genericRoom.jpg"
image bg desk = "office_desk.jpg"
image bg office_generic = "office_straightOn.jpg"


label onboarding:

    scene bg office_exterior

    "At last... after all these years, I've finally made it."
    "I somehow managed to get hired by the renowned video game studio, [studio_name] Games...{w} even though I have no training or experience to speak of."
    "But what I lack in experience, I think I more than make up for in raw enthusiasm... not to mention my copious spunk."
    "I can't wait to get started!"

    $ calDate.replace(second=10, hour=12, minute=30, day=2, month=7, year=2012)
    call calendar(1)

    scene bg office_generic at ken_burns(anchory=0.5, duration=10, maxzoom=1.1) with dissolve

    "(It looks like a normal office in most ways... but with a lot more toys on the desks.)"

    p "A lot of people must bring their kids to work! That's nice."

    show jane at right_to_left

    "(A girl shuffles past with a cup of coffee in her hand. {w}She doesn't seem to take any notice of me...)"

    show hr happy at right_third with easeinright

    hr "Hi there!{p} You must be the new hire. Welcome to [studio_name]!"
    hr "I'm Susan, from the HR department. I'll be handling your onboarding this lovely morning."

    $ knows_susan = True

    hr "Give me just a second to print out the forms."

    "(Some documents are slowly being printed...)"

    hr "So, is this your first time in the bay area?"

    menu:

        "Sure is.":
            hr "Bet you're enjoying this weather, huh? Ha ha!"
            hr "It's a great place to live, but a little on the expensive side. As I'm sure you've noticed!"

        "I've visited a few times.":
            hr "It's a great place to visit. You know, when you live here, it all starts to feel a bit routine."
            hr "But it really is a beautiful area. Sometimes I wish I could experience it as a tourist!"

        "I grew up here.":
            hr "Ah, a native! Well, then I guess you know your way around. Great, so I won't have to give you the rundown of the area."

        "...":
            hr "Don't talk much, do you? Well, that's OK... I can gab enough for the both of us. Hah!"

    hr "Ah, looks like those forms are just about ready."
    hr "Now then. First things first... could you please confirm the spelling of your first name?"

    call name_game

    hr "OK, that all looks correct on the paperwork. Nice to meet you, [first_name]."

    hr "Now, for this next question... we ask everybody this because we don't want to make any assumptions."
    hr "But it's not a reflection on the way you look or anything. Just part of the process!"
    hr "What personal pronouns would you prefer that we use for you?{w} If you'd rather not answer, we'll just go with singular 'they.'"

    call figure_out_pronouns
    
    hr "Got it. And I think that's all the information I need from you right now!"
    hr "Thank you for your cooperation. Your department manager will take over from here. Let's go and find him!"

    scene bg desk with dissolve

    show v at left_third with dissolve

    hr "Victor, this is [first_name], the latest addition to your army."

    v "Oh hey!"

    hr "I'll leave [pronoun_them] in your capable hands. [first_name], my door is always open if you need anything. Until then, toodle-oo!"

    hide hr with dissolve

    v "What's uppppp"

    return

label sucked:

    menu:
        hr "Oh no! What happened?"

        "I wrecked my car.":
            hr "Yikes! I hope you're insured."

        "A crazy guy killed a bunch of people.":
            hr "Are you just messing with me? I don't appreciate that."

    return

label name_game:

    python:

        first_name = get_player_name("Please spell your first name.")

        if not first_name or first_name == "":
            first_name = ""
            renpy.say(hr, "You don't have a first name? Well, that's unusual... well then, how about your last name?")
        else:
            renpy.say(hr, "So that's [first_name]? Got it. And your last name?")

        last_name = get_player_name("Please spell your last name.")

        if not last_name or last_name == "":
            if first_name == "":
                renpy.say(hr, "So you're telling me you have no name? Well, that's going to cause a bit of confusion!")
                renpy.say(hr, "Tell you what. From now on, your name is Alex.")
                first_name = "Alex"
            else:
                last_name = ""
                renpy.say(hr, "So you just go by your first name, like Cher?")
                renpy.say(hr, "Well, that's going to cause some headaches for payroll, but I suppose we can handle it.")
        elif first_name == "":
            first_name = last_name
            last_name = ""

        player_name = first_name
        if last_name != "":
            player_name += " " + last_name

    return


label figure_out_pronouns:
    python:
        pronoun_they = renpy.input('Nominative case (e.g. "she/he/they")?').lower() or "they"
        pronoun_them = renpy.input('Objective case (e.g. "him/her/them")?').lower() or "them"
        pronoun_their = renpy.input('Adjectival possessive (e.g. "their/his/her")?').lower() or "their"
        pronoun_theirs = renpy.input('Substantival ppossessive (e.g. "his/hers/theirs")?').lower() or "theirs"

    return

