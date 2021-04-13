import pygame as P
import random as R
import time as T
from Space_Game_var import *

# bullet


def bullet_manage(bullet_list, main_screen, bullet, bullet_speed, Pause):
    index_of_deleted = []
    for item in bullet_list:
        main_screen.blit(bullet, item)
        if item[1] <= 5 or item[1] >= max_y-25:
            index_of_deleted.append(bullet_list.index(item))
        if not Pause:
            item[1] -= bullet_speed
    for item in index_of_deleted:
        del bullet_list[item]


def shoot_bullet(ship_x, ship_y, player):
    global bullet_scale, bullet_list, bullet_sound, enemy_bullet_list, enemy_bullet_speed
    if player:
        bullet_sound.play()
        bullet_list.append([ship_x + bullet_scale * 2 // 3 + 3, ship_y])
    else:
        enemy_bullet_list.append([ship_x + bullet_scale * 2 // 3 + 3, ship_y])


# enemy


def enemy_manage(enemy, main_screen, Pause, Lives):
    global enemy_bullet_speed
    index_of_deleted = []
    for item in enemy:
        main_screen.blit(item[0], item[1])
        if item[1][1] >= max_y-25:
            Lives -= 1
            index_of_deleted.append(enemy.index(item))
        if not Pause:
            item[1][1] += item[2]
        # if P.time.get_ticks() % 120 == 0: # enable for enemy shooting
            # shoot_bullet(item[1][0], item[1][1], False)
            # enemy_bullet_speed = 10*enemy_speed
    for item in index_of_deleted:
        del enemy[item]
    return Lives


def enemy_explosion_manage(enemy_explosion_list):
    global main_screen, enemy_explosion_pic
    for i in enemy_explosion_list:
        main_screen.blit(enemy_explosion_pic, i)


def enemy_crash(Score):
    global bullet_list, enemy, enemy_explosion_list
    index_e, index_b = [], []
    for e in enemy:
        x_enemy = e[1][0]
        y_enemy = e[1][1]
        for b in bullet_list:
            x_bullet = b[0]
            y_bullet = b[1]
            if (x_enemy <= x_bullet <= x_enemy + 80) and (y_enemy <= y_bullet <= y_enemy + 80):
                enemy_explosion_list.append([x_enemy, y_enemy])
                index_b.append(bullet_list.index(b))
                index_e.append(enemy.index(e))
                Score += 400 + round(y_enemy)
    try:
        for item in index_b:
            del bullet_list[item]
        for item in index_e:
            del enemy[item]
    except:
        pass
    return Score


# lives


def show_lives(Lives, main_screen):
    global lives, max_x, max_y
    for item in range(1, Lives+1):
        main_screen.blit(lives, (max_x-(item*55), 10))

# missiles


def show_missiles(Missiles, main_screen):
    global missiles_pic, max_x, max_y
    for item in range(1, Missiles+1):
        main_screen.blit(missiles_pic, (max_x-(item*55), 70))


def use_missile(enemy, Missiles, Score):
    global missile_sound, main_screen, enemy_explosion_list
    Score += R.randint(200, 300)*len(enemy)
    enemy.clear()
    enemy_explosion_list.clear()
    missile_sound.play()
    main_screen.blit(missiles_pic, (max_x//2, max_y//2))
    return Missiles - 1, True, Score
