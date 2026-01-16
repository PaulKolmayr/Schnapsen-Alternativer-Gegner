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


