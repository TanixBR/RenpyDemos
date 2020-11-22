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
        "Verificar Final do jogo":
            if game_player.check_savefile("TrueEnd2.txt"):
                "FINAL 2"
                "Tem o True end 2"                                
                return
            elif game_player.check_savefile("TrueEnd.txt"):
                "FINAL 1"
                "Tem to True end 1 e vai criar o 2"   
                $game_player.create_file("TrueEnd2.txt")             
                return
            else:
                "FINAL 0"
                "Criar o TrueEnd.txt"
                $game_player.create_file("TrueEnd.txt")                
                return



