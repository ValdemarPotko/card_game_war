import random

class Card:
    suits = ("♡", "♢", "♧", "♤")
    values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    value_map = {v: i for i, v in enumerate(values, start=2)}

    def __init__(self, suit, value): 
        self.suit = suit
        self.value = value

    @classmethod
    def compare(cls, card1, card2):
        if cls.value_map[card1.value] > cls.value_map[card2.value]:
            return 1
        elif cls.value_map[card1.value] < cls.value_map[card2.value]:
            return -1
        else:
            return 0

    def __repr__(self):
        return f"{self.value}{self.suit}"

class Deck:
    @staticmethod
    def create_deck():
        return [Card(suit, value) for suit in Card.suits for value in Card.values]

    @staticmethod
    def shuffle_deck(deck):
        random.shuffle(deck)

    @staticmethod
    def split_deck(deck):
        mid_index = len(deck) // 2
        return deck[:mid_index], deck[mid_index:]

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []

    def receive_cards(self, cards):
        self.deck.extend(cards)

    def play_card(self):
        return self.deck.pop(0) if self.deck else None

class WarGame:
    def __init__(self):
        deck = Deck.create_deck()
        Deck.shuffle_deck(deck)
        self.player1 = Player(input("First player name: "))
        self.player2 = Player(input("Second player name: "))
        p1_deck, p2_deck = Deck.split_deck(deck)
        self.player1.receive_cards(p1_deck)
        self.player2.receive_cards(p2_deck)

    def make_turn(self):
        turn_cards = []
        player1_card = self.player1.play_card()
        player2_card = self.player2.play_card()
        if player1_card is None or player2_card is None:
            return

        turn_cards.extend([player1_card, player2_card])

        while True:
            result = Card.compare(player1_card, player2_card)
            if result != 0:
                winner = self.player1 if result == 1 else self.player2
                winner.receive_cards(turn_cards)
                break
            else:
                for _ in range(3):  # Each player places three cards face down
                    if self.player1.deck: turn_cards.append(self.player1.play_card())
                    if self.player2.deck: turn_cards.append(self.player2.play_card())
                
                player1_card = self.player1.play_card()  # Next card for the tiebreaker
                player2_card = self.player2.play_card()
                if player1_card is None or player2_card is None:
                    return
                turn_cards.extend([player1_card, player2_card])

    def play(self):
        while self.player1.deck and self.player2.deck:
            self.make_turn()
        
        if not self.player1.deck:
            print(f"{self.player2.name} wins the game!")
        else:
            print(f"{self.player1.name} wins the game!")

def main():
    game = WarGame()
    game.play()

if __name__ == "__main__":
    main()
