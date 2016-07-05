image bg office_exterior = "office_genericRoom.jpg"
image bg hr_office = "office_genericRoom.jpg"
image bg desk = "office_desk.jpg"
image bg office_generic = "office_straightOn.jpg"


label onboarding:

    scene bg office_exterior

    "At last... after all these years, I've finally made it."
    "I somehow managed to get hired by the renowned video game studio, Wacky Shack Games...{w} even though I have no training or experience to speak of."
    "But what I lack in experience, I make up for in raw enthusiasm... and spunk."
    "I can't wait to get started!"

    scene bg office_generic with dissolve

    "(It looks like a normal office... but all the desks have lots of toys on them.)"

    show jane at right_to_left
    pause

    "(A girl shuffles past with a cup of coffee in her hand.)"

    show hr happy at right_third with easeinright

    hr "Welcome! We've got some paperwork you'll need to fill out."
    hr "Give me just a second to pull up your files."

    "(Some documents are slowly being printed...)"


    menu:
        hr "So how was the trip?"

        "It was great!":
            hr "Glad to hear it!"

        "It was OK.":
            show hr angry
            hr "Don't want to talk about it? Fine then."

        "It sucked.":
            call sucked

        "...":
            show hr angry
            hr "Don't talk much, do you?"

    return

label sucked:

    menu:
        hr "Oh no! What happened?"

        "I wrecked my car.":
            hr "Yikes! I hope you're insured."

        "A crazy guy killed a bunch of people.":
            hr "Are you just messing with me? I don't appreciate that."

    return
