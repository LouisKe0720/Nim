#Name: Nim Game

import random
import time
import sys



#Type text characters with a delay
def type(text, delay = 0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay*0.4)
    print()



#Choose number of players
def players():
    type("\n" + "Welcome to Nim!\n" + "You can play it with 2 players or against the computer.", 0.07)
    type("Choose for 2 players (1), 1 player vs computer (2), or learn with the help of a computer (3).\n", 0.07)
    choice = input("Enter your choice: ")
    if choice == "1":
        type("You have chosen to play with 2 players.\n", 0.07)
        players_2()
    elif choice == "2":
        type("You have chosen to play against the computer.\n", 0.07)
        players_1()
    elif choice == "3":
        type("You have chosen to learn with the computer.\n", 0.07)
        computer_learning()
    else:
        #Invalid choice
        while choice != "1" or choice != "2" or choice != "3":
            type("Invalid choice. Please try again.\n", 0.07)
            choice = input("Enter your choice: ")
            if choice == "1":
                type("You have chosen to play with 2 players.", 0.07)
                players_2()
                break
            elif choice == "2":
                type("You have chosen to play against the computer.", 0.07)
                players_1()
                break     
            elif choice == "3":
                type("You have chosen to learn with the computer.", 0.07)
                computer_learning()
                break

#Player choice of difficulty
def player_choice():
    choice = input("Enter computer difficulty (1-10): ")
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        type("Invalid choice. Please enter 1 to 10.\n", 0.07)
        player_choice()
    return int(choice)



# Initialize piles
def initialize_piles():
    #Random number of counters in each pile for each game
    return [random.randint(1, 10) for i in range(3)]



# 2 Player game
def players_2():
    i = random.randint(1, 2)
    #Player names
    name_1 = input("Enter player 1's name: ")
    #If no name is entered, default name is Player 1
    if name_1 == "":
        name_1 = "Player 1"
    name_2 = input("Enter player 2's name: ")
    #If no name is entered, default name is Player 2
    if name_2 == "":
        name_2 = "Player 2"
    names = [name_1, name_2]
    if i == 1:
        type(names[0] + " goes first.\n", 0.07)
    else:
        type(names[1] + " goes first.\n", 0.07)
    display_pile(piles)

    #Game Loop continues game if there are counters left and the sum of the piles is greater than 1
    while any(piles) and sum(piles) > 1:
        type("\n" + names[i-1] + "'s turn.\n", 0.07)
        #Player move with player number
        player_move(piles, names[i-1])
        display_pile(piles)
        #Switch players
        if i == 1:
            i = 2
        else:
            i = 1
        

    #End of game if there is only 1 counter left after player move
    if sum(piles) == 1:
        type("\n" + names[i-1] + " loses because there is only 1 counter left!", 0.07)

    #End of game if there are no counters left after player moves, the player who took that last counter is the one who just moved
    elif sum(piles) == 0:
        type("\n" + names[i] + " loses because they took the last counter!", 0.07)



# 1 Player game vs computer
def players_1():
    name = input("Enter your name: ")
    #If no name is entered, default name is Player 1
    if name == "":
        name = "Player 1"
    difficulty = computer_difficulty()
    type("You go first.\n", 0.07)
    #Display the piles
    display_pile(piles)

    #Game Loop, continues game if there are counters left and the sum of the piles is greater than 1
    while any(piles) and sum(piles) > 1:
        type("\n" + name + "'s turn.", 0.07)
        #Player move
        player_move(piles, name)
        display_pile(piles)

        #End of game if there is only 1 counter left after player move
        if sum(piles) == 1:
            type("\n" + "The computer loses because there is only 1 counter left!", 0.07)
            break
        type("\n" + "Computer's turn.", 0.07)
        #Computer move
        computer_move(piles, difficulty)
        #Display the piles
        display_pile(piles)

        #End of game if there is only 1 counter left after computer move
        if sum(piles) == 1:
            type("\n" + name + " loses because there is only 1 counter left!", 0.07)
            break

        #End of game if there are no counters left after player moves. Computer never takes until all piles equals 0. Only the player can
        if sum(piles) == 0:
            type("\n" + name + " loses because they took the last counter!", 0.07)
            break


#Computer Difficulty
def computer_difficulty():
    choice = input("Enter computer difficulty (1-10): ")
    while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        type("Invalid choice. Please enter 1 to 10.\n", 0.07)
        choice = input("Enter computer difficulty (1-10): ")
        if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            return int(choice)
    if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        return int(choice)



#Computer move
def computer_move(piles, difficulty):
    if random.random() < difficulty / 10:  #User's choice

        #Winning move, if one pile has no counters, one has 1 counter and other has 1 or more, remove all counters from the pile with 1 or more counters
        if piles[0] == 0 and piles[1] == 1 and piles[2] != 0:
            piles[2] -= piles[2]
            type("Computer removed all counters from pile 3.\n", 0.07)
            return
        if piles[0] == 1 and piles[1] == 0 and piles[2] != 0:
            piles[2] -= piles[2]
            type("Computer removed all counters from pile 3.\n", 0.07)
            return
        if piles[0] == 1 and piles[1] != 0 and piles[2] == 0:
            piles[1] -= piles[1]
            type("Computer removed all counters from pile 2.\n", 0.07)
            return
        if piles[0] != 0 and piles[1] == 1 and piles[2] == 0:
            piles[0] -= piles[0]
            type("Computer removed all counters from pile 1.\n", 0.07)
            return
        if piles[0] != 0 and piles[1] == 0 and piles[2] == 1:
            piles[0] -= piles[0]
            type("Computer removed all counters from pile 1.\n", 0.07)
            return
        if piles[0] == 0 and piles[1] != 0 and piles[2] == 1:
            piles[1] -= piles[1]
            type("Computer removed all counters from pile 2.\n", 0.07)
            return
        
        #Winning move, if 2 piles has 0 counters, remove all counters except 1 from the last pile
        if piles[0] == 0 and piles[1] == 0 and piles[2] != 0:
            type("Computer removed " + str(piles[2]) +" counter from pile 3.\n", 0.07)
            piles[2] -= piles[2] - 1
            return
        if piles[0] == 0 and piles[1] != 0 and piles[2] == 0:
            type("Computer removed " + str(piles[1] - 1) +" counter from pile 2.\n", 0.07)
            piles[1] -= piles[1] - 1
            return 
        if piles[0] != 0 and piles[1] == 0 and piles[2] == 0:
            type("Computer removed " + str(piles[0] - 1) +" counter from pile 1.\n", 0.07)
            piles[0] -= piles[0] - 1
            return
        
        #Winning move, if 2 piles has 1 counter, remove all counters from the last pile
        if piles[0] == 1 and piles[1] == 1 and piles[2] != 0 and piles[2] != 1:
            type("Computer removed " + str(piles[2] - 1) +" counter from pile 3.\n", 0.07)
            piles[2] -= piles[2] - 1
            return
        if piles[0] == 1 and piles[1] != 0 and piles[1] != 1 and piles[2] == 1:
            type("Computer removed " + str(piles[1] - 1) +" counter from pile 2.\n", 0.07)
            piles[1] -= piles[1] - 1
            return
        if piles[0] != 0 and piles[0] != 1 and piles[1] == 1 and piles[2] == 1:
            type("Computer removed " + str(piles[0] - 1) +" counter from pile 1.\n", 0.07)
            piles[0] -= piles[0] - 1
            return
        
        #Winning move, if all piles have the same number of counters, remove all counters from one of the piles
        win_number = 0 
        for pile in piles:
            win_number ^= pile #XOR of all piles
        #There is a winning move
        if win_number != 0:
            #Only happens if the XOR of all piles is not 0
            for i in range(len(piles)): #Finds the pile to remove counters from
                target_pile = piles[i] ^ win_number #XOR of the pile and the win number
                if target_pile < piles[i]: #If the target pile is less than the current pile, this makes that pile the winning move
                    type("Computer removed " + str(piles[i] - target_pile) +" counters from pile " + str(i + 1) + ".\n", 0.07)
                    piles[i] = target_pile #Make the pile equal to the target pile
                    return

    #Chance of random move (depends on difficulty)
    while True:
        pile_index = random.randint(0, len(piles) - 1) #Random pile
        if piles[pile_index] > 0: #If the pile is not empty
            remove_count = random.randint(1, piles[pile_index]) #Random number of counters to remove
            piles[pile_index] -= remove_count #Remove the counters
            type("Computer removed " + str(remove_count) +" counters from pile " + str(pile_index + 1) + ".\n", 0.07)
            return        



#Computer Learning
def computer_learning():
    name = input("Enter your name: ")
    #If no name is entered, default name is Player 1
    if name == "":
        name = "Player 1"
    difficulty = computer_difficulty()
    type("You go first.\n", 0.07)
    #Display the piles
    display_pile(piles)

    #Game Loop, continues game if there are counters left and the sum of the piles is greater than 1
    while any(piles) and sum(piles) > 1:
        type("\n" + name + "'s turn.", 0.07)
        #Player move
        computer_evaluation(piles) #Computer recommends move (Best moves)
        player_move(piles, name)
        display_pile(piles)

        #End of game if there is only 1 counter left after player move
        if sum(piles) == 1:
            type("\n" + "The computer loses because there is only 1 counter left!", 0.07)
            break
        type("\n" + "Computer's turn.", 0.07)

        #Computer move
        computer_move(piles, difficulty)
        #Display the piles
        display_pile(piles)

        #End of game if there is only 1 counter left after computer move
        if sum(piles) == 1:
            type("\n" + name + " loses because there is only 1 counter left!", 0.07)
            break

        #End of game if there are no counters left after player moves. Computer never takes until all piles equals 0. Only the player can
        if sum(piles) == 0:
            type("\n" + name + " loses because they took the last counter!", 0.07)
            break


#Computer Evaluation (Learning)
def computer_evaluation(piles):
    if random.random() < 1: 

        #Winning move, if one pile has no counters, one has 1 counter and other has 1 or more, remove all counters from the pile with 1 or more counters
        if piles[0] == 0 and piles[1] == 1 and piles[2] != 0:
            type("The Computer recommends removing all counters pile 3", 0.07)
            return
        if piles[0] == 1 and piles[1] == 0 and piles[2] != 0:
            type("The Computer recommends removing all counters pile 3", 0.07)
            return
        if piles[0] == 1 and piles[1] != 0 and piles[2] == 0:
            type("The Computer recommends removing all counters pile 2", 0.07)
            return
        if piles[0] != 0 and piles[1] == 1 and piles[2] == 0:
            type("The Computer recommends removing all counters pile 1", 0.07)
            return
        if piles[0] != 0 and piles[1] == 0 and piles[2] == 1:
            type("The Computer recommends removing all counters pile 1", 0.07)
            return
        if piles[0] == 0 and piles[1] != 0 and piles[2] == 1:
            type("The Computer recommends removing all counters pile 2", 0.07)
            return
        
        #Winning move, if 2 piles has 0 counters, remove all counters except 1 from the last pile
        if piles[0] == 0 and piles[1] == 0 and piles[2] != 0:
            type("Computer recommends removing " + str(piles[2] - 1) + " counters from piles 3.\n", 0.07)
            return 
        if piles[0] == 0 and piles[1] != 0 and piles[2] == 0:
            type("Computer recommends removing " + str(piles[1] - 1) + " counters from piles 2.\n", 0.07)
            return 
        if piles[0] != 0 and piles[1] == 0 and piles[2] == 0:
            type("Computer recommends removing "+ str(piles[0] - 1) + " counters from piles 1.\n", 0.07)
            return 
        
         #Winning move, if 2 piles has 1 counter, remove all counters from the last pile
        if piles[0] == 1 and piles[1] == 1 and piles[2] != 0 and piles[2] !=1:
            type("Computer recommends removing " + str(piles[2] - 1) +" counters from pile 3.\n", 0.07)
            return
        if piles[0] == 1 and piles[1] != 0 and piles[1] != 1 and piles[2] == 1:
            type("Computer recommends removing " + str(piles[1] - 1) +" counter from pile 2.\n", 0.07)
            return
        if piles[0] != 0 and piles[0] != 1 and piles[1] == 1 and piles[2] == 1:
            type("Computer recommends removing " + str(piles[0] - 1) +" counter from pile 1.\n", 0.07)
            return

        #Winning move, if all piles have the same number of counters, remove all counters from one of the piles
        win_number = 0 
        for pile in piles:
            win_number ^= pile #XOR of all piles
        #There is a winning move
        if win_number != 0:
            #Only happens if the XOR of all piles is not 0
            for i in range(len(piles)): #Finds the pile to remove counters from
                target_pile = piles[i] ^ win_number #XOR of the pile and the win number
                if target_pile < piles[i]: #If the target pile is less than the current pile
                    type("Computer recommends removing " + str(piles[i] - target_pile) +" counters from pile " + str(i + 1) + ".\n", 0.07)
                    return


#Display the current piles
def display_pile(piles):
    type("\nCurrent piles: \n", 0.07)
    for i, pile in enumerate(piles):
        type("Pile " + str(i + 1) + ": (" + str(pile) + ")" +" *" * pile, 0.07)



#Player move
def player_move(piles, player):
    while True:
        try:
            #Choose a pile
            pile_index = int(input(str(player) + ", choose a pile (1-" + str(len(piles)) + "): ")) - 1
            if pile_index < 0 or pile_index >= len(piles) or piles[pile_index] == 0:
                type("Invalid pile. Try again.\n", 0.05)
                continue
            #Choose number of counters to remove from the pile
            remove_count = int(input(str(player) + ", choose number of counters to remove from pile " + str(pile_index + 1) + ": "))
            if remove_count <= 0 or remove_count > piles[pile_index]:
                type("Invalid number of counters. Try again.\n", 0.05)
                continue
            #Remove the counters from the pile
            for i in range(remove_count):
                piles[pile_index] -= 1
                type("\n" + "Removing counter...\n" + "Pile " + str(pile_index + 1) + ": " + "(" + str(piles[pile_index]) + ")" +  " *" * piles[pile_index], 0.03)
            break
        #Invalid input
        except ValueError:
            print("Invalid input. Try again.\n")



# Main game loop
while True:
    piles = initialize_piles()
    players()
    choice = input("Do you want to play again? yes (1) or no (2): ")
    if choice == "2":
        type("Thanks for playing! Goodbye!", 0.07)
        sys.exit()
    elif choice == "1":
        continue
    else:
        #Invalid choice
        while choice != "1" or choice != "2":
            type("Invalid choice. Please try again.\n", 0.07)
            choice = input("Do you want to play again? yes (1) or no (2): ")
            if choice == "2":
                type("Thanks for playing! Goodbye!", 0.07)
                sys.exit()
            elif choice == "1":
                break
            else:
                continue
    