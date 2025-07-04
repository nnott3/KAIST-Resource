import random

from cs1graphics import *

from nvm import NeverMind


_board = None


def create_board(width, height, num_mines):
    """To start the game, create Minesweeper object and call draw_scene function
    """
    global _board
    if _board:
        raise RuntimeError("A world already exists!")
    _board = Minesweeper(width, height, num_mines)
    _board.draw_scene()


def restart_board():
    """To restart the game, close scene and call create_board function
    """
    global _board
    if not _board:
        raise RuntimeError("A world doesn't exist!")
    _board._scene.close()
    width, height, num_mines = _board.width, _board.height, _board.num_mines
    _board = None
    create_board(width, height, num_mines)


class Tile(object):
    def __init__(self):
        self.hidden = True  # if the tile is hidden or not
        self.flagged = False  # if the tile is flagged or not
        self.mine = False  # if the tile has a mine or not
        self.value = 0  # the number of mines in surrounding tiles


class Minesweeper(NeverMind):
    def __init__(self, width, height, num_mines):
        """Sets up both UI and game logic
        """
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.num_flags = self.num_mines  # the number of flags left to display
        self.game_over = False  # if the game is finished or not

        if self.num_mines > self.width * self.height:
            print('Number of mines cannot exceed number of tiles!')
            exit()

        # Generate mines' positions randomly and apply them to Tile objects
        self.tiles = list()
        mine_indices = random.sample(range(self.width * self.height), k=self.num_mines)
        for i in range(self.height):
            tile_row = list()
            for j in range(self.width):
                tile_obj = Tile()
                if i * self.width + j in mine_indices:
                    tile_obj.mine = True
                tile_row.append(tile_obj)
            self.tiles.append(tile_row)

        self.initialize_value()  # to initialize each value of tiles
        self.cursor = [0, 0]  # initialize the cursor's position

    def initialize_value(self):
        """(10 pts.) Initializes each Tile object's value in self.tiles
        """
        height = len(self.tiles)
        width = len(self.tiles[0])
        ### ↓↓↓ IMPLEMENT HERE ↓↓↓ ###
        
        
        
        ### ↑↑↑ IMPLEMENT HERE ↑↑↑ ###
        pass

    def dig(self, pos):
        """Performs the dig action on the given coordinate and handles linked UI changes
        """
        selected_tile = self.tiles[pos[1]][pos[0]]
        if not selected_tile.hidden:  # skip the process if the tile is already opened
            return
        selected_tile.hidden = False  # open the tile

        self._nvm_select_layer(pos)
        self._nvm_clear_selected_layer()

        if not selected_tile.mine:
            if selected_tile.value > 0:  # display the digit
                self._nvm_display_digit(selected_tile)
            elif selected_tile.value == 0:  # automatically dig adjacent tiles
                for i in range(pos[1] - 1, pos[1] + 2):
                    for j in range(pos[0] - 1, pos[0] + 2):
                        if i < 0 or i >= self.height or j < 0 or j >= self.width:
                            continue
                        self.dig((j, i))
            self.game_over = self.check_win()  # to check if the player has won
            if self.game_over:  # game is over after digging no mine -> process victory
                self._nvm_process_victory()
        else:  # digging a mine -> process defeat
            self._nvm_process_defeat()

    def check_win(self):
        """(5 pts.) Checks if every tile not containing mine in self.tiles is uncovered

        :return: True if the player has won, otherwise False
        """
        ### ↓↓↓ IMPLEMENT HERE ↓↓↓ ###
        
        
        
        ### ↑↑↑ IMPLEMENT HERE ↑↑↑ ###
        pass

    def flag(self):
        """Performs the flag action on the given coordinate and handles linked UI changes
        """
        selected_tile = self.tiles[self.cursor[1]][self.cursor[0]]
        if not selected_tile.hidden:  # skip the process if the tile is already opened
            return

        self._nvm_select_layer(self.cursor)
        if selected_tile.flagged:  # unflag
            selected_tile.flagged = False
            self.num_flags += 1

            self._nvm_clear_selected_layer()
            self._nvm_create_hidden(self.selected_layer)
        else:  # flag
            selected_tile.flagged = True
            self.num_flags -= 1

            self._nvm_mark_flag()

        self._nvm_refresh_num_flags()

    def chord(self):
        """(5 pts.) Performs the chord action on the selected tile
        """
        if self.tiles[self.cursor[1]][self.cursor[0]].hidden:
            return

        ### ↓↓↓ IMPLEMENT HERE ↓↓↓ ###
        
        
        
        ### ↑↑↑ IMPLEMENT HERE ↑↑↑ ###


def interact():
    """Handles player's keyboard inputs
    """
    px_w_lb, px_w_ub = _board._padding, _board._scene_width - _board._padding
    px_h_lb, px_h_ub = _board._padding * 2 + _board._info_height, _board._scene_height - _board._padding
    while True:
        e = _board._scene.wait()
        d = e.getDescription()
        if d == 'keyboard':
            allow_dig = False
            k = e.getKey().lower()
            if k == 'q':  # halts the game
                _board._scene.close()
                break
            elif k == 'r':  # resets the game
                restart_board()
            elif not _board.game_over:
                if k == 'd':  # dig
                    _board.dig(_board.cursor)
                elif k == 'f':  # flag
                    _board.flag()
                elif k == 's':  # chord
                    _board.chord()
                else:
                    if k == 'i' and _board.cursor[1] > 0:  # up
                        _board.cursor[1] -= 1
                    elif k == 'k' and _board.cursor[1] < _board.height - 1:  # down
                        _board.cursor[1] += 1
                    elif k == 'j' and _board.cursor[0] > 0:  # left
                        _board.cursor[0] -= 1
                    elif k == 'l' and _board.cursor[0] < _board.width - 1:  # right
                        _board.cursor[0] += 1
                _board._nvm_redraw_cursor()  # redraw the cursor
        elif d == 'mouse click' or d == 'mouse drag':
            pos = e.getMouseLocation()  # get mouse location
            x = pos.getX()
            y = pos.getY()
            if px_w_lb <= x <= px_w_ub and px_h_lb <= y <= px_h_ub:  # on tile
                xq = (x - px_w_lb) // _board._tile_length
                yq = (y - px_h_lb) // _board._tile_length
                _board.cursor = [int(xq), int(yq)]  # move the cursor to the tile
                _board._nvm_redraw_cursor()  # redraw the cursor


if __name__ == '__main__':
    # You may uncomment the next line to fix the tiles' numbers for debugging purposes
    # random.seed(0)

    # It is okay to change the board's size or the number of mines for debugging purposes
    create_board(10, 9, 13)
    interact()
