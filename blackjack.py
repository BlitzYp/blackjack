import random
import pyfiglet

deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def allowed_to_play(player):
    if sum(player) > 21:
        return False
    return True

def check_endgame_results(player, computer):
    result1, result2 = sum(player), sum(computer)
    print(f"Final results: {player} {computer}")
    if (result1 > result2 and result1 <= 21) or result2 > 21:
        print("You win!")
    elif (result2 > result1 and result2 <= 21) or result1 > 21:
        print("You lose!")
    else:
        print("Draw")

def game_logic(player: list, computer: list, player_choice: bool = True):
    # Player logic
    if player_choice:
        print(f"Your current cards: {player}: total {sum(player)}\nComputers cards: {computer[0:len(computer)-1]}")
        if sum(player) == 21:
            check_endgame_results(player, computer)
            return
        if "y" in input("Draw another card?(y/n): "): player.append(random.choice(deck))
        else: player_choice = False

    # Logic for the computer
    computer_choice = random.randint(0, 1)
    if computer_choice > 0:
        computer.append(random.choice(deck))
    elif computer_choice == 0:
        check_endgame_results(player, computer)
        return
    if allowed_to_play(player) and allowed_to_play(computer):
        game_logic(player, computer, player_choice)
    else:
        check_endgame_results(player, computer)

if __name__ == "__main__":
    while True:
        if "n" in input("Want to play blackjack 0_0?(y/n): "):
            break
        print(pyfiglet.figlet_format("Blackjack"))
        player = [random.choice(deck), random.choice(deck)]
        computer = [random.choice(deck), random.choice(deck)]
        if sum(player) == 21:
            print("Blackjack...You won!")
            continue
        game_logic(player,computer)
    print("The game ended :0")