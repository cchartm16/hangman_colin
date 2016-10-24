from random import choice
import turtle

# Get word from dictionary
dictionary = open("common_words.txt", "r")
# Use readlines in order to get each word, rather than each letter
word = choice(dictionary.readlines())
dictionary.close()

# --------------WARNING: SHOWS ANSWER
# print(word)


'''Edge cases Functions'''


def IsApostraphe(word):
    if "'" in word:
        print("Note: a ' is in the word. Go ahead and put that in there.")


def GetLetter():
    '''Gets move from user'''
    user_input = input(
        "Guess a letter and a position. First the letter, then the position (indicated by a number) Note that everything is lowercase.\n\n\n")

    while not IsValidMove(user_input):
        user_input = input("Invalid move! Please enter first a letter, then a number: ")

    return user_input


def IsValidMove(answer):
    '''Checks if move is valid'''
    if len(answer) > 1:
        return False
    else:
        return True


def ReDrawList(list1, list2):
    '''Makes a new list of blank spaces'''
    for i in range(len(list2)):
        list1.append("_")

    return list1


def CheckIfEquals(list1, list2):
    if list1 == list2:
        return True
    else:
        return False


def AddLettersToList(input, list1, list2):
    if input in list2:
        print("That letter, '" + input + "', is in there", list2.count(input), "times! Way to go!")
        for i in range(len(list2)):
            if list2[i] == input:
                del (list1[i])
                list1.insert(i, input)
    else:
        print("\n\n\nThat letter, '" + input + "', is NOT in there. Please try again: \n\n\n")


def main():
    '''Main function'''

    # Checks for apostrophe
    IsApostraphe(word)

    # Tells user how many letters the word is

    # NOTE: for some reason includes a newline character or something, so it's -1 for now...will fix LATER....
    print("Your word is:", len(word) - 1, "letters")

    # Gets input from user
    user_input = GetLetter()
    # While the word is incomplete
    word_list = list(word)
    user_word_list = []

    # List of used words
    used_letters = []

    temp_list = word_list[0: (len(word_list) - 1)]

    # --------------------------------WARNING: SHOWS ANSWER
    # print(temp_list)

    ReDrawList(user_word_list, temp_list)

    # While user_word_list not equal to temp_list
    # NOTE: There's a newline character, so will not compare all of word_list
    while not CheckIfEquals(user_word_list, temp_list):
        AddLettersToList(user_input, user_word_list, temp_list)

        # Prints a list for the user to see
        print(user_word_list)

        while user_input in used_letters:
            print("See:", used_letters, "\n\n")
            user_input = input("You've already used that letter! Try again: \n\n")

            AddLettersToList(user_input, user_word_list, temp_list)
            print(user_word_list)

            continue

        # Adds each guess
        # Note: checks FIRST if letter already in list
        if user_input not in used_letters:
            used_letters.append(user_input)

        print("\n\nYou have used the following letters:", used_letters)
        user_input = input("\nEnter another letter. If finished (i.e. you see the FULL word), just press 'Enter': ")
        continue

    # Winner statement
    print("You win! Your word was:", word)


main()


