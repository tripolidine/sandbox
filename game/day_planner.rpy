# This contains code for the day planner. You probably
# don't want to change this file.
#
# If you want to change the appearance of the day planner,
# look for the dp_ styles in styles.rpy


init -100 python:

    # The title of the done button.
    dp_done_title = "Done Planning"

    # A map from period name to the information we know about that
    # period.
    __periods = { }

    # The period we're updating.
    __period = None
    
    class __Period(object):

        def __init__(self, name, var):
            self.name = name
            self.var = var
            self.acts = [ ]

    def dp_period(name, var):
        __periods[name] = store.__period = __Period(name, var)

    __None = object()
        
    def dp_choice(name, value=__None, enable="True", show="True"):

        if not __period:
            raise Exception("Choices must be part of a defined period.")

        if value is __None:
            value = name
        
        __period.acts.append((name, value, enable, show))
    

    def __set_noncurried(var, value):
        setattr(store, var, value)
        return True
        
    __set = renpy.curry(__set_noncurried)


# Our Day Planner displays the stats, and buttons for the user to choose what to do
# during each period of time defined in "periods".
screen day_planner(periods):  
    # indicate to Ren'Py engine that this is a choice point
    $ renpy.choice_for_skipping()
    window:
        style "dayplanner_window"          
        use display_stats(True, True, True, True)
        use display_planner(periods)            
            
screen display_planner(periods):            
    frame:
        style_group "dp"        
        vbox:
            text "Day Planner" yalign 0.0 xalign 0.5
            hbox:
                $ can_continue = True
                for p in periods:
                    vbox:
                        label p
                        if p not in __periods:
                            $ raise Exception("Period %r was never defined." % p)
                        $ this_period = __periods[p]

                        $ valid_choice = False
                        vbox:
                            style_group "dp_choice"
                            for name, curr_val, enable, should_show in this_period.acts:
                            
                                $ show_this = eval(should_show)
                                $ enable = eval(enable)

                                if show_this:
                                    if enable:
                                        textbutton name action [SetField(store, this_period.var, curr_val), Return()]
                                    else:
                                        textbutton name
                                    
            #if (can_continue):
            #    textbutton dp_done_title style "dp_done_button" action Jump(func)
            #else:
            #    textbutton dp_done_title style "dp_done_button"

