## Show Money Screen ##########################################################
##
## Display Money to the player
##
## DOCS URL?

screen show_money():
    $x = 0
    text "Your money is [game_player.money]"
    for i in str(game_player.money):        
        $number_image = game_player.imagebase.format(i)
        text i:
            xpos x
            ypos 100
        text number_image:
            xpos x
            ypos 150
        #add number_image
        $x += 250

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    key "mouseup_3" action ShowMenu("custom_prefs")
    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

## Quick Menu show ###########################################################
##
## 
## 

screen custom_prefs:
    modal True
    image "main_video"
    textbutton "{size=38}{b}{outlinecolor=#C42B0B}game menu{/outlinecolor}{/b}":
        at zoom3
        xalign 0.96
        ypos 260
        action MainMenu()
    textbutton "{size=38}{b}{outlinecolor=#C42B0B}Saves{/outlinecolor}{/b}":
        at zoom2
        xalign 0.90
        ypos 460
        action SetVariable("pref_menu", False), SetVariable("help_menu", False), ShowMenu("save")
    textbutton "{size=40}{b}{outlinecolor=#C42B0B}Preferencias{/outlinecolor}{/b}":
        at zoom3
        xalign 0.97
        yalign 0.78
        action Hide("preferences"), Hide("save"), ToggleVariable("pref_menu", True), SetVariable("help_menu", False)#interruptor
    textbutton "{size=38}{b}{outlinecolor=#C42B0B}Help{/outlinecolor}{/b}":
        at zoom2
        xalign 0.9
        yalign 0.93
        action ToggleVariable("help_menu", True), SetVariable("pref_menu", False)#interruptor
    if pref_menu == True:
        use preferences
    if help_menu == True:
        use about
    textbutton "{size=40}{b}{outlinecolor=#C42B0B}Voltar{/outlinecolor}{/b}":
        at zoom2
        xalign 0.91
        ypos 590
        action Hide("quick_menu_content"), Return()
    key "mouseup_3" action Return()

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    ## This ensures that any other menu screen is replaced.
    modal True
    tag menu
    style_prefix "main_menu"
    add Movie(play="videos/oa4_launch.webm", pos=(0, 0), anchor=(0, 0), size=(1920, 1080), channel='movie')
    
    text "{size=100}{i}{b}Tanix Dev Team":
        at zoom1
        xalign 0.5
        ypos -400
    
    textbutton "{size=60}{outlinecolor=#4169E1}{i}{b}{color=#F0F8FF}Start{/b}{/outlinecolor}":
        at zoom2
        xalign 0.5
        yalign 0.6
        action Start()
                
    textbutton "{size=60}{b}{i}{outlinecolor=#C42B0B}{color=#FFDAB9}Preferences{/outlinecolor}{/b}":
        at zoom3
        xalign 0.5
        yalign 0.77
        action  ToggleScreen("custom_prefs")

    textbutton "{size=60}{outlinecolor=#DAA520}{i}{b}{color=#FFFFF0}Exit{/outlinecolor}{/b}":
        at zoom2
        xalign 0.5
        yalign 0.92
        action Quit(confirm=not main_menu)

    frame:
        pass


    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"
    
    frame:
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Voltar"):
        style "return_button"

        action Return()

    label title


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30