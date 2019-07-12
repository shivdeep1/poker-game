def straight(ranks):
    if len(set(ranks)) == 5 and (max(ranks)-min(ranks) == 4):
        return True
    return False

def flush(suits):
    if len(set(suits)) == 1:
        return True
    return False

def kind(n,ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r
        return None

def two_pair(ranks):
    hicard = kind(2,ranks)
    locard = kind(2, tuple(reversed(ranks)))
    if hicard != locard:
        return(hicard,locard)
    return None

if __name__ == "__main__":
    assert(straight([6,5,4,3,2]) == True)                         #assert is used for unit testing
    assert(straight([6,5,5,3,2]) == False)

def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks

def card_suits(hand):
    return [s for r,s in hand]

def poker(hands):
    return max(hands , key=hand_rank)

def hand_rank(hand):
    ranks = card_ranks(hand)
    suits = card_suits(hand)

    if straight(ranks) and flush(suits):
        return(8, max(ranks))   #priority given to straight flush =8
    elif kind(4, ranks):
        return(7, kind(4,ranks), kind(1, ranks))




