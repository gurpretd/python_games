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
        pygame.init()
        self.main_screen = pygame.display.set_mode((self.game_main_window_size, self.game_main_window_size +
                                                    self.game_text_window_height))

        pygame.draw.rect(self.main_screen, (100, 0, 0), (0, 0, self.game_main_window_size, self.game_main_window_size))
        pygame.draw.rect(self.main_screen, (100, 100, 100), (0, self.game_main_window_size, self.game_main_window_size,
                                                             self.game_text_window_height))

    def create_game_context(self):
        box_id = 0
        for row in range(3):
            for column in range(3):
                game_context = GameContext()

                # Calculate position and size
                rect = pygame.Rect(column * 200, row * 200, 200, 200)
                rect_surface = pygame.Surface((200, 200))

                # Fill the surface with the fill color
                FILL_COLOR = (200, 200, 200)  # Light gray color
                BORDER_COLOR = (0, 0, 0)  # Black border
                BORDER_WIDTH = 3

                # Fill the surface
                rect_surface.fill(FILL_COLOR)

                # Draw the border on top
                pygame.draw.rect(rect_surface, BORDER_COLOR, (0, 0, 200, 200), BORDER_WIDTH)

                # Set the default symbol (e.g., "b" for blank)
                symbol = "b"

                # Store information in game_context
                game_context.box_id = box_id
                game_context.symbol = symbol
                game_context.rect = rect
                game_context.rect_surface = rect_surface

                # Add the context to the game context list
                self.game_context.append(game_context)
                print(f"Filled default rect for {box_id} at {game_context.rect}")

                box_id += 1

    def print_game_context(self):
        for box_id in range(3 * 3):
            print(self.game_context[box_id].box_id, self.game_context[box_id].symbol, self.game_context[box_id].rect)

        print("game state", self.game_state, "current player", self.get_current_player(),
              "message", self.message)


    def detect_mouse_click(self):
        status = Error_Status.FAIL
        pos = None
        randomly_computed = False
        if randomly_computed:
            x = random.randint(0, 600)
            y = random.randint(0, 600)
            pos = (x, y)
        else:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
                    x, y = event.pos  # Get mouse click position
                    print(f"Mouse clicked at: ({x}, {y})")
                    pos = event.pos
                    status = Error_Status.SUCCESS

        print("Next pos is ", pos)
        return status, pos

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
                    self.update_box(box_id)
                    status = Error_Status.SUCCESS
                    break
                else:
                    print(pos, "collides with box", box_id, "already occupied")
                    status = Error_Status.BOX_ALREADY_OCCUPIED
                    break
        return status

    def set_next_player(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def get_current_player(self):
        return self.current_player

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
        self.game_context[2].symbol = 2
        self.game_context[5].symbol = 2
        self.game_context[8].symbol = 2
        self.update_box(2)
        self.update_box(5)
        self.update_box(8)

    def update_box(self, box_id):
        box_context: GameContext = self.game_context[box_id]
        rect_surface = box_context.rect_surface
        rect = box_context.rect

        if box_context.symbol == 1:
            symbol = "O"
        elif box_context.symbol == 2:
            symbol = "X"
        else:
            symbol = ""

        TEXT_COLOR = (0, 0, 0)  # Black
        font = pygame.font.Font(None, 200)
        text_surface = font.render(symbol, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(
            center=((self.game_main_window_size / 3) / 2, (self.game_main_window_size / 3) / 2))

        print(f" *** Drawn {symbol} to box {box_id}")
        rect_surface.blit(text_surface, text_rect)

    def draw_game_grid(self):
        print("Redraw Grid")
        for i in range(9):
            box = self.game_context[i]
            print(f" rendering at {box.rect.x} {box.rect.y}")
            self.main_screen.blit(box.rect_surface, (box.rect.x, box.rect.y))
            flip_screen()

    def update_message_box(self):

        TEXT_COLOR = (0, 0, 0)  # Black
        font = pygame.font.Font(None, 20)
        text_surface = font.render(self.message, True, TEXT_COLOR)
        # (x, y, width, height)
        rect = pygame.Rect(0, self.game_main_window_size + 50, self.game_main_window_size + 20, 100)
        pygame.draw.rect(self.main_screen, (100, 100, 100), (0, self.game_main_window_size, self.game_main_window_size,
                                                             self.game_text_window_height))
        self.main_screen.blit(text_surface, rect)
        flip_screen()


    def tic_tac_toe_play(self):
        print("play")
        # self.update_message_window()
        #      self.flip_screen()
        game_state = GAME_STATES.GAME_CONTINUE
        self.draw_game_grid()
        self.update_message_box()

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
                    self.message = f" Player {player_won} WINS"
                elif result == GAME_STATES.GAME_DRAW:
                    print("Game DRAW")
                    self.message = f"Game DRAW"
                    self.game_state = GAME_STATES.GAME_OVER
                else:
                    self.set_next_player()
                    self.message = f"Next Player {self.get_current_player()} \'s Turn"

            else:
                print("Invalid Move. Try again")
                self.message = f"Invalid Move. Try again"
            self.update_message_box()
            self.draw_game_grid()
            self.print_game_context()
            if self.game_state == GAME_STATES.GAME_OVER:
                input("enter to quit")


    def do_turn(self):
        status, pos = self.detect_mouse_click()
        if status == Error_Status.SUCCESS:
            status = self.process_mouse_click(pos)
        return status

game = Tic_Tac_Toe()
game.create_game_context()

game.tic_tac_toe_play()
