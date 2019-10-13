from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        chands = Counter(hand)
        skey = sorted(chands.keys())
        while skey:
            s = skey[0]
            for x in range(W):
                if chands[x+s] <= 0:
                    return False
                chands[x+s] -= chands[x]
                if chands[x+s] == 0:
                    skey.remove(x+s)
            if 0 < len(skey) < W:
                return False
        return True
