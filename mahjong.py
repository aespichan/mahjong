from collections import Counter

class Mahjong:
    @staticmethod
    def __bt(hand, n):
        if (n == 0):
            return True

        for num in hand:
            if hand[num] >= 3:
                # could be a set
                hand[num] -= 3
                if Mahjong.__bt(hand, n-3):
                    return True
                hand[num] += 3
            if (
                hand[num] >= 1 and 
                num+1 in hand and hand[num+1] >= 1 and
                num+2 in hand and hand[num+2] >= 1
            ):
                # could belong to a straight
                hand[num] -= 1
                hand[num+1] -= 1
                hand[num+2] -= 1
                if Mahjong.__bt(hand, n-3):
                    return True
                hand[num] += 1
                hand[num+1] += 1
                hand[num+2] += 1
            elif hand[num] >= 1: 
                # doesn't belong to set/straight, can't be a winning hand
                return False

        return False

    @staticmethod
    def is_winning_hand(hand):
        hand = [int(num) for num in hand.split(",")]
        hand = Counter(sorted(hand))

        for num in hand:
            if hand[num] >= 2:
                # could be a pair
                hand[num] -= 2
                if Mahjong.__bt(hand, 12):
                    return True
                hand[num] += 2
        return False

