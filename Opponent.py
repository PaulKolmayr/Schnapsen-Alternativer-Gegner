"""
Module contains Opponents Moves:
 - Opponents first draw: Opponent draws 5 cards
 - Opponents normal draw: Opponent draws a card after move
 - Opponent switches trumpf: Opponent will always switch trumpf
   if he can since I frankly dont see any sense in not doing it
 - Opponent plays first: Opponent will check if he is able to play
   a pair, if not he will for now (*in work) play the first card in his hand
 - Opponent plays second: Opponent will play to win or lose with the lowest card
   he can play, also will not use a trumpf unless he cant win with another card
"""

from Card_Properties import Deck as Cards

class Opponent:

    def __init__(self, cards):
        """
         - Deck imported so that there is continuity with which cards are in play and in the deck etc. during the game, 
           also deck method is needed for the draw
         - Hand initialized because it needs to be accessible and store the values that are only changed by the methods
        """
        self._cards = cards
        self._hand = []
    
    @property
    def show_hand(self):
        print(f"Gegner Spielkarten: {', '.join(str(card) for card in self._hand)}")
    

    def first_draw(self):
        """
        Opponent draws 5 Cards that are popped from the deck, these 5 cards are then only available in Opponents Deck
        Only used at start of the game
        """
        self._hand = [self._cards.draw() for _ in range(5)]

    
    def normal_draw(self, trumpf):
        """
        Simulates what happens in a real life game of Schnapsen, Opponent draws from the deck until there is only the
        trumpf card, then he draws that one
        No precaution for when both are empty because this is covered in the SingleGame class
        """
        if len(self._cards._deck) > 0:
            self._hand.append(self._cards.draw())
        else:
            self._hand.append(trumpf)
    

    def switches_trumpf(self, trumpf):
        """
        Opponent switches his trumpf bube for whatever trumpf card was drawn 
        All Cards (so one) that fit the needed criteria get sorted into their own list, if this list exists
        the card gets removed from opponents hand and is passed on to be the next trumpf while the old trumpf
        is appended to the opponents hand
        """
        op_switches = [card for card in self._hand if card.rank.name == 'Bube' and card.suit == trumpf.suit]
        if op_switches:
            self._hand.append(trumpf)
            self._hand.remove(op_switches[0])
            return op_switches[0]
        else:
            return trumpf


    def plays_first(self, op_points, trumpf):
        """
        Pair(s) get found by finding kings and queens, then their suits are compared and if a king and queen are of
        the same suit, they get appended to pairs as a pair.
        If opponent has the trumpf pair, he always plays that since it is worth 40 points. With normal pairs, it is too risky
        if he doesnt already have points on the board so he waits and plays other cards
        Otherwise, Opponent is free to play every card since he starts, so another algorithm comes in.
        Aggression Logic: Opponent is programmed as to, when he doesnt play a pair look at his points + the points he can get
        safely (points from trumpfcards). If they add up to over 66, he goes aggressive and plays high trumpf cards, if not
        he saves the important cards and plays low non trumpf cards to draw the player out
        """
        self._playable = []
        self._plays_pair = False
        
        #can play a pair
        dames = []
        kings = []
        pairs = []
        trumpf_pair = []

        for dame in self._hand:
            if dame.rank.name == 'Dame':
                dames.append(dame)
        for king in self._hand:
            if king.rank.name == 'König':
                kings.append(king)
        
        for card_a in dames:
            for card_b in kings:
                if card_a.suit.name == card_b.suit.name:
                    if card_a.suit.name == trumpf.suit.name:
                        trumpf_pair.append(card_a)
                        trumpf_pair.append(card_b)
                    else:
                        pairs.append(card_a)
                        pairs.append(card_b)
        
        plays_pair = False

        if len(trumpf_pair) > 0:
            self._playable = [card for card in self._hand if card in trumpf_pair]
            plays_pair = True
        elif len(pairs) > 0 and len(trumpf_pair) == 0:
            if op_points > 0:
                self._playable = [card for card in self._hand if card in pairs]
                plays_pair = True
            else:
                self._playable = [card for card in self._hand if card not in pairs]
        else:
            self._playable = [card for card in self._hand]
        
        print()
        if plays_pair == True:
            self._playable.sort(key=lambda card: card.rank.value)
            print(f"Der Gegner spielt das {self._playable[0].suit.name}-Paar aus!")
            self._plays_pair = True
            card = self._playable[0]
        else:
            trumpf_cards = []
            nontrumpf_cards = []
            for cards in self._playable:
                if cards.suit.name == trumpf.suit.name:
                    trumpf_cards.append(cards)
                else:
                    nontrumpf_cards.append(cards)
            
            aggressive_play = op_points
            for trumpfs in trumpf_cards:
                aggressive_play += trumpfs.rank.value
            
            trumpf_cards.sort(key=lambda card: card.rank.value, reverse=True)
            nontrumpf_cards.sort(key=lambda card: card.rank.value)
            
            if aggressive_play > 66:
                if len(trumpf_cards) > 0:
                    card = trumpf_cards[0]
                else:
                    card = nontrumpf_cards[0]
            else:
                if len(nontrumpf_cards) > 0:
                    card = nontrumpf_cards[0]
                else:
                    card = trumpf_cards[-1]
        
        self._hand.remove(card)
        return card


    def dynamic_value(self, trumpf, played_cards):
        """
        First Factor in how Opponent should play, should check how "out of position" a card is, therefore how much better
        it is compared to original value
        Can be used to exploit missmatches, for example if a bube is the last card of his suit, can be used to draw trumpf
        or get an easy win
        """
        #base point system
        card_missmatch = {missmatch: 0 for missmatch in self._hand}
        for card in self._hand:
            if card.rank.name == 'Ass':
                card_value = 5
            elif card.rank.name == 'Zehn':
                card_value = 4
            elif card.rank.name == 'König':
                card_value = 3
            elif card.rank.name == 'Dame':
                card_value = 2
            elif card.rank.name == 'Bube':
                card_value = 1
            
            #Opponent is simulated to be able to remember any card that has been played
            #If Opponent knows a card to be played, he can eliminate i
            if card.suit.name == trumpf.suit.name:
                card_value += 5
            
            #Opponent is simulated to be able to remember any card that has been played
            #If Opponent knows a card to be played, he can eliminate it from his thinking, if this card
            #is higher than his card, therefore his card is now worth more
            for done_card in played_cards:
                if done_card.suit.name == card.suit.name and done_card.rank.value > card.rank.value:
                    card_value += 1
                    card_missmatch[card] += 1
            
            for op_card in self._hand:
                if op_card.suit.name == card.suit.name and op_card.rank.value > card.rank.value:
                    card_value += 1
                    card_missmatch[card] += 1
        
        return card_missmatch
    

    def risk_system_late_game(self, trumpf, deck, playerhand):
        """
        One of two risk systems: This one will be more important the later in the game the players are
        Later in the Game, Opponent cant count on the Player holding certain cards because they are too valuable as much
        as early in the game
        """
        #Opponent is able to memorize every card that was played so he is able to know which cards havent been played yet
        #With this logic, it is justifiable to let him know the unknown cards
        unknown_cards = []
        for cards in deck:
            unknown_cards.append(cards)
        for handcards in playerhand:
            unknown_cards.append(handcards)
        
        #Opponent checks his unknown cards for cards that would lose against his card
        risk_values = {}
        for op_card in self._hand:
            worse_cards = []
            if op_card.suit.name == trumpf.suit.name:
                for item in unknown_cards:
                    if item.suit.name != trumpf.suit.name:
                        worse_cards.append(item)
                    elif item.suit.name == trumpf.suit.name and item.rank.value < op_card.rank.value:
                        worse_cards.append(item)
            elif op_card.suit.name != trumpf.suit.name:
                for item in unknown_cards:
                    if item.suit.name != trumpf.suit.name and item.suit.name != op_card.suit.name:
                        worse_cards.append(item)
                    elif item.suit.name == op_card.suit.name and item.rank.value < op_card.rank.value:
                        worse_cards.append(item)
        
            #He assesses the risk level of playing each card by dividing all better cards by all unknown cards
            #and multiplying this with the points he stands to lose if he loses the card
            if len(unknown_cards) > 0:
                risk_level = (len(worse_cards)/len(unknown_cards))
                risk_values[op_card] = risk_level
            else:
                risk_level = (len(worse_cards)/1)
                risk_values[op_card] = risk_level
        
        return risk_values
    

    def risk_system_early_game(self, trumpf, deck, playerhand):
        """
        One of two risk systems: Earlier in the game, a player can reasonably expect that the other player will not use
        a trumpf to win against king or lower, so the risk system has to reflect that.
        """
        #Opponent is able to memorize every card that was played so he is able to know which cards havent been played yet
        #With this logic, it is justifiable to let him know the unknown cards
        unknown_cards = []
        unknown_cards_no_trumpf = []
        for cards in deck:
            if cards.suit.name == trumpf.suit.name:
                unknown_cards.append(cards)
            else:
                unknown_cards.append(cards)
                unknown_cards_no_trumpf.append(cards)
        for handcards in playerhand:
            if handcards.suit.name == trumpf.suit.name:
                unknown_cards.append(handcards)
            else:
                unknown_cards.append(handcards)
                unknown_cards_no_trumpf.append(handcards)
        
        #Opponent checks his unknown cards for cards that would lose against his card
        risk_values = {}
        for op_card in self._hand:
            worse_cards = []
            if op_card.suit.name == trumpf.suit.name:
                for item in unknown_cards:
                    if item.suit.name != trumpf.suit.name:
                        worse_cards.append(item)
                    elif item.rank.value < op_card.rank.value:
                        worse_cards.append(item)

            elif op_card.suit.name != trumpf.suit.name:
                if op_card.rank.value > 5:
                    for item in unknown_cards:
                        if item.suit.name != trumpf.suit.name and item.suit.name != op_card.suit.name:
                            worse_cards.append(item)
                        elif item.suit.name == op_card.suit.name and item.rank.value < op_card.rank.value:
                            worse_cards.append(item)
                else:
                    for item in unknown_cards_no_trumpf:
                        if item.suit.name != trumpf.suit.name and item.suit.name != op_card.suit.name:
                            worse_cards.append(item)
                        elif item.suit.name == op_card.suit.name and item.rank.value < op_card.rank.value:
                            worse_cards.append(item)

            if op_card.suit.name != trumpf.suit.name and op_card.rank.value < 5:
                if len(unknown_cards_no_trumpf) > 0:
                    risk_level = (len(worse_cards)/len(unknown_cards_no_trumpf))
                    risk_values[op_card] = risk_level
                else:
                    risk_level = (len(worse_cards)/1)
                    risk_values[op_card] = risk_level
            else:
                if len(unknown_cards) > 0:
                    risk_level = (len(worse_cards)/len(unknown_cards))
                    risk_values[op_card] = risk_level
                else:
                    risk_level = (len(worse_cards)/1)
                    risk_values[op_card] = risk_level

        return risk_values


    def part_of_pair(self, trumpf):
        pair_part = {card: 0 for card in self._hand}
        for card_a in self._hand:
            for card_b in self._hand:
                if card_a.rank.name == 'König': 
                    if card_b.rank.name == 'Dame' and card_a.suit.name == card_b.suit.name:
                        if card_a.suit.name == trumpf.suit.name:
                            pair_part[card_a] = 2
                            pair_part[card_b] = 2
                        elif card_a.suit.name != trumpf.suit.name:
                            pair_part[card_a] = 1
                            pair_part[card_b] = 1            

        return pair_part


    def pair_possibility(self, trumpf, played_cards):
        pair_possibility = {card: 0 for card in self._hand}

        for king in self._hand:
            if king.rank.name == 'König':
                poss_score = 0
                for pos_dame in played_cards:
                    if pos_dame.rank.name == 'Dame' and pos_dame.suit.name == king.suit.name:
                        poss_score += 1
                for act_dame in self._hand:
                    if act_dame.rank.name == 'Dame' and act_dame.suit.name == king.suit.name:
                        poss_score += 1
                if poss_score == 0:
                    if king.suit.name == trumpf.suit.name:
                        pair_possibility[king] += 2
                    else:
                        pair_possibility[king] += 1
            
        for dame in self._hand:
            if dame.rank.name == 'Dame':
                poss_score = 0
                for pos_king in played_cards:
                    if pos_king.rank.name == 'König' and pos_king.suit.name == dame.suit.name:
                        poss_score += 1
                for act_king in self._hand:
                    if act_king.rank.name == 'König' and act_king.suit.name == dame.suit.name:
                        poss_score += 1
                if poss_score == 0:
                    if dame.suit.name == trumpf.suit.name:
                        pair_possibility[dame] += 2
                    else:
                        pair_possibility[dame] += 1
                    
        return pair_possibility
    

    def colour_strength(self, played_cards):
        """
        Under construction, need to consult with my expert
        """
        pass
    
    
    def which_play(self, roundcounter):
        """
        coming soon
        """
        importance = roundcounter/10

        factors =  {'early_risk_factor': 0.8*(importance), 
                    'late_risk_factor': 1.2*(1-(importance)), 
                    'dynamic_rating_factor': 0.4 + 0.5*(1-(importance)),
                    'pair_possibility_factor': 0.5*(importance),
                    'pair_on_hand_factor': 0.5 + (importance)}

        return factors


    def expected_points(self, trumpf, deck, playerhand):
        """
        coming soon
        """
        pass
        

    def play_first_new(self, op_points, trumpf, played_cards, deck, player_cards, roundcounter):
        """
        Opponen
        """
        self._plays_pair = False
        #Opponent assesses the risk of losing each card he is able to play
        risk_values_early = self.risk_system_early_game(trumpf, deck, player_cards)
        risk_values_late = self.risk_system_late_game(trumpf, deck, player_cards)
        card_strength = self.dynamic_value(trumpf, played_cards)
        pair_part = self.part_of_pair(trumpf)
        pair_possibility = self.pair_possibility(trumpf, played_cards)
        round_factor = self.which_play(roundcounter)

        playing_recommendation = {}
        for card in self._hand:
            score = (round_factor['early_risk_factor'] * risk_values_early[card]) + (round_factor['late_risk_factor'] * risk_values_late[card]) + (round_factor['dynamic_rating_factor'] * card_strength[card]) + (round_factor['pair_on_hand_factor'] * pair_part[card]) + (round_factor['pair_possibility_factor'] * pair_possibility[card])
            playing_recommendation[card] = score

        recommended_card = max(playing_recommendation, key=playing_recommendation.get)

        if recommended_card.rank.name == "König":
            for cards in self._hand:
                if cards.rank.name == "Dame" and cards.suit.name == recommended_card.suit.name:
                    print(f"Der Gegner spielt das {recommended_card.suit.name}-Paar aus!")
                    self._plays_pair = True
        
        print(playing_recommendation)
        self._hand.remove(recommended_card)
        return recommended_card


    def plays_second(self, zugedreht, playcard, trumpf):
        """
        If the deck is closed("zugedreht"), the opponent has to act under "Farbzwang", so he can only play the same
        suit, unless he doesnt have cards of the same suit as the players card
        If the deck is not closed, this does not apply.
        The cards that are legal to play then get sorted into the categories higher, lower and trumpf.
        If the opponent is able to win the card without playing a trumpf, he will play the lowest non-trumpf-card he
        can win with
        If he has to play a trumpf card to win, he will play the lowest trumpf card he can get the card with
        If no win is possible, he will play the lowest card he can dispose of as to not give more points than needed
        to the player.
        *Opponent methods regarding the card he plays are in active work, I very much intend on making the opponent smarter
        **Although it is nice that so far I am able to win against him
        """
        self._playable = []
        if zugedreht == False:
            self._playable = [card for card in self._hand]
        else:
            for cards in self._hand:
                if cards.suit.name == playcard.suit.name:
                    self._playable.append(cards)
            
            if len(self._playable) == 0:
                self._playable = [card for card in self._hand]
        
        #Opponent should take the card if he can, optimally with the lowest card possible
        #Trumpfs should also only be played if Opponent can't win otherwise
        higher_list = []
        trumpf_list = []
        lower_list = []
        for card in self._playable:
            if card.suit.name == playcard.suit.name:
                if card.rank.value > playcard.rank.value:
                    higher_list.append(card)
                else:
                    lower_list.append(card)
            else:
                if card.suit.name == trumpf.suit.name:
                    trumpf_list.append(card)
                else:
                    lower_list.append(card)
        
        higher_list.sort(key=lambda card: card.rank.value)
        lower_list.sort(key=lambda card: card.rank.value)
        trumpf_list.sort(key=lambda card: card.rank.value)

        if len(higher_list) == 0:
            if len(trumpf_list) == 0:
                op_card = lower_list[0]
            else:
                op_card = trumpf_list[0]
        else:
            op_card = higher_list[0]

        return op_card
