
################################################################################
## General Functions
################################################################################

screen display_hover(img):
    add img  

################################################################################
## Input Screen
################################################################################
screen input_name(default_value):

    #add "gui/input_name.png"

    text "ENTER YOUR NAME *THIS SHOULD BE REPLACED BY SOME GUI IMAGE"

    input default default_value:
        xalign 0.25
        yalign 0.43

