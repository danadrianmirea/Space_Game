import pygame as P
import random as R
from pygame_functions import *
# display
P.init()
P.display.set_caption('Space Hunter!')
max_x, max_y = 800, 800
main_screen = P.display.set_mode((max_x, max_y))
screenSize(max_x, max_y)
setAutoUpdate(True)
P.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))  # making curser invisible
# background
setBackgroundImage([".Images\Textures\stars_galaxy.jpg"])
bg_pic = P.image.load(".Images\Textures\stars_galaxy_bullured.jpg")
background_x, background_y = 0, 0
bg_scroll_speed = 3
bg_color = (0, 0, 0)
# player ship
ship = P.image.load(".Images\Objects\ship2.png").convert_alpha()
ship_x, ship_y = max_x//2, max_y - max_y//5
ship_x_change, ship_y_change = 0, 0
ship_change_by_key = 10
# enemy ships
enemy_pics = [P.image.load(".Images\Objects\ship_blue.png").convert_alpha(), P.image.load(".Images\Objects\ship_gray.png").convert_alpha(),
              P.image.load(".Images\Objects\ship_green.png").convert_alpha(), P.image.load(".Images\Objects\ship_orange.png").convert_alpha(), P.image.load(".Images\Objects\ship_red.png").convert_alpha(), P.image.load(".Images\Objects\ship_white.png").convert_alpha(), P.image.load(".Images\Objects\ship_yellow.png").convert_alpha()]
enemy_explosion_pic = P.image.load(r".Images\Objects\boom2.png").convert_alpha()
enemy_explosion_delay = 100
enemy_explosion_list = []
enemy_bullet_list = []
enemy_bullet_speed = -1
enemy_x, enemy_y = R.randint(10, 100), R.randint(10, max_y-10)
enemy_appear_time = 100
enemy = []  # list of active enemies
enemy_speed = 0.25
# player bullet
bullet = P.image.load(r".Images\Objects\bullet5.png").convert_alpha()
bullet_scale = 50
P.transform.scale(bullet, (bullet_scale, bullet_scale))
bullet_list = []
bullet_speed = 3
bullet_sound = P.mixer.Sound(".Sounds\gunshot.wav")
# enemy bullet
enemy_bullet_pic = P.image.load(r".Images\Objects\bullet1.png")
# color
White = (255, 255, 255)
Black = (0, 0, 0)
# missiles
missiles_pic = P.image.load(".Images\Objects\missile.png").convert_alpha()
Missile_using_pic = P.image.load(r".Images\Objects\boom1.png").convert_alpha()
Missiles = 0
Missile_explosion_delay = 150
Missile_cost = 2500
missile_sound = P.mixer.Sound(r".Sounds\bomb.wav")
Missile_limit = 5
Missile_boom = False
# lives
lives = P.image.load(".Images\Objects\heartred50.png").convert_alpha()
Life_cost = 5000
Lives = 3
Lives_limit = 5
# score
Score = 0
# other variables
Music = P.mixer.music.load(".Sounds\Epic Hip Hop.mp3")
margin_x = 100
Pause = False
Frame = P.time.Clock()
Level = 1
# texts and font
Font1 = P.font.SysFont('Victor Mono', 24, bold=True)
Font2 = P.font.SysFont('Mikhak', 20)
Font3 = P.font.SysFont('Victor Mono', 30, bold=True)
text_missile_hint = Font1.render("To Use Missile Press 'M'", True, White)
text_game_over = makeLabel("GAME OVER! ", 37, max_x//3+30, max_y//2-50, White, "Victor Mono")
text_mehrshad = makeLabel("Designed By Mehrshad", 24, max_x//3+25, max_y//2+25, White)
text_lives = Font1.render(f'Lives: {Lives}', True, White)
text_score = Font1.render(f'Score: {Score}', True, White)
text_level = Font1.render(f'Level: {Level}', True, White)
text_pause = Font3.render(f'GAME PAUSED', True, White)
text_mehrshad = Font2.render('Designed By Mehrshad', True, White)
