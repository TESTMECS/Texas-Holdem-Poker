import operator
#################################
#handles solving of poker hands
class Poker(object):
    def __init__(self, Player1, Player2, Player3, Dealer) -> None:
        self.Player1 = Player1
        self.Player2 = Player2
        self.Player3 = Player3
        self.Dealer = Dealer

    def get_most_suits(self, hand):
        suits = {0:0, 1:0, 2:0, 3:0}
        for card in hand:
            suits[card.suit] += 1
        return max(suits, key=suits.get)

    def get_most_rank(self, hand):
        ranks = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
        for card in hand:
            ranks[card.value] += 1
        return max(ranks, key=ranks.get)

    def get_score(self, hand):
        card_Count = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
        for card in hand:
            card_Count[card.value] += 1
        unique_cards = 0
        for rankcount in card_Count.values():
            if rankcount > 0:
                unique_cards += 1
        straight = self.is_straight(hand)
        flush = self.is_flush(hand)
        points = 0
        if straight and flush:
            points = max(points, 9)  # straight flush
        elif flush and not straight:
            points = max(points, 6)  # flush
        elif not flush and not straight:
            points = max(points, 5)  # straight
        elif unique_cards == 2:
            if max(card_Count.values()) == 4:
                points = 8  # four of a kind (2 uniques and 4 are the same)
            elif max(card_Count.values()) == 3:
                points = 7  # full house (2 unique and 3 are the same)
        elif unique_cards == 3:
            if max(card_Count.values()) == 3:
                points = 4  # three of a kind (3 unique and 3 are the same)
            elif max(card_Count.values()) == 2:
                points = 3  # two pair (3 uniques and 2 are the same)
        elif unique_cards == 4:
            if max(card_Count.values()) == 2:
                points = 2  # one pair (4 uniques and 2 are the same)
        elif unique_cards == 5:
            points = 1  # high card

        
        sorted_cardCount = sorted(card_Count.items(), key=operator.itemgetter(1, 0), reverse=True)
        for keyval in sorted_cardCount:
            if keyval[1] != 0:
                points = int(str(points) + (keyval[1] * str(keyval[0]).zfill(2)))

        return points

    def is_straight(self, hand):
        values = []
        for card in hand:
            values.append(card.value)
        values.sort()
        for i in range(0, 6):
            if values[i] + 1 != values[i + 1]:
                return False
        return True

    def is_flush(self, hand):
        suit = hand[0].suit
        for card in hand:
            if card.suit != suit:
                return False
        return True
