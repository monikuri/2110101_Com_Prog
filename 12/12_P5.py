class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'
    def next1(self):
        suit_map = {'club': 'diamond', 'diamond': 'heart',
                    'heart': 'spade','spade': 'club'}
        value_map = {'2': '3', '3': '4', '4': '5', '5': '6', '6':'7',
                     '7': '8', '8': '9', '9': '10', '10': 'J', 'J': 'Q',
                     'Q': 'K', 'K': 'A', 'A': '2'}
        new_suit = suit_map[self.suit]
        new_value = value_map[self.value] if self.suit == 'spade' else self.value
        return Card(new_value, new_suit)
    def next2(self):
        new_obj = self.next1()
        self.value = new_obj.value
        self.suit = new_obj.suit
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])