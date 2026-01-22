"""
Since Schnapsen is, similar to tennis is comprised of games that build bigger games, this module
controls the overarching flow of the game
"""

from Single_Game import SingleGame as Game

class GameMain:

    def __init__(self):
        self._player_points = 0
        self._opponent_points = 0

    def bummerl(self):
        """
        Method prints a Welcome Message
        Method calls the single game while no player has won 7 points towards his 'Bummerl'.
        When a Player has won 7 Points, per the rules of Schnapsen he has won the 'Bummerl' and the game ends.
        Method lets you know if you have won or lost
        """
        print()
        print("-------------------------------------------------------")
        print("Herzlich Willkommen zum Schnapsen Simulator 2026!!")
        print("Wir freuen uns dass Sie ein Bummerl mit uns spielen!")
        print("-------------------------------------------------------")

        intro_rules = input("Wollen Sie bevor Sie starten die Regeln wissen?(Ja/Nein) ")
        if intro_rules == 'Ja':
            print()
            print("---------------------------------------------------------------------------------------------")
            print('REGELWERK')
            print()
            print("Im Schnapsen geht es darum, Bummerl zu gewinnen")
            print("Ein Bummerl besteht aus 7 gewonnenen Games, die jeweils auf 66 Punkte gehen")
            print()
            print("Ein Game startet, wenn ein Spieler ausgibt, der andere spielt dann aus")
            print("Wenn Sie am Zug sind, können Sie:")
            print(" - Trumpf tauschen: Möglich, wenn Sie den Trumpf Buben auf der Hand haben")
            print(" - Zudrehen: Sie können immer zudrehen, wenn Sie am Spielzug sind")
            print("    - Dadurch kann kein Spieler mehr Karten heben, ist also gut wenn Sie denken, dass sie")
            print("      mit Ihren Handkarten über 66 kommen und dem Gegner keine Chance lassen wollen.")
            print(" - Ein Pärchen spielen: Möglich, wenn Sie sowohl König als auch Dame auf der Hand haben")
            print("    - Ein normales Pärchen: 20 Punkte")
            print("    - Ein Trumpf-Pärchen: 40 Punkte")
            print(" - Eine Karte spielen: Trumpf sticht alle Farben, wenn kein Trumpf im Spiel liegt,")
            print("   sticht die ausgespielte Farbe jegliche Karten anderer Farben")
            print(" - Die Karten der Stärke nach: Ass - Zehn - König - Dame - Bube")
            print("Sobald zugedreht wurde oder das Deck leer ist, gilt Farbenzwang.")
            print("Viel Glück!")
            print("---------------------------------------------------------------------------------------------")

        while self._player_points < 7 and self._opponent_points < 7:

            lets_play = Game()
            lets_play.game()

            self._player_points += lets_play._wins[0]
            self._opponent_points += lets_play._wins[1]
            
            print("-------------------------------------------------------")
            print("Zwischenstand:")
            print(f"Punkte Spieler: {self._player_points}")
            print(f"Punkte Gegner: {self._opponent_points}")
            print("-------------------------------------------------------")

        if self._player_points >= 7:
            print()
            print(f"Gratuliere!")
            print(f"Sie haben dieses Bummerl gewonnen!")

        elif self._opponent_points >= 7:
            print()
            print("Schade!")
            print("Diese Runde hat leider der Computer gewonnen!")


