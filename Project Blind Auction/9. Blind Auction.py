#from replit import clear
from art import logo

print(logo)
#HINT: You can call clear() to clear the output in the console.
all_bids = {}

def highest_bidder():
    highest_bid = 0
    winner = ""
    for bidder in all_bids:
        bid_amount = all_bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        print(f"The winner is {bidder} with the bid of {highest_bid}")


def auction(name, bid):
    bids = {}
    bids[name] = bid
    all_bids.update(bids)   #this appends bids dict to all_bids main dict with all values
    
    
user_add = True
while user_add:    
    names_ip = input("Please enter your name: ")
    bids_ip = int(input("Please enter your bid: ₹"))

    auction(name = names_ip, bid = bids_ip)

    user_add = input("Wish to add other person? (ans in 'yes'/'no')")

    if user_add.lower() == 'no':
        user_add = False
        highest_bidder()

    #else:
        #clear()     #this is a replit function might not work in local IDE
