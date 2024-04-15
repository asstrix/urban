current_player = 'X'  # 'X' starts first
boardX = 0
boardO = 0
values = [' '] * 9


def draw_board(arg):
    top = "  ┌─────┬─────┬─────┐"
    mid = "  ├─────┼─────┼─────┤"
    bot = "  └─────┴─────┴─────┘"

    print(top)
    print(f"  │  {values[0]}  │  {values[1]}  │  {values[2]}  │")
    print(mid)
    print(f"  │  {values[3]}  │  {values[4]}  │  {values[5]}  │")
    print(mid)
    print(f"  │  {values[6]}  │  {values[7]}  │  {values[8]}  │")
    print(bot)


def check_winner(board):
    winning_positions = [7, 56, 448, 73, 146, 292, 273, 84]
    for pos in winning_positions:
        if board & pos == pos:  # To check if a player won, use bitwise (&)
            draw_board(values)
            return True
    return False


def get_player_choice():
    valid_input = False
    while not valid_input:
        try:
            choice = int(input("Enter a number of field (1-9): "))
            if 1 <= choice <= 9:
                valid_input = True
            else:
                print("Invalid input. Enter a number from 1 to 9.")
        except ValueError:
            print("Invalid input. Use only integers.")
    move = 1 << (choice - 1)  # Convert position to a bitmask
    return move


def valid_move(move, board_x, board_o):
    if (board_x & move) == 0 and (board_o & move) == 0:  # Check if positions is free in each boards
        return True
    else:
        return False


while True:
    draw_board(values)
    print("Emtpy cells:", *[i + 1 for i, v in enumerate(values) if v != 'X' and v != 'O'])
    print(f'It\'s {current_player}\'s turn')
    move_bitmask = get_player_choice()  # Get players move
    if valid_move(move_bitmask, boardX, boardO):
        index = (move_bitmask.bit_length() - 1)  # Determine index from mask
        values[index] = current_player
        if current_player == 'X':
            boardX |= move_bitmask  # Do 'X' turn
            if check_winner(boardX):
                print("X wins")
                break
            current_player = 'O'
        else:
            boardO |= move_bitmask  # Do 'O' turn
            if check_winner(boardO):
                print("O wins")
                break
            current_player = 'X'
    else:
        print("Invalid move. The cell is already in use.")
