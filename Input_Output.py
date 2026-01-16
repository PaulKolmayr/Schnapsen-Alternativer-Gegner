"""
All Inputs and Outputs in one Place
"""

class InputOutput:
    

    def see_won_cards(self):
        corr = False
        while corr == False:
            answer = input("Wollen Sie Ihre gewonnenen Karten ansehen?(Ja/Nein) ")
            if answer == 'Ja' or answer == 'Nein':
                corr = True
            else:
                pass
        return answer


    def show_won_cards(self, won_cards):
        print(f"Gewonnene Spielkarten: {', '.join(str(card) for card in won_cards)}")


    def switch_trumpf(self):
        corr = False
        while corr == False:
            switch = input("Wollen Sie Ihren Buben für die Trumpfkarte tauschen?(Ja/Nein) ")
            if switch == 'Ja' or switch == 'Nein':
                corr = True
            else:
                pass

        return switch


    def opponent_drew_trumpf(self):
        print("Der Gegner hat den Trumpf ausgetauscht!")
    

    def close_the_deck(self):
        corr = False
        while corr == False:
            answer = input("Wollen Sie zudrehen?(Ja/Nein) ")
            if answer == 'Ja' or answer == 'Nein':
                corr = True
            else:
                pass
        return answer
    

    def deck_is_closed(self):
        print("Sie haben zugedreht!")


    def pair_can_be_played(self, pairs):
        print("Es können folgende Paare gespielt werden:")
        for pair in pairs:
            print(pair[0].suit.name)
            print()
        corr = False
        while corr == False:
            decision = input("Wollen Sie ein Paar ausspielen?(Ja/Nein) ")
            if decision == 'Ja' or decision == 'Nein':
                corr = True
            else:
                pass

        return decision
    
    def more_pairs_can_be_played(self):
        decision = input("Welches Paar wollen Sie ausspielen? ")
        return decision
    
    def which_card_to_play(self):
        card = input("Welche Karte wollen Sie spielen? ")
        return card
    
    def playercard_played(self, playcard):
        print()
        print(f"Sie haben folgende Karte gespielt: {playcard}")
    
    def opponentcard_played(self, playcard):
        print()
        print(f"Der Gegner hat folgende Karte gespielt: {playcard}")

    def illegal_card_error(self):
        print("Diese Karte kann zu diesem Zeitpunkt nicht legal gespielt werden!")

    def who_has_dealt(self):
        corr = False
        while corr == False:
            who_dealt = input("Wer hat die Karten ausgegeben?(Spieler/Gegner) ")
            if who_dealt == 'Spieler' or who_dealt == 'Gegner':
                corr = True
            else:
                pass
            
        return who_dealt
    
    def starter_message(self, dealer):
        if dealer == 'Gegner':
            print("Sie fangen an!")
        elif dealer == 'Spieler':
            print("Der Gegner fängt an!")
        
    def show_trumpf(self, trumpf):
        print(f"Die Trumpfkarte: {trumpf}")
    
    def show_trumpf_farbe(self, trumpf_farbe):
        print(f"Die Trumpffarbe: {trumpf_farbe}")
    
    def show_battleground(self, battleground):
        print()
        print(f"Liegende Karten: {', '.join(str(card) for card in battleground)}")
    
    def show_player_hand(self, hand):
        print()
        print(f"Ihre Spielkarten: {', '.join(str(card) for card in hand)}")

    def show_opponent_hand(self, hand):
        print(f"Gegner Spielkarten: {', '.join(str(card) for card in hand)}")

    def show_playable_cards(self, playable):
        print()
        print(f"Spielbare Karten: {', '.join(str(card) for card in playable)}")

    def break_between_games(self):
        print()
        print('---------------------------------------------------------------------------')
        print()

    def scoring_prints(self, who_won, player_points, opponent_points):
        print()
        print(f"Der {who_won} hat dieses Blatt gewonnen!")
        print("Der Punktestand:")
        print()
        print(f"Spieler: {player_points}")
        print(f"Gegner: {opponent_points}")
        print()