import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Work in sprits"
TILE_SCALING = 0.5

CHARACTER_SCALING = 1

class Game(arcade.Window):
    def __init__(self):
            super().__init__(SCREEN_WIDTH,  SCREEN_HEIGHT, SCREEN_TITLE)
            arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
            self.player_sprite = None
            self.player_list = None
            self.ground_list = None
            self.box_list = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)
        self.ground_list = arcade.SpriteList(use_spatial_hash=True)
        for x in range(0, 1250, 64):
            ground = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            ground.center_x = x
            ground.center_y = 32
            self.ground_list.append(ground)
        self.box_list = arcade.SpriteList(use_spatial_hash=True)
        coordinate_list = [[512, 96], [256,  96], [768, 96]]
        for coordinate in coordinate_list:
            box = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
            box.position = coordinate
            self.box_list.append(box)

    def on_draw(self):
        self.clear()
        self.player_sprite.draw()
        self.ground_list.draw()
        self.box_list.draw()
        

    def update(self, delta_time: float):
        pass

if __name__ == "__main__":
    game = Game()
    game.setup()
    arcade.run()


