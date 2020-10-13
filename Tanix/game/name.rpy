label set_name:
    #Call Screen to set Player Name
    call screen input_name(game_player.player_name)
    $game_player.player_name = _return
    $MC = Character(game_player.player_name, color='#f0f055')
    
    "Here we go!!!! [game_player.player_name]"

    jump start_menu