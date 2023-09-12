import random

VALID_OPTIONS = ['rock', 'paper', 'scissors']
score_game = [0, 0]


def run_game():
    while True:
        print("Please enter your choice(rock, paper, scissors): ")
        user_choice = input()
        if user_choice not in VALID_OPTIONS:
            print("Invalid option. Please try again.")
            return run_game()
        print("You chose: " + user_choice)

        computer_choice = random.choice(VALID_OPTIONS)
        print("The computer chose: " + computer_choice)
        if user_choice == computer_choice:
            print("It's a tie!")
            print(f'Your score: {score_game[0]} Computer score: {score_game[1]}')
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print("You win!")
            score_game[0] += 1
            print(f'Your score: {score_game[0]} Computer score: {score_game[1]}')
        elif user_choice == 'paper' and computer_choice == 'rock':
            print("You win!")
            score_game[0] += 1
            print(f'Your score: {score_game[0]} Computer score: {score_game[1]}')
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print("You win!")
            score_game[0] += 1
            print(f'Your score: {score_game[0]} Computer score: {score_game[1]}')
        else:
            print("You lose!")
            score_game[1] += 1
            print(f'Your score: {score_game[0]} Computer score: {score_game[1]}')

        print("Would you like to play again? (y/n)")
        play_again = input()
        if play_again != 'y':
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("--------------------------------")
    print("Welcome to Rock, Paper, Scissors!")
    print("--------------------------------")
    print("menu:")
    print("1. Play game")
    print("2. View score")
    print("3. Reset score")
    print("4. Quit")
    print("Please enter your choice: ")
    option = input()

    while option != '4':
        if option == '1':
            run_game()
            option = str(5)
        elif option == '2':
            if score_game[0] == 0 and score_game[1] == 0:
                print("The score is 0. Please play a game first.")
                print("--------------------------------")
                option = str(5)
            elif score_game[0] > score_game[1]:
                print('Your score is ' + str(score_game[0]) + ' and the computer score is ' + str(
                    score_game[1]) + '. You are winning!')
                print("--------------------------------")
                option = str(5)
            elif score_game[0] == score_game[1]:
                print('Your score is ' + str(score_game[0]) + ' and the computer score is ' + str(
                    score_game[1]) + '. You are tied!')
                print("--------------------------------")
                option = str(5)
            else:
                print('Your score is ' + str(score_game[0]) + ' and the computer score is ' + str(
                    score_game[1]) + '. You are losing!')
                print("--------------------------------")
                option = str(5)
        elif option == '3':
            if score_game[0] == 0 and score_game[1] == 0:
                print("The score is already 0. Please play a game first.")
                print("--------------------------------")
                option = str(5)
            else:
                score_game = [0, 0]
                print("Score has been reset.")
                print("--------------------------------")
                option = str(5)
        elif option == '5':
            print("menu:")
            print("1. Play game")
            print("2. View score")
            print("3. Reset score")
            print("4. Quit")
            print("Please enter your choice: ")
            option = input()

        else:
            print("Invalid option. Please try again.")
            print("Please enter your choice (1 to 4): ")
            option = input()

    print("Thank you for playing!")
