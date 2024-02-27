import arcade
import random
import time

SCREEN_TITLE = "work with anamation"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

class Person(arcade.AnimatedTimeBasedSprite):
    def __init__(self, sprite, scale):
        super().__init__(sprite, scale)
        self.player = None

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.ground_list = None
        self.bg_layer1 = arcade.load_texture("resource/bg/background.png")
        self.bg_layer2 = arcade.load_texture("resource/bg/middleground.png")
        self.house_list = None

    def setup(self):
        self.ground_list = arcade.SpriteList()

        for j in range(0, SCREEN_WIDTH + 1, 16):
            r_sprite = random.randint(1, 2)
            ground = arcade.Sprite(f'resource/enviroments/wall-{r_sprite}.png')
            ground.center_x = j
            ground.center_y = 5
            self.ground_list.append(ground)

            self.player = Person('resource/person/bearded-idle/bearded-ide-1.png', 1)
            self.player.center_x = 50
            self.player.bottom = self.ground_list[0].top
            self.house_list = arcade.SpriteList()
            for i in range(3):
                house = arcade.Sprite(f'resource/enviroments/house-{i}.png')
                house.center_x = 80 + i * 220
                if i !=1:
                    house.center_y = 100
                else:
                    house.center_y = 130
                self.house_list.append(house)

    def on_draw(self):
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg_layer1)
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg_layer2)
        self.ground_list.draw()

        self

        self.house_list.draw()
if __name__ == '__main__':
    game = Game()
    game.setup()
    arcade.run()
        