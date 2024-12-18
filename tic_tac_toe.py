import pygame
import random


class GAME_STATES:
    GAME_OVER = 0
    GAME_WIN = 1
    GAME_CONTINUE = 2
    GAME_DRAW = 3


class Error_Status:
    SUCCESS = 0
    FAIL = 1
    BOX_ALREADY_OCCUPIED = 2


class GameContext:
    box_id: int
    symbol: str
    rect_surface: pygame.Surface
    rect: pygame.Rect


def flip_screen():
    pygame.display.flip()


class Tic_Tac_Toe:
    main_screen = None
    game_context = list()
    game_state = GAME_STATES.GAME_CONTINUE
    running = True
    message = "Lets Start the game. 1st player takes O, second one X"
    current_player = 1
    game_main_window_size: int = 600
    game_text_window_height: int = 100

    def __init__(self):
        pass
        # self.main_screen = pygame.display.set_mode((self.game_main_window_size, self.game_main_window_size +
        #                                             self.game_text_window_height))
        #
        # pygame.draw.rect(self.main_screen, (100, 0, 0), (0, 0, self.game_main_window_size, self.game_main_window_size))
        # pygame.draw.rect(self.main_screen, (100, 100, 100), (0, self.game_main_window_size, self.game_main_window_size,
        #                                                    self.game_text_window_height))
        # flip_screen()

    def create_game_context(self):
        box_id = 0
        for row in range(3):
            for column in range(3):
                game_context = GameContext()
                # print(row, column)
                rect = pygame.Rect(column * 200, row * 200, 200, 200)
                rect_surface = pygame.Surface(size=(200, 200))
                symbol = "b"

                game_context.box_id = box_id
                game_context.symbol = symbol
                game_context.rect = rect
                game_context.rect_surface = rect_surface
                self.game_context.append(game_context)
                box_id = box_id + 1

    def print_game_context(self):
        for box_id in range(3 * 3):
            print(self.game_context[box_id].box_id, self.game_context[box_id].symbol, self.game_context[box_id].rect)

        print("game state", self.game_state, "current player", self.get_current_player(),
              "message", self.message)

    def detect_mouse_click(self):
        # pos = get_pos()
        x = random.randint(0, 600)
        y = random.randint(0, 600)
        pos = (x, y)
        print("Next pos is ", pos)
        return pos

    # Checks if the click is within the game window and if the clicked box is unused.
    # Otherwise returns failure.
    def process_mouse_click(self, pos):
        status = Error_Status.FAIL

        for box_id in range(3 * 3):
            box = self.game_context[box_id]

            if box.rect.collidepoint(pos):
                current_symbol = box.symbol
                if current_symbol == "b":
                    print(pos, "collides with box", box_id)
                    symbol = self.get_current_player()
                    box.symbol = symbol
                    status = Error_Status.SUCCESS
                    break
                else:
                    print(pos, "collides with box", box_id, "already occupied")
                    status = Error_Status.BOX_ALREADY_OCCUPIED
                    break
        return status

    def draw_box(self, box_id, value):
        pass
        # if value=="b":
        #     draw_b()
        # if symbol == "o":
        #     draw_0()
        # if symbol == "x":
        #     draw_x()

    def update_game_window(self):
        pass

    def set_next_player(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def get_current_player(self):
        return self.current_player

    # def update_game_context(self, box_id, player_id):
    #     # Check game context and update the box if one is unoccupied.
    #     #   Otherwise return error if box is already occupied.

    # This checks if it is a draw or game_win or continue game case.
    def check_game_result(self):

        result, player_won = self.check_win()
        if result != GAME_STATES.GAME_WIN:
            result = self.check_draw()
            if result != GAME_STATES.GAME_DRAW:
                result = GAME_STATES.GAME_CONTINUE
        return result, player_won

    def check_draw(self):
        if self.game_context[0].symbol != "b" and self.game_context[1].symbol != "b" and \
                self.game_context[2].symbol != "b" and self.game_context[3].symbol != "b" and \
                self.game_context[4].symbol != "b" and self.game_context[5].symbol != "b" and \
                self.game_context[6].symbol != "b" and self.game_context[7].symbol != "b" and \
                self.game_context[8].symbol != "b":
            return GAME_STATES.GAME_DRAW
        else:
            return GAME_STATES.GAME_CONTINUE

    def check_win(self):
        is_win = False
        player_won = None
        if (self.game_context[0].symbol == self.game_context[1].symbol and
                self.game_context[0].symbol == self.game_context[2].symbol and self.game_context[0].symbol != "b"):
            is_win = True
            player_won = self.game_context[0].symbol
            print("1")
        elif (self.game_context[0].symbol == self.game_context[4].symbol and
              self.game_context[0].symbol == self.game_context[8].symbol and self.game_context[0].symbol != "b"):
            is_win = True
            player_won = self.game_context[0].symbol
            print("2")
        elif (self.game_context[0].symbol == self.game_context[3].symbol and
              self.game_context[0].symbol == self.game_context[6].symbol and self.game_context[0].symbol != "b"):
            is_win = True
            player_won = self.game_context[0].symbol
            print("3")
        elif (self.game_context[2].symbol == self.game_context[5].symbol and
              self.game_context[2].symbol == self.game_context[8].symbol and self.game_context[2].symbol != "b"):
            is_win = True
            player_won = self.game_context[2].symbol
            print("4")
        elif (self.game_context[6].symbol == self.game_context[7].symbol and
              self.game_context[6].symbol == self.game_context[8].symbol and self.game_context[6].symbol != "b"):
            is_win = True
            player_won = self.game_context[6].symbol
            print("5")
        elif (self.game_context[1].symbol == self.game_context[4].symbol and
              self.game_context[1].symbol == self.game_context[7].symbol and self.game_context[1].symbol != "b"):
            is_win = True
            player_won = self.game_context[1].symbol
            print("6")
        elif (self.game_context[3].symbol == self.game_context[4].symbol and
              self.game_context[3].symbol == self.game_context[5].symbol and self.game_context[3].symbol != "b"):
            is_win = True
            player_won = self.game_context[3].symbol
            print("7")
        elif (self.game_context[2].symbol == self.game_context[4].symbol and
              self.game_context[2].symbol == self.game_context[6].symbol and self.game_context[2].symbol != "b"):
            is_win = True
            player_won = self.game_context[2].symbol
            print("8")

        if is_win:
            return GAME_STATES.GAME_WIN, player_won
        else:
            return GAME_STATES.GAME_CONTINUE, player_won

    def fill_fake_game_context(self):
        self.game_context[2].symbol = 1
        self.game_context[5].symbol = 1
        self.game_context[8].symbol = 1

    def tic_tac_toe_play(self):
        print("play")
        # self.update_message_window()
        #      self.flip_screen()
        game_state = GAME_STATES.GAME_CONTINUE
        while self.game_state == GAME_STATES.GAME_CONTINUE:
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:  # allow to leave the loop
            #         self.game_state = GAME_STATES.GAME_OVER
            #         continue

            print("current player", self.get_current_player())

            status = self.do_turn()
            if status == Error_Status.SUCCESS:
                # self.fill_fake_game_context()
                result, player_won = self.check_game_result()
                if result == GAME_STATES.GAME_WIN:
                    print(f" Player {player_won} WINS")
                    self.game_state = GAME_STATES.GAME_OVER
                elif result == GAME_STATES.GAME_DRAW:
                    print("Game DRAW")
                    self.game_state = GAME_STATES.GAME_OVER
                else:
                    self.set_next_player()
                    self.message = f"Next Player {self.get_current_player()} \'s Turn"
            else:
                print("Invalid Move. Try again")
            self.print_game_context()
            # input("enter to continue")

    def do_turn(self):
        pos = self.detect_mouse_click()
        status = self.process_mouse_click(pos)
        return status


game = Tic_Tac_Toe()
game.create_game_context()

game.tic_tac_toe_play()
# game.tic_tac_toe_play()
