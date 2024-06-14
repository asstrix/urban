top = f"{' ' * 2}┌─────┬─────┬─────┐"  # top line
mid = f"{' ' * 2}├─────┼─────┼─────┤"  # middle line
bot = f"{' ' * 2}└─────┴─────┴─────┘"  # bottom line
values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # array of possible values 'X', 'O' or ' ' (empty)


def draw_board(arg):
	print(top)  																				# ┌─────┬─────┬─────┐
	print(f"{' ' * 2}│  {values[0 * 3]}  │  {values[0 * 3 + 1]}  │  {values[0 * 3 + 2]}  │")  	# │     │     │     │
	print(mid)  																				# ├─────┼─────┼─────┤
	print(f"{' ' * 2}│  {values[1 * 3]}  │  {values[1 * 3 + 1]}  │  {values[1 * 3 + 2]}  │")  	# │     │     │     │
	print(mid)  																				# ├─────┼─────┼─────┤
	print(f"{' ' * 2}│  {values[2 * 3]}  │  {values[2 * 3 + 1]}  │  {values[2 * 3 + 2]}  │")  	# │     │     │     │
	print(bot)  																				# └─────┴─────┴─────┘
	print("Emtpy cells:", (','.join([i for i in values if i != 'X' and i != 'O'])))


print('\n' + 'Welcome to tic tac toe')
draw_board(values)
#values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
choice = int(input('Enter the field cell number: ')) - 1
values[choice] = 'X'
draw_board(values)
