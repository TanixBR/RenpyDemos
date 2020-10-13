label start:

    "Bora lá Iniciar o Tanix v1.0 Core"

    #init Player on start
    $game_player = player()
    $MC = Character(game_player.player_name, color='#f0f055')

    jump start_menu

label start_menu:

    menu:
        "Qual Tutorial gostaria de ver?"
        "Atribuir nome do jogador e personagem principal":
            jump set_name
        "Gerenciar pontos relacionamento":
            jump relationship
        "Gerenciar Inventario":
            jump inventory


