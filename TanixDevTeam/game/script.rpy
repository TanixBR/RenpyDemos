label start:

    $game_player = player()

    "Hello Word, this its Money show time"

    jump handle_money

label handle_money:

    "Your money is [game_player.money]"

    menu:
        "What you want to do?"
        "credit_money Money +1":
            $game_player.credit_money(1)
            jump handle_money

        "credit_money Money +100":
            $game_player.credit_money(100)
            jump handle_money

        "credit_money Money +1000":
            $game_player.credit_money(1000)
            jump handle_money
        
        "debit_money Money -1":
            $game_player.debit_money(1)
            jump handle_money

        "debit_money Money -1000":
            $game_player.debit_money(1000)
            jump handle_money

        "Credit Max Money":
            $game_player.credit_money(99999999)
            jump handle_money

        "Debit Max Money":
            $game_player.debit_money(99999999)
            jump handle_money

        "Display Money Screen":
            show screen show_money
            "Here is your money"
            jump handle_money