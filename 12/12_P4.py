class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'
    def getScore(self):
        if self.value == 'A':
            return 1
        elif self.value in ['J', 'Q', 'K']:
            return 10
        else:
            return int(self.value)
    def sum(self, other):
        return (self.getScore() + other.getScore())%10
    def __lt__(self, rhs):
        card_values = {}
        i = 0
        for e in [str(e) for e in range(3,11)] + ['J', 'Q', 'K', 'A', '2']:
            card_values[e] = i
            i += 1
        l = card_values[self.value]; r = card_values[rhs.value];
        if  l == r:
            return self.suit < rhs.suit
        else:
            return l < r

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])