from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        Keys_get = key.get_pressed()
        if Keys_get[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if Keys_get[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        Keys_get = key.get_pressed()
        if Keys_get[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if Keys_get[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
                    
back = (96, 255, 128)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racked1 = Player('racked.png', 30, 200, 4, 50, 150)
racked2 = Player('racked.png', 525, 200, 4, 50, 150)
ball = GameSprite('asteroid.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 36)
lose_1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose_2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 6
speed_y = 6

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racked1.update_l()
        racked2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racked1, ball) or sprite.collide_rect(racked2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height-50 or ball.rect.y <0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose_1, (200,200))
            game_over = True

        if ball.rect.x > win_width-50:
            finish = True
            window.blit(lose_2, (200,200))
            game_over = True

        racked1.reset()
        racked2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)