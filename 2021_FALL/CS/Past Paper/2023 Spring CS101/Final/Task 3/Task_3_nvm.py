from cs1graphics import *

class NeverMind:
    def draw_scene(self):
        multiplier = 2
        self._tile_length = 16 * multiplier
        self._info_height = 32 * multiplier
        self._padding = 10 * multiplier
        self._border_width = 2 * multiplier
        self._scene_width = self.width * self._tile_length + self._padding * 2
        self._scene_height = self.height * self._tile_length + self._padding * 3 + self._info_height
        self._scene = Canvas(self._scene_width, self._scene_height, (192, 192, 192))
        self._scene.setTitle("Minesweeper")

        self._value_to_color = {
            1: (0, 0, 255),
            2: (0, 123, 0),
            3: (255, 0, 0),
            4: (0, 0, 123),
            5: (123, 0, 0),
            6: (0, 123, 123),
            7: (255, 255, 255),
            8: (123, 123, 123),
        }

        half_border_width = self._border_width / 2

        padding_color = (189, 189, 189)
        self._border_color_dark = (123, 123, 123)
        self._border_color_white = (255, 255, 255)

        outline_white_coords = [
            [(half_border_width, self._scene_height - half_border_width), (half_border_width, half_border_width),
             (self._scene_width - half_border_width, half_border_width)],
            [(self._padding - half_border_width, self._padding + self._info_height + half_border_width), (
                self._scene_width - self._padding + half_border_width,
                self._padding + self._info_height + half_border_width),
             (self._scene_width - self._padding + half_border_width, self._padding - half_border_width)],
            [(self._padding - half_border_width, self._scene_height - self._padding + half_border_width), (
                self._scene_width - self._padding + half_border_width,
                self._scene_height - self._padding + half_border_width), (
                 self._scene_width - self._padding + half_border_width,
                 self._padding * 2 + self._info_height - half_border_width)]
        ]
        for coords in outline_white_coords:
            outline = Path(*[Point(*coord) for coord in coords])
            outline.move(0.5, 0.5)
            outline.setBorderColor(self._border_color_white)
            outline.setBorderWidth(self._border_width)
            outline.setDepth(1)
            self._scene.add(outline)

        outline_dark_coords = [
            [(half_border_width, self._scene_height - half_border_width),
             (self._scene_width - half_border_width, self._scene_height - half_border_width),
             (self._scene_width - half_border_width, half_border_width)],
            [(self._padding - half_border_width, self._padding + self._info_height + half_border_width),
             (self._padding - half_border_width, self._padding - half_border_width),
             (self._scene_width - self._padding + self._border_width, self._padding - half_border_width)],
            [(self._padding - half_border_width, self._scene_height - self._padding + half_border_width),
             (self._padding - half_border_width, self._padding * 2 + self._info_height - half_border_width), (
                 self._scene_width - self._padding + half_border_width,
                 self._padding * 2 + self._info_height - half_border_width)]
        ]
        for coords in outline_dark_coords:
            outline = Path(*[Point(*coord) for coord in coords])
            outline.move(-0.5, -0.5)
            outline.setBorderColor(self._border_color_dark)
            outline.setBorderWidth(self._border_width)
            self._scene.add(outline)

        self.text_flags = Text('Flags left: %02d' % self.num_flags, self._tile_length, Point(0, 0))
        self.text_flags.moveTo(self._scene_width / 2, self._padding + self._info_height / 2)
        self.text_flags.setFontColor('red')
        self._scene.add(self.text_flags)

        for i in range(self.height):
            tile_line = Path(Point(self._padding, self._padding * 2 + self._info_height + self._tile_length * i),
                             Point(self._scene_width - self._padding,
                                   self._padding * 2 + self._info_height + self._tile_length * i))
            tile_line.setBorderColor(self._border_color_dark)
            tile_line.setBorderWidth(half_border_width)
            self._scene.add(tile_line)
        for i in range(self.width):
            tile_line = Path(Point(self._padding + self._tile_length * i, self._padding * 2 + self._info_height),
                             Point(self._padding + self._tile_length * i, self._scene_height - self._padding))
            tile_line.setBorderColor(self._border_color_dark)
            tile_line.setBorderWidth(half_border_width)
            self._scene.add(tile_line)

        x0 = self._tile_length / 2 + self._padding
        y0 = self._tile_length / 2 + self._padding * 2 + self._info_height

        self.tile_layers = list()
        for i in range(self.height):
            tile_layer_row = list()
            for j in range(self.width):
                tile_layer = Layer()
                self._nvm_create_hidden(tile_layer)

                tile_layer.moveTo(x0 + self._tile_length * j, y0 + self._tile_length * i)
                self._scene.add(tile_layer)
                tile_layer_row.append(tile_layer)
            self.tile_layers.append(tile_layer_row)

        self.cursor_box = Square(self._tile_length, Point(0, 0))
        self.cursor_box.setBorderColor('Red')
        self.cursor_box.setBorderWidth(self._border_width)
        self._scene.add(self.cursor_box)
        self._nvm_redraw_cursor()

    def _nvm_redraw_cursor(self):
        x0 = self._tile_length / 2 + self._padding
        y0 = self._tile_length / 2 + self._padding * 2 + self._info_height
        self.cursor_box.moveTo(x0 + self._tile_length * self.cursor[0], y0 + self._tile_length * self.cursor[1])

    def _nvm_select_layer(self, pos):
        self.selected_layer = self.tile_layers[pos[1]][pos[0]]
    
    def _nvm_clear_selected_layer(self):
        self.selected_layer.clear()

    def _nvm_display_digit(self, selected_tile):
        text_value = Text('%1d' % selected_tile.value, self._tile_length / 2, Point(0, 0))
        text_value.setFontColor(self._value_to_color[selected_tile.value])
        self.selected_layer.add(text_value)

    def _nvm_mark_flag(self):
        half_border_width = self._border_width / 2

        flag_black = Polygon(Point(0, 0), Point(0, half_border_width * 2),
                             Point(half_border_width * 3, half_border_width * 3.5),
                             Point(half_border_width * 3, half_border_width * 4),
                             Point(half_border_width * (-4), half_border_width * 4),
                             Point(half_border_width * (-4), half_border_width * 3), Point(0, half_border_width * 2))
        flag_black.move(half_border_width, 0)
        flag_black.setFillColor('Black')
        flag_black.setBorderWidth(half_border_width)
        self.selected_layer.add(flag_black)

        flag_red = Polygon(Point(0, 0), Point(0, half_border_width * (-4)),
                           Point(half_border_width * (-1), half_border_width * (-4)),
                           Point(half_border_width * (-4), half_border_width * (-2.5)))
        flag_red.move(half_border_width, 0)
        flag_red.setFillColor('Red')
        flag_red.setBorderWidth(half_border_width)
        flag_red.setBorderColor('Red')
        self.selected_layer.add(flag_red)

    def _nvm_refresh_num_flags(self):
        self.text_flags.setMessage('Flags left: %d' % self.num_flags)

    def _nvm_create_hidden(self, layer):
        half_border_width = self._border_width / 2

        tile_outline1 = Path(Point(0, self._tile_length - self._border_width - half_border_width / 2), Point(0, 0),
                             Point(self._tile_length - self._border_width, 0))
        tile_outline1.setBorderColor(self._border_color_white)
        tile_outline1.setBorderWidth(self._border_width)
        tile_outline1.move(-self._tile_length / 2 + half_border_width, -self._tile_length / 2 + half_border_width)
        tile_outline1.setDepth(self._border_width)
        layer.add(tile_outline1)

        tile_outline2 = Path(Point(0, self._tile_length - self._border_width),
                             Point(self._tile_length - self._border_width, self._tile_length - self._border_width),
                             Point(self._tile_length - self._border_width, 0))
        tile_outline2.setBorderColor(self._border_color_dark)
        tile_outline2.setBorderWidth(self._border_width)
        tile_outline2.move(-self._tile_length / 2 + half_border_width, -self._tile_length / 2 + half_border_width)
        layer.add(tile_outline2)

    def _create_mine(self, layer):
        unit_length = self._border_width / 2
        mine_layer = Layer()

        mine_line_coords = [[(0, -6), (0, 6)], [(-6, 0), (6, 0)], [(-4, -4), (4, 4)], [(-4, 4), (4, -4)]]
        for mine_line_coord in mine_line_coords:
            mine_line = Path(*[Point(coord[0] * unit_length, coord[1] * unit_length) for coord in mine_line_coord])
            mine_line.setBorderWidth(unit_length)
            mine_layer.add(mine_line)

        mine_circle = Circle(unit_length * 4, Point(0, 0))
        mine_circle.setFillColor('Black')
        mine_circle.setBorderWidth(0)
        mine_layer.add(mine_circle)

        mine_square = Square(unit_length * 2, Point(0, 0))
        mine_square.setFillColor('White')
        mine_square.setBorderWidth(0)
        mine_square.moveTo(-unit_length * 1.5, -unit_length * 1.5)
        mine_layer.add(mine_square)

        layer.add(mine_layer)

    def _remove_cursor_box(self):
        try:
            self._scene.remove(self.cursor_box)
        except:
            pass

    def _nvm_process_defeat(self):
        square_mine = Square(self._tile_length, Point(0, 0))
        square_mine.setBorderWidth(0)
        square_mine.setFillColor('Red')
        self.selected_layer.add(square_mine)

        self._create_mine(self.selected_layer)

        self.game_over = True

        for i in range(self.height):
            for j in range(self.width):
                if i == self.cursor[1] and j == self.cursor[0]:
                    continue
                tile_obj = self.tiles[i][j]
                if tile_obj.mine:
                    tile_layer = self.tile_layers[i][j]
                    tile_layer.clear()
                    self._create_mine(tile_layer)

        self.text_flags.setMessage('You lose!')
        self._remove_cursor_box()

    def _nvm_process_victory(self):
        for i in range(self.height):
            for j in range(self.width):
                tile_obj = self.tiles[i][j]
                if tile_obj.mine:
                    self.selected_layer = self.tile_layers[i][j]
                    self.selected_layer.clear()
                    self._nvm_create_hidden(self.selected_layer)
                    self._nvm_mark_flag()

        self.text_flags.setMessage('You win!')
        self._remove_cursor_box()