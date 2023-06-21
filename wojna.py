import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']


def create_deck() -> list:
    deck = []
    for rank in ranks:
        for suit in suits:
            card = (rank, suit)
            deck.append(card)
    random.shuffle(deck)
    return deck


def distribute_cards(player1_deck: list, player2_deck: list, deck: list):
    for i, card in enumerate(deck):
        if i % 2 == 0:
            player1_deck.append(card)
        else:
            player2_deck.append(card)
    return player1_deck, player2_deck


def compare_cards(player1_card: list, player2_card: list) -> str:
    if ranks.index(player1_card[0]) > ranks.index(player2_card[0]):
        return "player_1"
    elif ranks.index(player1_card[0]) < ranks.index(player2_card[0]):
        return "player_2"
    else:
        return "war"


def main():
    player1_deck = []
    player2_deck = []
    deck = create_deck()
    distribute_cards(player1_deck, player2_deck, deck)

    while player1_deck and player2_deck:
        player1_card = player1_deck.pop(0)
        print("Player 1 card:", player1_card)
        player2_card = player2_deck.pop(0)
        print("Player 2 card:", player2_card)

        result = compare_cards(player1_card, player2_card)
        if result == "player_1":
            player1_deck.extend([player1_card, player2_card])
            print("Player 1 wins")
        elif result == "player_2":
            player2_deck.extend([player1_card, player2_card])
            print("Player 2 wins")
        elif result == "war":
            table = [player1_card, player2_card]
            print("War")
            while True:
                if len(player1_deck) < 4:
                        print("Player 2 wins the game!")
                        break
                elif len(player2_deck) < 4:
                        print("Player 1 wins the game!")
                        break
                else:
                    for i in range(2):
                        player1_card = player1_deck.pop(0)
                        print("Player 1 card:", player1_card)
                        player2_card = player2_deck.pop(0)
                        print("Player 2 card:", player2_card)
                        table.extend([player1_card, player2_card])

                    result = compare_cards(player1_card, player2_card)
                    if result == "war":
                        print("Also war")
                    elif result == "player_1":
                        player1_deck.extend(table)
                        print("Player 1 wins")
                        break
                    else:
                        player2_deck.extend(table)
                        print("Player 2 wins")
                        break


    if len(player1_deck) == 0:
        print("Player 2 wins the game!")
    elif len(player2_deck) == 0:
        print("Player 1 wins the game!")


main()
