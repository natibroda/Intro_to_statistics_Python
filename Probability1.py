# Suppose we have 2 coins. We pick one at random from the bag and we flip it three times. 
# Let's ask the user for the combination of three flips he or she is interested in:

combination = input("Please state the combination of three coin flips using H and T: ")

# Let's also ask for probabilities of heads in coin 1 and coin 2:

coin1_H = float(input("Please enter the probability of heads for coin 1: "))
coin2_H = float(input("Please enter the probability of heads for coin 2: "))

# Let's assume that it is equally likely to pick each coin from the bag.

pick_coin = 0.5

def calculate_flips(combination, coin1_H, coin2_H):
    # Now we can calculate the probability of tails for each coin.
    coin1_T = 1 - coin1_H
    coin2_T = 1 - coin2_H
    # Initiate probability for each coin to 1
    P_coin1 = 1;
    P_coin2 = 1;
    # Now we need to loop through the string to determine the result of each flip.
    for letter in combination:
        if letter == 'H':
            P_coin1 = P_coin1 * coin1_H
            P_coin2 = P_coin2 * coin2_H
        elif letter == 'T':
            P_coin1 = P_coin1 * coin1_T
            P_coin2 = P_coin2 * coin2_T
    return [round(P_coin1, 4), round(P_coin2, 4)]

answer = calculate_flips(combination, coin1_H, coin2_H)

coin1 = answer[0]
coin2 = answer[1]

# Calculate the total probability of this event

P_total = pick_coin * (coin1 + coin2)
print("Total probability of this event occurring is: {}".format(P_total))