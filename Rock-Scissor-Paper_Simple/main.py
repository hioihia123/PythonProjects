##Simple Version of Rock Scissor Paper
##Rock > Scissor, Scissor > Paper, Rock > Paper
import random

rock = "Rock"
scissor = "Scissor"
paper = "Paper"

gameList = [rock, scissor,paper]
gameList_str = str(gameList)
print("Choose one of these 3"  + gameList_str + "\n")

user_score = 0
computer_score = 0

computer_won_str = "Sorry, the computer has won"
user_won_str = "Congratulation, you've won!"

while True:
    user_hasWon = False
    computer_hasWon = False
    ##ask for user inputs
    user_choice = input("What do you choose? (Rock, Scissor or Paper)" + "\n" )

    ##Computer_choice 
    computer_choice = random.randint(0,2)
    computer_choice_str = gameList[computer_choice]

    print("Computer chose " + computer_choice_str)
    
    if ((computer_choice_str == "Rock" and  user_choice == "Scissor") or
       (computer_choice_str == "Scissor" and user_choice == "Paper") or 
       (computer_choice_str == "Paper" and user_choice == "Rock")
    ):
        print(computer_won_str)
        computer_hasWon = True
        computer_score += 1
        print("Computer Score is " + str(computer_score) + "\n")
        
    elif(
        (user_choice == "Rock" and computer_choice_str == "Scissor") or 
        (user_choice == "Scissor" and computer_choice_str == "Paper") or 
        (user_choice == "Paper" and computer_choice_str == "Rock")
    ):
        user_hasWon = True
        print(user_won_str)
        user_score += 1
        print("Your score is " + str(user_score))
    elif user_choice == computer_choice_str:
        print("Tie Game")
        break
   

    
    user_input_after_game = input("Do you want to continue the game? Y or N" + "\n")
    print(user_input_after_game)
    if user_input_after_game != "Y":
        print("The score of the computer is " + str(computer_score) + "\n")
        print("Your score is " + str(user_score) + "\n")
        break
