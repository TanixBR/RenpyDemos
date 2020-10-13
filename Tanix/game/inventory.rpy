label inventory:
    
    "Bem Vindo ao sistema de Inventário Tanix 1.0"

    menu:
        "Inventário Tanix 1.0"
        "Lista de todos Items possíveis":
            jump show_items
        "Lista Items que o jogador possui":
            jump player_items
        "Adicionar item do jogo para o jogador":
            jump player_items
        "Retornar ao menu principal":
            jump start_menu

label show_items:

    $item_names = game.getItemNames()
    $lista_items = ""
    while item_names:
        $lista_items += item_names.pop() + ", "

    show text "Items do sistema: [lista_items]"

    pause 2.0

    hide text

    jump inventory

label player_items:

    $item_names = game_player.items
    $lista_items = ""
    while item_names:
        $lista_items += item_names.pop() + ", "

    show text "Items do jogador: [lista_items]"

    pause 2.0

    hide text

    jump inventory
