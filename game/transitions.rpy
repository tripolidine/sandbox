label transition(period):

    show screen TransitionFrame
    pause 2
    hide screen TransitionFrame
    pause 1

transform transition_swipe(xPos, yPos, t=0):
    subpixel True

#    t*0.1

    on show:
        xalign 0.5 xpos 0.0 xcenter 1.0
        easein 0.5 xcenter 0.5

    on hide:
        xcenter 0.5
        easeout 0.5 xalign 1.0 xpos 0.0

screen TransitionText:
#    at transition_swipe(0.5, 0.35, t=1)
    text period size 72 color "#ffffff" xalign 0.5

screen TransitionFrame:
    frame:
        at transition_swipe(0.5, 0.35, t=1)
        background "#ffff00"
        xsize 100
        ysize 20
        xcenter 0.5
        ycenter 0.35

        #text period size 72 color "#000000" xalign 0.5 at transition_swipe(0.5, 0.5, t=3)
        text period size 72 color "#000000" xalign 0.5

