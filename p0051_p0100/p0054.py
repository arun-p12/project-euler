'''
Given the cards dealt during the poker series between two players (1000 games),
how many games did player 1 win?
'''
# rekey the cards to assist sorting
def rekey_cards(h, key):
    v, s = 0, 1             # value and suit
    for i in range(len(h)):
        if h[i][v] in key: h[i] = key[h[i][v]] + h[i][s]
    return h

# for debugging ... revert cards back to human readable notation
def unkey_analsis(win):
    mk = {}
    for k, v in key1.items():
        mk[v] = k

    nwin = {'suit': win['suit'], 'seq': win['seq'], 'fh': {}}
    nwin['hc'] = mk[win['hc']]
    for k in win['fh']:
        nwin['fh'][mk[k]] = win['fh'][k]
    #print("lyze : ", nwin)
    return(nwin)

# sort the cards to assit determining the winning hand
def sort_hand(hand):
    rekey_cards(hand, key1)
    for i in range(1, len(hand)):
        j, ok = i - 1, True
        card = hand[i]
        while(ok and card[0] < hand[j][0]):
            hand[j+1] = hand[j]
            j -= 1
            if j < 0: ok = False
        hand[j+1] = card
    return(hand)

def save_details(hand):
    win = { 'hc': '0',      # high card
            'fh': {},       # covers 1p, 2p, 3k, 4k, full house
            'suit': True,   # covers flush, and  half of st./ royal flush
            'seq': True,    # covers straight and half of royal flush

    }
    v, s = 0, 1                     # value and suit
    prev_val = ord(hand[0][v]) - 1  # 1 less than the first card
    for card in hand:
        # are the cards of the same suit?
        if win['suit'] and card[s] != hand[0][s]:
            win['suit'] = False
        # are the cards in sequence?
        if win['seq'] and ord(card[v]) == prev_val+1:
            prev_val = ord(card[v])
        else:
            win['seq'] = False
        # get histogram by card value
        if card[v] in win['fh']: win['fh'][card[v]] += 1
        else: win['fh'][card[v]] = 1
        # save the highest value
        if ord(card[v]) > ord(win['hc']): win['hc'] = card[v]
    return(win)

# identify the winning combination in the hand
def check_winning(win):
    # royal flush, straight flush, flush or straight
    if win['suit']:
        if win['seq']:
            if win['hc'] == 'A': return [10, 'A', 'Royal Flush']
            else: return [9, win['hc'], "Straight Flush"]
        else: return [6, win['hc'], "Flush"]
    if win['seq']: return [5, win['hc'], "Straight"]

    # 4 of a kind, Full house, 3 of a kind, 2 pairs, 1 pair
    h_len = len(win['fh'])
    for k, v in win['fh'].items():
        if v == 4 and h_len == 2: return [8, k, "Four of a Kind"]
        elif v == 3:
            if h_len == 2: return [7, k, "Full House"]
            else: return [4, k, "3 of a Kind"]
        elif v == 2:
            if h_len == 3: return [3, k, "Two Pairs"]
            else: return [2, k, "One Pair", win['hc']]

    # base case : high card
    return [1, win['hc'], "High Card"]

# idenify and declare winner ... keep count of winnings
def declare_winner(res1, res2):
    cnt1, cnt2 = 0, 0
    print("show : ", res1, res2)
    if res1[0] > res2[0]:
        print("Player 1 wins : ", res1[2], "over", res2[2])
        cnt1 += 1
    elif res1[0] < res2[0]:
        print("Player #2 wins :", res1[2], "undr", res2[2])
        cnt2 += 1
    else:           # next level tie breaker
        if res1[0] <= 2:
            if key1[res1[1]] > key1[res2[1]]:
                print("Player A wins : ", res1[1], "over", res2[1])
                cnt1 += 1
            elif key1[res1[1]] < key1[res2[1]]:
                print("Player B wins : ", res1[1], "undr", res2[1])
                cnt2 += 1
            else:
                if key1[res1[3]] > key1[res2[3]]:
                    print("Player x wins : ", res1[3], "over", res2[3])
                    cnt1 += 1
                elif key1[res1[3]] < key1[res2[3]]:
                    print("Player y wins : ", res1[3], "undr", res2[3])
                    cnt2 += 1
                else:
                    print("this blows ... more analysis needed")
                    input("Enter any key")
        else:
            print("more analysis needed")
            input("enter any key")
    return(cnt1, cnt2)

# analyze the hand, and save the relevant details for winning combo
def analyze_hand(hand):
    #print("hand : ", hand)
    hand = sort_hand(hand)
    #print("sort : ", hand)
    win = save_details(hand)
    #print("lyze :", win)
    win = unkey_analsis(win)
    result = check_winning(win)
    return(result)


# game on... cycle thru all hands
def play_game(file='./p0054_poker.txt'):
    hands = [hand.strip().split() for hand in open(file, "r").readlines()]
    cnt1, cnt2 = 0, 0
    for i in range(len(hands)):
        print("Game : ", i, " :: ", hands[i])
        player1 = hands[i][:5]
        player2 = hands[i][5:]
        #print(player1, "\t\t", player2)
        res1 = analyze_hand(player1)
        res2 = analyze_hand(player2)
        p1, p2 = declare_winner(res1, res2)
        cnt1 += p1
        cnt2 += p2
        print()
    print("Winnigs by Player #1 : ", cnt1, "out of ", cnt1+cnt2)



import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

# reset the card values for comparison, and play
key1 = {'2': 'a', '3': 'b', '4':'c', '5':'d', '6':'e', '7':'f', '8':'g',
        '9':'h', 'T': 'i', 'J': 'j', 'Q': 'k', 'K': 'l', 'A': 'm'}
play_game()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
