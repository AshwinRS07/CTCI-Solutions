# Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would
# subclass the data structures to implement blackjack.

# Objects: Deck, Card, Hand, Card_Suite, Card_Rank, Player, Dealer

# Relationships: Deck inherits Card, Card inherits/contains Card_Rank and Card_Suite. Deck is a static class. Card has flags to check if drawn or not. Another flag if it is an ace or not.
#                Player inherits Hand. Hand holds Card objects. Hand has current_sum of cards. Player has methods Draw_Card and Stand to proceed.
#                Dealer inherits player. Dealer simply follows rules as they cannot make many choices.
#                For Ace cards, we can have conditions such as if (Ace==11 and Hand_Sum>21), (Ace==11 and Hand_Sum<=21), use some decision strategy for ambiguous scenarios.

from enum import Enum
import random


class SUIT(Enum):
    HEART, SPADE, CLUB, DIAMOND = 1, 2, 3, 4

class Card:
    def __init__(self, suit, rank):
        self.card_suit = suit
        self.card_rank = rank
    
    def get_suite(self):
        return self.card_suite

    def get_rank(self):
        return self.card_rank

class BlackJackCard(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)
        self.game_value = self.card_rank if self.card_rank < 10 else 10
    
    def get_game_value(self):
        return self.game_value


class Deck(Card):
    def __init__(self):
        self.__cards = set()
        for value in range(14):
            for suit in SUIT:
                self.cards.add(BlackJackCard(suit, value))
    
    def get_cards(self):
        return self.__cards
    
    def shuffle(self):
        card_count = self.__cards.size()
        for i in range(0, card_count):
            j = random.randrange(0,card_count-i-1,1)
            self.__cards[i], self.__cards[j] = self.__cards[j], self.__cards[i]

    def deal_card(self):
        if self.__cards.size() == 0:
            return 'No Cards Left'
        return self.__cards.remove(0)


class Hand:
    def __init__(self, card1: Card, card2: Card):
        self.__cards = [card1, card2]
    
    def get_scores(self):
        totals = [0]

        for card in self.__cards:
            new_totals = []
            for score in totals:
                new_totals.add(card.get_rank() + score)
                if card.get_rank() == 1:
                    new_totals.add(11 + score)
                total = new_totals
        return totals
    
    def add_card(self, card: Card):
        self.__cards.add(card)
    
    def get_final_score(self):
        scores = self.get_scores()
        best = 0
        for score in scores:
            if score <= 21 and score > best:
                best = score
        return best

class Player():
    def __init__(self):
        self.bet = 0
        self.total_cash = 0

class Dealer():
    def __init__(self):
        pass


class Game:
    def __init__(self, player, dealer):
        self._player = player
        self._dealer = dealer
    
    def action(self, action, hand):
        actions = {
            'hit': self.hit(hand),
            'stand': self.stand()
        }
        actions.get(action, 'Invalid Move')
    
    def hit(self, hand):
        self.__hand.add_card(self.Deck.deal_card())

    def stand(self):
        dealer_score = self._dealer.get_scores()
        player_score = self._player.get_total_score()
        hands = self._player.get_hands()
        for hand in hands:
            best_score = hand.resolve_score()
            if player_score == dealer_score:
                None
            elif player_score == 21:
                None
            elif player_score > dealer_score:
                None
            else:
                None


# Incomplete
