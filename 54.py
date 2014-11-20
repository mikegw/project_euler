#'High Card' =
#'One Pair' =
#'Two Pairs' =
#'Three of a Kind' =
#'Straight' =
#'Flush' =
#'Full House' =
#'Four of a Kind' =
#'Straight Flush' =
#'Royal Flush' =

hands_list = open("/home/mike/Python/Euler/poker.txt",'r')

ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
suits = ['C','D','H','S']


class Card:
    def __init__(self,c):
        self.rank = c[:-1]
        self.suit = c[-1]

    def __str__(self):
        return self.rank + self.suit

    def __lt__(self,other):
        return ranks.index(self.rank) < ranks.index(other.rank)

    def __le__(self,other):
        return ranks.index(self.rank) <= ranks.index(other.rank)

    def __gt__(self,other):
        return ranks.index(self.rank) > ranks.index(other.rank)

    def __ge__(self,other):
        return ranks.index(self.rank) >= ranks.index(other.rank)

    def __eq__(self,other):
        return ranks.index(self.rank) == ranks.index(other.rank)

    def __ne__(self,other):
        return ranks.index(self.rank) != ranks.index(other.rank)

    def __sub__(self,other):
        return ranks.index(self.rank) - ranks.index(other.rank)

class Hand:
    def __init__(self,hand_string):
        self.hand = []
        self.ranks = []
        j = 0
        for i in range(5):
            #print(hand_string[3*i:3*i+2])
            if hand_string[3*i:3*i+2]=='10':
                self.hand.append(Card(hand_string[3*i+j:3*i+j+3]))
                j += 1
            else:
                self.hand.append(Card(hand_string[3*i+j:3*i+2+j]))
        for c in self.hand:
            self.ranks.append(c.rank)
        #print(str([str(c) for c in self.hand]))
        self.string = sum([len(str(c)) + 1 for c in self.hand])
        self.sort()
        self.count()
        self.evaluate()
        #print(str([str(h) for h in self.hand]), self.ranks)

    def __str__(self):
        return str([str(c) for c in self.hand])

    def __getitem__(self,i):
        return self.hand[i]

    def sort(self):
        newhand = [self.hand[0]]
        l = 1
        for c in self.hand[1:]:
            for i in range(l):
                if self.ranks.count(c.rank) > self.ranks.count(newhand[i].rank):
                    newhand.insert(i,c)
                    break   
                elif self.ranks.count(c.rank) == self.ranks.count(newhand[i].rank) and c > newhand[i]:
                    newhand.insert(i,c)
                    break
            else:
                newhand.append(c)
            l += 1
        self.hand = newhand

    def count(self):
        self.no_of_rank = {}
        for r in ranks:
            self.no_of_rank[r] = self.ranks.count(r)
        #print(self.no_of_rank)

    def is_pair(self):
        for r in ranks:
            if self.no_of_rank[r] > 1:
                return True
        else:
            return False

    def is_two_pair(self):
        pairs = 0
        for r in ranks:
            if self.no_of_rank[r] > 1:
                pairs += 1
        if pairs == 2:
            return True
        else:
            return False

    def is_triple(self):
        for r in ranks:
            if self.no_of_rank[r] > 2:
                return True
        else:
            return False

    def is_four_of_a_kind(self):
        for r in ranks:
            if self.no_of_rank[r] > 3:
                return True
        else:
            return False

    def is_flush(self):
        for i in range(len(self.hand)-1):
            if self.hand[i+1].suit != self.hand[i].suit:
                return False
        else:
            print([str(c) for c in self.hand])
            return True

    def is_straight(self):
        for i in range(len(self.ranks)-1):
            if ranks.index(self.hand[i+1].rank) != ranks.index(self.hand[i].rank)-1:
                return False
        else:
            print([str(c) for c in self.hand])
            return True

    def is_straight_flush(self):
        return (self.is_straight() and self.is_flush())

    def is_full_house(self):
        pairs = 0
        triple = 0
        for r in ranks:
            if self.no_of_rank[r] > 2:
                triple += 1
            elif self.no_of_rank[r] > 1:
                pairs += 1
        if pairs == triple == 1:
            return True
        else:
            return False


    def evaluate(self):
        self.value = 0
        if self.is_pair():
            self.value = 1
        if self.is_two_pair():
            self.value = 2
        if self.is_triple():
            self.value = 3
        if self.is_straight():
            self.value = 4
        if self.is_flush():
            self.value = 5
        if self.is_full_house():
            self.value = 6
        if self.is_four_of_a_kind():
            self.value = 7
        if self.is_straight_flush():
            self.value = 8

    def __gt__(self,other):
        if self.value > other.value:
            return True
        elif self.value < other.value:
            return False
        else:
            for i in range(len(self.hand)):
                if self.hand[i] > other.hand[i]:
                    return True
                elif self.hand[i] < other.hand[i]:
                    return False
            
        

#hand2 = Hand('7H 7D 10S 6D 6S')
#print(str([str(c) for c in hand2]))

hand1_score = 0

for line in hands_list:
    hand1 = Hand(line)
    hand2 = Hand(line[hand1.string:])
    hand1_wins = (hand1 > hand2)
    #print(str([str(c) for c in hand1]),str([str(c) for c in hand2]), hand1.value, hand2.value, hand1_wins)
    if hand1 > hand2:
        hand1_score +=1

print(hand1_score)   



