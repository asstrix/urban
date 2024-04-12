top = "┌─────┬─────┬─────┐"  # top line
mid = "├─────┼─────┼─────┤"  # middle line
bot = "└─────┴─────┴─────┘"  # bottom line
values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # array of possible values 'X', 'O' or ' ' (empty)


def draw_board(arg):
	print(top)
	print(f"│  {values[0 * 3]}  │  {values[0 * 3 + 1]}  │  {values[0 * 3 + 2]}  │")
	print(mid)
	print(f"│  {values[1 * 3]}  │  {values[1 * 3 + 1]}  │  {values[1 * 3 + 2]}  │")
	print(mid)
	print(f"│  {values[2 * 3]}  │  {values[2 * 3 + 1]}  │  {values[2 * 3 + 2]}  │")
	print(bot)


draw_board(values)
