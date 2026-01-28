# A short Guide to this Schnapsen Simulator


## 1. Rules

The rules implemented in this Schnapsen Simulator mirror the Rules one has to adhere to when playing Schnapsen in the pub with friends. This means:

 - There are two phases of play. Which phase of play you are in depends on if there are any cards left to draw and if either the opponent or the player has closed the deck.  

 - Rules during the whole game:
    - At the start, whoever shuffled the cards and dealt them out is the second to play.
    - In any other round, the winner of the previous round plays first
    - Ass = 11, Zehn = 10, König = 4, Dame = 3, Bube = 2
    - The winner of a round wins the value of both cards combined (eg. König + Ass = 15)
    - König and Dame of the same suit are a pair, if it is called, it is worth 20 points
    - A pair of the trumpf suit is worth 40 Points
    - Points won through declaring a pair are only added to the players tally once they have more than 0 points
 
 - Rules with open deck:
    - The player playing out is able to play any card in their hand
    - The player playing out can switch the Trumpf Bube for the card that is currently signaling the Trumpf
        - Exception: This is only possible as long as there are more than 2 cards left in the deck
    - The player playing out may declare a pair, must then play either König or Dame of this pair
    - The player playing out may close the deck("Zudrehen")

    - The player answering can play any card they have on their hand
- Rules with closed deck:
    - The player playing out is still able to play any card in their hand, can also still declare a pair
    - He cannot close the deck or switch trumpf anymore

    - The player answering has to answer in suit, if they have a card of the same suit as the card played (Farbenzwang)
    - If the player has no card of the same suit, they must play to win, if they are able to (Stichzwang)
    - If the player has no card of the same suit and can not win, they are free to play any card on their hand

- How to win a Bummerl:
    - A player can win 1 point if they are the first to get over 66 points, or if no player has equal to or more than 66 point, if they win the last card
    - A player can win 2 points if they get over 66 points and the opponent has less than 33 points
    - A player can win 3 points if they get over 66 points and the opponent has not won a single point

## 2. How to play

This Schnapsen Simulator is played in the Python Terminal, so you control it via input.  
While most questions for input tell you which answers are expected, the choice of which card to play should be entered as "Farbe Rang", so for example "Herz König", "Karo Ass", "Pik Zehn", "Kreuz Dame" or "Herz Bube".  
Proper grammar, especially Capitalization is important. Some inputs will ask you again if the answer is not properly written as expected, and for "Ja"/"Nein" questions, they often count everything that is not "Ja" as "Nein".  
  
Have fun playing!
