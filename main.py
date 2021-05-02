import tictactoe


def main():
    print("Welcome to the game of Tic Tac Toe!")
    print("We are playing on a flexible board size and the first person to get 4 in a row wins!")
    while True:
        try:
            size = int(input("Select the size of the board (min - 4, max - 9): "))
            if size not in range(4, 10):
                raise Exception
        except (TypeError, ValueError):
            print("Incorrect input!")
        except Exception:
            print("Size of the board must be between 4 and 9!")
        else:
            game = tictactoe.TicTacToe(size)
            game.clear()
            game.draw_board()
            playing = True
            while playing:
                for actor in "x", "o":
                    game.player_turn(actor)
                    game.update_board()
                    if game.check_winning_conditions(actor):
                        playing = False
                        break
            break


if __name__ == "__main__":
    main()
