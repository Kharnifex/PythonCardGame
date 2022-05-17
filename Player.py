class Player:
    maxHitpoints = 10
    currHitpoints = 10
    currShield = 0

    def __init__(self):
        self.graveyardDeck = []  # leave as is
        self.deck = []  # TODO: initialize deck
        self.hand = []  # TODO: draw 3 cards from deck

    def takeDamage(self, amount):
        if amount > 0:
            if self.currShield > 0:
                self.currShield -= 1
            else:
                self.currHitpoints -= 1
            if self.currHitpoints == 0:
                self.die()
            self.takeDamage(amount - 1)
        elif amount == 0:
            return
        else:
            print("how the fuck do you catch exceptions in python also for some reason"
                  "the game wants you to take negative damage so thats great i love coding")

    def getShield(self, amount):
        self.currShield += amount
        return

    def loseShield(self):
        self.currShield = 0
        return

    def heal(self, amount):
        self.currHitpoints += amount

    def die(self):
        # idk just die lol
        return
