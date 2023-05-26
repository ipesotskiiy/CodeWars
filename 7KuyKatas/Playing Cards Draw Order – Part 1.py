def draw(deck):
    drawn_cards = []
    while deck:
        drawn_cards.append(deck.pop(0))
        if deck:
            deck.append(deck.pop(0))
    return drawn_cards

