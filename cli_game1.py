import random as r
# function to select random word*********
def ran_word():
    word_list=["apple","banana","cherry","pear","mango","orange","strawberry","kivi","pineapple"]
    index=r.randint(0,len(word_list)-1)
    return word_list[index]


# function to print
def print_all(current_status, attempt_rem):
    print("CURRENT STATUS:",end=" ")

    for i in current_status:
        print(i,end=" ")

    print("ATTEMPTS REMAINING: ",end=" ")
    print(attempt_rem)


# function to check weather the input character is present in word
def check_char(random_word,current_status,attempt_rem,input_char):
    if input_char in random_word:                                                      # check input character in present in word
        current_status=change_current_status(random_word,current_status,input_char)       #if pesent called change_current_status
    else:
        attempt_rem = attempt_rem-1
    return current_status , attempt_rem


#to change the current stauts if word is present
def change_current_status(random_word,current_status,input_char):
    modify=""                                                                               #empty string
    for i in range(len(random_word)):                                                       #loop to check each element of random word
        if current_status[i]=="_" and random_word[i]==input_char:         #check if char in random word is present in random word and current state is space
            modify +=input_char                                            #if true extend in modify
        else:
            modify +=current_status[i]                                      #else extend space
    return modify


def game_check(random_word,attempt_rem,change_status):
    if random_word==change_status:
        print("!!!!YEAH CONGRATS YOU WON!!!!!!!")
        return True
    if attempt_rem <=0:
        print("SRY YOU LOST......HAVE A NXT TRY!!!!")
        print("WORD WAS", end="")
        print(random_word)
        return True
    return  False


#main function *************
def play(attempt=5):

    random_word = ran_word()

    current_status = "_" * len(random_word)                     # to count no of space as per word

    attempt_rem = attempt

    print_all(current_status, attempt_rem)                       # to print the spaces and attempts left

    while True:

        input_char=input("GUESS THE CHARACTER:")

        print("")

        current_status,attempt_rem=check_char(random_word,current_status,attempt_rem,input_char)

        print_all(current_status, attempt_rem)

        game_end=game_check(random_word,attempt_rem,current_status)

        if game_end==True:
            break
if __name__ == "__main__":
    play()
