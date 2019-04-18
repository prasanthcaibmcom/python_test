import shlex
import copy


class TicTacToeBoard:
    def __init__(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]

    def is_game_over(self):
        return self.is_game_won() or self.is_cats_game()

    def is_cats_game(self):
        if not self.is_game_won():
            for row in self.board:
                for item in row:
                    if not item:
                        return False
            return True
        return False

    def is_game_won(self):
        is_won = self.is_cross_won()
        if not is_won:
            for i in range(3):
                is_won = self.is_row_won(i) or self.is_column_won(i)
                if is_won:
                    break
        if is_won:
            return is_won
        else:
            return False

    def is_row_won(self, row):
        return self.board[row][0] is not None \
               and self.board[row][0] == self.board[row][1] == self.board[row][2]

    def is_column_won(self, column):
        return self.board[0][column] is not None \
               and self.board[0][column] == self.board[1][column] == self.board[2][column]

    def is_cross_won(self):
        return self.board[0][0] is not None and self.board[0][0] == self.board[1][1] == self.board[2][2] or \
               self.board[0][2] is not None and self.board[0][2] == self.board[1][1] == self.board[2][0]

    def put_x(self, x, y):
        if self.board[x][y] is None:
            self.board[x][y] = "X"
        else:
            print("cannot put X in {},{}".format(x, y))

    def put_o(self, x, y):
        if self.board[x][y] is None:
            self.board[x][y] = "O"
        else:
            print("cannot put O in {},{}".format(x, y))

    def print_board(self, pointer_location):
        display_board = copy.deepcopy(self.board)
        current_value_at_pointer = display_board[pointer_location[0]][pointer_location[1]]
        if current_value_at_pointer is not None:
            display_board[pointer_location[0]][pointer_location[1]] = "*" + str(current_value_at_pointer) + "*"
        else:
            display_board[pointer_location[0]][pointer_location[1]] = "**"

        i = 0
        for row in display_board:
            print("{}|{}|{}".format(self.get_print_value(row[0]),
                                    self.get_print_value(row[1]),
                                    self.get_print_value(row[2])))
            if i == 0 or i == 1:
                print("------------")
            i += 1

    @staticmethod
    def get_print_value(value):
        if value is not None:
            return " {} ".format(value)
        else:
            return "   "

    def already_marked(self, pointer):
        if self.board[pointer[0]][pointer[1]] is not None:
            return True


def move_cursor_up(pointer):
    if pointer[0] != 0:
        pointer = (pointer[0] - 1, pointer[1])
    return pointer


def move_cursor_down(pointer):
    if pointer[0] != 2:
        pointer = (pointer[0] + 1, pointer[1])
    return pointer


def move_cursor_left(pointer):
    if pointer[1] != 0:
        pointer = (pointer[0], pointer[1] - 1)
    return pointer


def move_cursor_right(pointer):
    if pointer[1] != 2:
        pointer = (pointer[0], pointer[1] + 1)
    return pointer


print("Player 1 begins.")
print("Type left, right, up, and down to move the pointer.")
print("Type mark to mark the position.")

MARK_O = "O"
MARK_X = "X"
is_player_one = True

new_board = TicTacToeBoard()
cursor_point = (0, 0)
new_board.print_board(cursor_point)

while True:
    cmd, *args = shlex.split(input('> '))

    if cmd == 'left':
        cursor_point = move_cursor_left(cursor_point)
    elif cmd == 'right':
        cursor_point = move_cursor_right(cursor_point)
    elif cmd == 'up':
        cursor_point = move_cursor_up(cursor_point)
    elif cmd == 'down':
        cursor_point = move_cursor_down(cursor_point)
    elif cmd == 'mark':
        if new_board.already_marked(cursor_point):
            print("This point is already marked!")
        else:
            if is_player_one:
                new_board.put_o(cursor_point[0], cursor_point[1])
            else:
                new_board.put_x(cursor_point[0], cursor_point[1])
            is_player_one = not is_player_one

            if new_board.is_cats_game():
                print("Game is drawn!")
                break
            elif new_board.is_game_won():
                print("Game won!")
                break
    elif cmd == 'exit':
        break
    else:
        print('Unknown command: {}'.format(cmd))

    new_board.print_board(cursor_point)
