# Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would
# subclass the data structures to implement blackjack.

# Objects: Deck, Card, Hand, Card_Suite, Card_Rank, Player, Dealer

# Relationships: Deck inherits Card, Card inherits/contains Card_Rank and Card_Suite. Deck is a static class. Card has flags to check if drawn or not. Another flag if it is an ace or not.
#                Player inherits Hand. Hand holds Card objects. Hand has current_sum of cards. Player has methods Draw_Card and Stand to proceed.
#                Dealer inherits player. Dealer simply follows rules as they cannot make many choices.
#                For Ace cards, we can have conditions such as if (Ace==11 and Hand_Sum>21), (Ace==11 and Hand_Sum<=21), use some decision strategy for ambiguous scenarios.