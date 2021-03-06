﻿label start:

    #init Player on start
    $game_player = player()

    #Call Screen to set Player Name
    call screen input_name(game_player.player_name)
    $game_player.player_name = _return
    $MC = Character(game_player.player_name, color='#f0f055')
    
    "Here we go!!!! [game_player.player_name]"

    $game_player.addRelationship("Hanna")
    $game_player.addRelationship("Mayumi")
    $game_player.addRelationship("Gisel")

    MC "Olá obrigado por escolher um nome para mim"

    MC "Configuramos 0 para cada personagem Hanna, Mayumi e Gisel"

    MC "Que tal adicionar alguns pontos de realcionamento para algum desses personagens?"

    jump show_points


label show_points:

    

    $Hanna = game_player.getRelationship('Hanna')
    $Mayumi = game_player.getRelationship('Mayumi')
    $Gisel = game_player.getRelationship('Gisel')

    MC "Atualmente temos [Hanna] para Hanna, [Mayumi] para Mayumi e [Gisel] para Gisel"

    jump add_points

label add_points:

    menu:
        "Quem está ganhando Atualmente?":
            if (game_player.winner):
                MC "O Meu Match que esta ganhando no momento é [game_player.winner]"
                MC "Em caso de empate, a Primeira da lista é a ganhadora"
            else:
                MC "Ocorreu um erro ao pontuar"
        "Adicionar pontos para Hanna":
            $game_player.increaseRelationship('Hanna',1)
        "Adicionar pontos Mayumi":
            $game_player.increaseRelationship('Mayumi',1)
        "Adicionar pontos para Gisel":
            $game_player.increaseRelationship('Gisel',1)
    
    "Parabéns pontos foram adicionados para o personagem a sua escolha, agora vamos ver o placar?"

    jump show_points