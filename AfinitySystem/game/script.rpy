label start:

    "Here we go!!!!"

    $game_player.addRelationship("Hanna")
    $game_player.addRelationship("Mayumi")
    $game_player.addRelationship("Gisel")

    $points = game_player.getRelationship('Hanna')

    jump show_points


label show_points:

    $Hanna = game_player.getRelationship('Hanna')
    $Mayumi = game_player.getRelationship('Mayumi')
    $Gisel = game_player.getRelationship('Gisel')

    "We have [Hanna] from Hanna"

    "We have [Mayumi] from Mayumi"

    "We have [Gisel] from Gisel"
    jump add_points

label add_points:

    menu:
        "Give Points to Hanna":
            $game_player.increaseRelationship('Hanna',1)
        "Give Points to Mayumi":
            $game_player.increaseRelationship('Mayumi',1)
        "Give Points to Gisel":
            $game_player.increaseRelationship('Gisel',1)
    
    "Ok Now points were added"

    jump show_points