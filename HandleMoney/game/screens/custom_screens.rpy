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