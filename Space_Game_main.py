import pygame as P
import random as R
import time as T
from Space_Game_func import *
from Space_Game_var import *
P.mixer.music.play(-1)
enemy.append([enemy_pics[R.randint(0, len(enemy_pics)-1)], [R.randint(margin_x // 3, round(max_x-margin_x*1.3)), R.randint(50, 100)], R.random()*enemy_speed])
while True:
    # fps limit
    Frame.tick(80)
    Event = P.event.poll()
    # quit
    if Event.type == P.QUIT:
        hideLabel(text_game_over)
        hideLabel(text_mehrshad)
        if Lives == -1:
            updateDisplay()
            Lives -= 1
        P.mixer.music.pause()
        setBackgroundImage([".Images\Textures\stars_galaxy_bullured.jpg"])
        text_game_over = makeLabel("COME BACK!", 50, max_x//3-5, max_y//2-50, White, "Victor Mono")
        text_mehrshad = makeLabel("Designed By Mehrshad", 24, max_x//3+25, max_y//2+25, White)
        showLabel(text_game_over)
        showLabel(text_mehrshad)
        T.sleep(1.5)
        break
    # game over
    if Lives == 0:
        Pause = True
        P.mixer.music.pause()
        text_game_over = makeLabel("GAME OVER!", 50, max_x//3-5, max_y//2-50, White, "Victor Mono")
        text_mehrshad = makeLabel("Designed By Mehrshad", 24, max_x//3+25, max_y//2+25, White)
        setBackgroundImage([".Images\Textures\stars_galaxy_bullured.jpg"])
        showLabel(text_game_over)
        showLabel(text_mehrshad)
        updateDisplay()
        Lives -= 1
    if not Pause:
        P.mixer.music.unpause()
        scrollBackground(0, bg_scroll_speed)
        # timing
        if P.time.get_ticks() % 7000 == 0:
            bg_scroll_speed += 1
        if P.time.get_ticks() % Missile_explosion_delay == 0 and Missile_boom == True:
            Score += len(enemy) * R.randint(2, 3)
            Missile_boom = False
        if P.time.get_ticks() % enemy_explosion_delay == 0 and enemy_explosion_list != []:
            enemy_explosion_list.clear()
        if P.time.get_ticks() % enemy_appear_time == 0:
            enemy.append([enemy_pics[R.randint(0, len(enemy_pics)-1)], [R.randint(margin_x // 3, round(max_x-margin_x*1.3)), R.randint(50, 100)], R.randint(7, 10)*enemy_speed])
            if enemy_appear_time > 25:
                enemy_appear_time -= 1  # enable for getting more challenge by time
        # control with mouse
        if Event.type == P.MOUSEMOTION:
            ship_x = Event.pos[0]-bullet_scale
        if Event.type == P.MOUSEBUTTONDOWN:
            shoot_bullet(ship_x, ship_y, True)
        # control with keyboard
        if Event.type == P.KEYDOWN:
            if Event.key == P.K_RIGHT or Event.key == P.K_d:
                ship_x_change = ship_change_by_key
            if Event.key == P.K_LEFT or Event.key == P.K_a:
                ship_x_change = -ship_change_by_key
            if Event.key == P.K_SPACE:
                shoot_bullet(ship_x, ship_y, True)
            if Event.key == P.K_m:
                Missiles, Missile_boom, Score = use_missile(enemy, Missiles, Score)
        if Event.type == P.KEYUP:
            if Event.key == P.K_LEFT or Event.key == P.K_RIGHT or Event.key == P.K_d or Event.key == P.K_a:
                ship_x_change = 0
        ship_x += ship_x_change
    if Event.type == P.KEYDOWN and Event.key == P.K_p and Lives > 0:
        Pause = not Pause
        if Pause:
            setBackgroundImage([".Images\Textures\stars_galaxy_bullured.jpg"])
            P.mixer.music.pause()
        else:
            setBackgroundImage([".Images\Textures\stars_galaxy.jpg"])
    # main_screen updates
    if Lives > 0:
        if Missile_cost <= Score:
            if Missile_limit > Missiles:
                Missiles += 1
            Missile_cost *= 1.3
        if Life_cost <= Score:
            if Lives_limit > Lives:
                Lives += 1
            Life_cost *= 1.3
        if ship_x >= round(max_x-margin_x*1.3):
            ship_x = round(max_x-margin_x*1.3)
        if ship_x <= margin_x // 3:
            ship_x = margin_x // 3
        Lives = enemy_manage(enemy, main_screen, Pause, Lives)
        Score = enemy_crash(Score)
        bullet_manage(bullet_list, main_screen, bullet, bullet_speed, Pause)
        # bullet_manage(enemy_bullet_list, main_screen, bullet, enemy_bullet_speed, Pause)
        text_level = Font1.render(f'Level: {Level}', True, White)
        text_score = Font1.render(f'Score: {Score}', True, White)
        if enemy_explosion_list != []:
            enemy_explosion_manage(enemy_explosion_list)
        if Missile_boom:
            main_screen.blit(Missile_using_pic, (0, 0))
        if Pause:
            main_screen.blit(text_pause, (max_x//3+40, 10))
        show_lives(Lives, main_screen)
        show_missiles(Missiles, main_screen)
        main_screen.blit(ship, (ship_x, ship_y))
        main_screen.blit(text_score, (10, 10))
        main_screen.blit(text_mehrshad, (max_x//2-75, max_y-25))
        updateDisplay()
P.quit()
