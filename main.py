squares = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
line_v = "|"
line_h = "-----------------"
player1 = []
player2 = []
space = " "

def show_grid():
    grid = f"{squares[0]}  {line_v}  {squares[1]}  {line_v}  {squares[2]} " \
           f"\n{line_h}\n" \
           f"{squares[3]}  {line_v}  {squares[4]}  {line_v}  {squares[5]} " \
           f"\n{line_h}\n" \
           f"{squares[6]}  {line_v}  {squares[7]}  {line_v}  {squares[8]}"
    print(grid)


def player_choose_square(name):
    if name == name1:
        player1.append(chosen_square)
        squares[chosen_square-1] = "❌"
    else:
        player2.append(chosen_square)
        squares[chosen_square-1] = "⭕️"

    show_grid()


def check_for_win(player):
    if player == "pl1":
        stamp = "❌"
        name = name1
    else:
        stamp = "⭕️"
        name = name2

    if squares[0] == stamp and squares[1] == stamp and squares[2] == stamp:
        print(f"You Won, {name}!")
        return False
    elif squares[3] == stamp and squares[4] == stamp and squares[5] == stamp:
        print(f"You Won, {name}!")
        return False
    elif squares[6] == stamp and squares[7] == stamp and squares[8] == stamp:
        print(f"You Won, {name}!")
        return False
    elif squares[0] == stamp and squares[3] == stamp and squares[6] == stamp:
        print(f"You Won, {name}!")
        return False
    elif squares[1] == stamp and squares[4] == stamp and squares[7] == stamp:
        print(f"You Won, {name}!")
        return False
    elif squares[2] == stamp and squares[5] == stamp and squares[8] == stamp:
        print(f"You Won, {name}!")
        return False
    elif squares[0] == stamp and squares[4] == stamp and squares[8] == stamp:
        print(f"You Won, {name}!")
        return False
    elif squares[6] == stamp and squares[4] == stamp and squares[2] == stamp:
        print(f"You Won, {name}!")
        return False
    else:
        print("Continue")
        return True


print("Welcome to Tic-Tac-Toe Game!")
name1 = input("What is the name of Player 1? ")
name2 = input("What is the name of Player 2? ")

show_grid()

game_on = True
while game_on == True:
    player_1 = True
    player_2 = True
    while player_1:
        chosen_square = int(input(f"What square do you choose, {name1}?: "))
        if chosen_square in player1 or chosen_square in player2:
            print("The Square already has been chosen. Try another one.")
        else:
            player_choose_square(name1)
            game_on = check_for_win("pl1")
            player_1 = False
    if game_on == True:
        while player_2:
            chosen_square = int(input(f"What square do you choose, {name2}?: "))
            if chosen_square in player1 or chosen_square in player2:
                print("The Square already has been chosen. Try another one.")
            else:
                player_choose_square(name2)
                game_on = check_for_win("pl2")
                player_2 = False
