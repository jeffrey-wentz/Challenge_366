

# this function takes two lists and checks to see if the second list is contained in the first list if a specific letter
# is removed.
def funnel(word1, word2):
    counter = 0
    # loops as many times as there are character in the first input
    while True:
        # this steps through each character in word 1
        for character in word1:
            # removes the character from the word
            del word1[counter]
            # if the two lists now equal each other then we have a word funnel
            if word1 == word2:
                print("True!")
                return 0
            # if they do not equal each other then we do not know if it is a word funnel yet
            else:
                # add the character back to it's original position
                word1.insert(counter, character)
                # this counter increases by 1 so if the next char removal does not reveal a word funnel it's position
                # can be tracked and inserted back to the list
                counter = counter + 1
        print("False")
        return 0


while True:
    word1 = list(input("Please enter your first word: "))
    word2 = list(input("Please enter your second word: "))
    funnel(word1, word2)
    cont = input("Would you like to check another?: ")
    if cont.lower() in ("no", "n", "nah", "nope"):
        break
