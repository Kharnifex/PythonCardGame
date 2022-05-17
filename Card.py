class Card:

    def __init__(self, owner, attack, heal, shield, draw, special=0, status=0):
        self.owner=owner
        self.heal = heal
        self.shield = shield
        self.draw = draw
        self.attack = attack
        self.special = special #TODO: decide this
        self.status=status #status: 0 = in deck, 1 = in hand, 2 = in graveyard