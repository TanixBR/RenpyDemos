label start:

    "Bora lá Iniciar o Tanix v1.0 Core"

    #init Player on start
    $game_player = player()
    $MC = Character(game_player.player_name, color='#f0f055')

    $evento = 0

    jump start_menu

label start_menu:

    menu:
        "Qual Tutorial gostaria de ver?"        
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
        "Controlar Evento V1":
            jump controlar_evento

label controlar_evento:
    "Controle do Evento"
    if evento == 3:
        jump dormir
    else:
        $evento += 1
        "RODANDO [evento] EVENTO"        
        jump controlar_evento

label dormir:
    $evento = 0
    "Dorme pra zerar o Evento"
    jump controlar_evento
