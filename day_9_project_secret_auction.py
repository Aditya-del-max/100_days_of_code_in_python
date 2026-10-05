#silent auction
def find_highest_bidder(dictionary):
    highest_bid=0
    for key in dictionary:
        if dictionary[key]>highest_bid:
            highest_bid=dictionary[key]
            winner=key
    print(f"the winner is {winner} with a bid of ${highest_bid}")
# function to find the highest bidder in the dictionary of bids
print("Welcome to the secret auction program.")
contestent= True
dictionary={}
while contestent:
    name=input("what is your name? ")
    bid=int(input("what is your bid? $ "))
    dictionary[name]=bid
    continues=input("are there any other bidders? type 'yes' or 'no'.\n")
    if continues=="no":
        contestent=False
        find_highest_bidder(dictionary)
    else:
        print("\n" * 10)
        contestent=True
