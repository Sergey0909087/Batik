import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHARACTER_SCALING = 1
SCREEN_TITLE = "Работа со слайдами"
TILE_SCALING = 0.5
class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.scene = None
        self.player_sprite = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source,CHARACTER_SCALING)
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


    def on_draw(self):
        self.clear()
        self.player_sprite.draw()
        self.ground_list.draw()

    def update(self, delta_time:float):
        pass


if __name__ == "__main__":
    game = Game()
    game.setup()
    arcade.run()