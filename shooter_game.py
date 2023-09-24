from typing import Any
import pygame
from time import time
from random import randint
width = 1300
height = 600
FPS = 60
score = 0
lost = 0
shots = 5
restart = False
pygame.mixer.init()
pygame.mixer.music.load("space.ogg")
pygame.mixer.music.play()
pygame.font.init()
font_stat = pygame.font.Font(None, 25)
font_stat1 = pygame.font.Font(None, 15)
text_score = font_stat.render('Рахунок: ' + str(score), True, (255, 255, 255))
text_lost = font_stat.render('Пропущено: ' + str(lost), True, (255, 255, 255))
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
game_over = False
finish = True
menu = True
pygame.display.set_caption("Автор Шутера:")
bullets = pygame.sprite.Group()
bg = pygame.transform.scale(pygame.image.load("galaxy.jpg"), (width, height))
easydiffinfo = pygame.transform.scale(pygame.image.load("easydifficultyinfo.png"), (64, 64))
mediumdiffinfo = pygame.transform.scale(pygame.image.load("mediumdifficultyinfo.png"), (64, 64))
harddiffinfo = pygame.transform.scale(pygame.image.load("harddifficultyinfo.png"), (64, 64))
endlessmodeinfo = pygame.transform.scale(pygame.image.load("endlessmodeinfo.png"), (64, 64))
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed, size):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.size = size
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
    def fire(self):
        new_bullet = Bullet("bullet.png", self.rect.x, self.rect.top, 8, (15,30))
        bullets.add(new_bullet)
        fire_sound = pygame.mixer.Sound("fire.ogg")
        fire_sound.play()
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > height:
            self.rect.y = 0
            self.rect.x = randint(10, width-70)
            self.speed = randint(3, 6)
            global lost
            lost += 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
player = Player('rocket.png', width/2, height-70, 4, (20, 20))
enemies = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
reload_time = False
while not game_over:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_over = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                if shots > 0 and not reload_time:
                    player.fire()
                    shots -= 1
                elif shots <= 0 and not reload_time:
                    last_time = time()
                    reload_time = True
            if e.key == pygame.K_r:
                    restart = True
        if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if 600 <= x < 664 and 200 <= y < 264:
                    menu = False
                    finish = False
                    difficulty = 1
                    enemy_num = 4
                    asteroid_num = 2
                    lives = 3
                    for i in range(enemy_num):
                        new_enemy = Enemy("ufo.png", randint(10, width-70), 0, randint(3, 6), (60, 65))
                        enemies.add(new_enemy)
                    for i in range(asteroid_num):
                        new_asteroid = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
                        asteroids.add(new_asteroid)
                elif 600 <= x < 664 and 264 <= y < 328:
                    menu = False
                    finish = False
                    difficulty = 2
                    enemy_num = 6
                    asteroid_num = 3
                    lives = 2
                    for i in range(enemy_num):
                        new_enemy = Enemy("ufo.png", randint(10, width-70), 0, randint(3, 6), (60, 65))
                        enemies.add(new_enemy)
                    for i in range(asteroid_num):
                        new_asteroid = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
                        asteroids.add(new_asteroid)
                elif 664 <= x < 728 and 200 <= y < 264:
                    menu = False
                    finish = False
                    difficulty = 3
                    enemy_num = 8
                    asteroid_num = 4
                    lives = 1
                    for i in range(enemy_num):
                        new_enemy = Enemy("ufo.png", randint(10, width-70), 0, randint(3, 6), (60, 65))
                        enemies.add(new_enemy)
                    for i in range(asteroid_num):
                        new_asteroid = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
                        asteroids.add(new_asteroid)
                elif 664 <= x < 728 and 264 <= y < 328:
                    menu = False
                    finish = False
                    difficulty = 4
                    enemy_num = 12
                    asteroid_num = 6
                    lives = 1
                    for i in range(enemy_num):
                        new_enemy = Enemy("ufo.png", randint(10, width-70), 0, randint(3, 6), (60, 65))
                        enemies.add(new_enemy)
                    for i in range(asteroid_num):
                        new_asteroid = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
                        asteroids.add(new_asteroid)
    if menu is True and finish is True:
        window.blit(bg, (0, 0))
        window.blit(easydiffinfo, (600, 200))
        window.blit(mediumdiffinfo, (600, 264))
        window.blit(harddiffinfo, (664, 200))
        window.blit(endlessmodeinfo, (664, 264))
    if restart and difficulty == 1:
        for e in enemies:
            e.kill()
        for b in bullets:
            b.kill()
        for a in asteroids:
            a.kill()
        lost = 0
        score = 0
        lives = 3
        shots = 5
        enemy_num = 4
        asteroid_num = 2
        reload_time = False
        player.rect.x = width/2
        for i in range(enemy_num):
            new_enemy = Enemy("ufo.png", randint(10, width-70), 0, randint(3, 6), (60, 65))
            enemies.add(new_enemy)
        for i in range(asteroid_num):
            new_asteroid = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
            asteroids.add(new_asteroid)
        restart = False
        finish = False
    elif restart and difficulty == 2:
        for e in enemies:
            e.kill()
        for b in bullets:
            b.kill()
        for a in asteroids:
            a.kill()
        lost = 0
        score = 0
        lives = 2
        shots = 5
        enemy_num = 6
        asteroid_num = 3
        reload_time = False
        player.rect.x = width/2
        for i in range(enemy_num):
            new_enemy = Enemy("ufo.png", randint(10, width-70), 0, randint(3, 6), (60, 65))
            enemies.add(new_enemy)
        for i in range(asteroid_num):
            new_asteroid = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
            asteroids.add(new_asteroid)
        restart = False
        finish = False
    elif restart and difficulty == 3:
        for e in enemies:
            e.kill()
        for b in bullets:
            b.kill()
        for a in asteroids:
            a.kill()
        lost = 0
        score = 0
        lives = 1
        shots = 5
        enemy_num = 8
        asteroid_num = 4
        reload_time = False
        player.rect.x = width/2
        for i in range(enemy_num):
            new_enemy = Enemy("ufo.png", randint(10, width-70), 0, randint(3, 6), (60, 65))
            enemies.add(new_enemy)
        for i in range(asteroid_num):
            new_asteroid = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
            asteroids.add(new_asteroid)
        restart = False
        finish = False
    elif restart and difficulty == 4:
        for e in enemies:
            e.kill()
        for b in bullets:
            b.kill()
        for a in asteroids:
            a.kill()
        lost = 0
        score = 0
        lives = 1
        shots = 5
        enemy_num = 12
        asteroid_num = 6
        reload_time = False
        player.rect.x = width/2
        for i in range(enemy_num):
            new_enemy = Enemy("ufo.png", randint(10, width-70), 0, randint(4, 7), (60, 65))
            enemies.add(new_enemy)
        for i in range(asteroid_num):
            new_asteroid = Enemy("asteroid.png", randint(10, width-70), 0, randint(2, 4), (60, 65))
            asteroids.add(new_asteroid)
        restart = False
        finish = False
    if not finish and difficulty == 1:
        window.blit(bg, (0, 0))
        text_score = font_stat.render('Рахунок: ' + str(score), True, (255, 255, 255))
        text_lost = font_stat.render('Пропущено: ' + str(lost), True, (255, 255, 255))
        text_lives = font_stat.render('Кількість життів: ' + str(lives), True, (255, 255, 255))
        window.blit(text_score, (20, 20))
        window.blit(text_lost, (20, 50))
        window.blit(text_lives, (20, 80))
        player.update()
        player.reset()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_m]:
            finish = True
            menu = True
            for e in enemies:
                e.kill()
            for b in bullets:
                b.kill()
            for a in asteroids:
                a.kill()
        if reload_time:
            cur_time = time()
            if cur_time - last_time >= 1.5:
                shots = 5
                reload_time = False
            else:
                wait_text = font_stat1.render('Зачекай! Зараз йде перезарядка', True, (255, 0, 0))
                window.blit(wait_text, (550, 300))
        enemies.update()
        enemies.draw(window)
        asteroids.update()
        asteroids.draw(window)
        bullets.update()
        bullets.draw(window)
        if pygame.sprite.groupcollide(bullets, enemies, True, True):
            score += 1
            new_enemy1 = Enemy("ufo.png", randint(10, width-70), 0, randint(3, 6), (60, 65))
            enemies.add(new_enemy1)
        if pygame.sprite.groupcollide(bullets, asteroids, True, True):
            new_asteroid = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
            new_asteroid1 = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
            asteroids.add(new_asteroid)
            asteroids.add(new_asteroid1)
        if score >= 10 and lost < 20:
            text_win = font_stat.render('ТИ ВИГРАВ! Натисни на r щоб почати заново', True, (0, 255, 0))
            window.blit(text_win, (550, 300))
            finish = True
        elif lost >= 20 and score < 10:
            text_lose = font_stat.render('Ти програв :(', True, (255, 0, 0))
            window.blit(text_lose, (550, 300))
            finish = True
        elif pygame.sprite.spritecollide(player, enemies, True):
            lives -= 1
        elif pygame.sprite.spritecollide(player, asteroids, True):
            lives -= 1
        if lives <= 0:
            finish = True
            text_lose = font_stat.render('Ти програв :(', True, (255, 0, 0))
            window.blit(text_lose, (550, 300))
    if not finish and difficulty == 2:
        window.blit(bg, (0, 0))
        text_score = font_stat.render('Рахунок: ' + str(score), True, (255, 255, 255))
        text_lost = font_stat.render('Пропущено: ' + str(lost), True, (255, 255, 255))
        text_lives = font_stat.render('Кількість життів: ' + str(lives), True, (255, 255, 255))
        window.blit(text_score, (20, 20))
        window.blit(text_lost, (20, 50))
        window.blit(text_lives, (20, 80))
        player.update()
        player.reset()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_m]:
            finish = True
            menu = True
            for e in enemies:
                e.kill()
            for b in bullets:
                b.kill()
            for a in asteroids:
                a.kill()
        if reload_time:
            cur_time = time()
            if cur_time - last_time >= 2:
                shots = 5
                reload_time = False
            else:
                wait_text = font_stat1.render('Зачекай! Зараз йде перезарядка', True, (255, 0, 0))
                window.blit(wait_text, (550, 300))
        enemies.update()
        enemies.draw(window)
        asteroids.update()
        asteroids.draw(window)
        bullets.update()
        bullets.draw(window)
        if pygame.sprite.groupcollide(bullets, enemies, True, True):
            score += 1
            new_enemy1 = Enemy("ufo.png", randint(10, width-70), 0, randint(3, 6), (60, 65))
            enemies.add(new_enemy1)
        if pygame.sprite.groupcollide(bullets, asteroids, True, True):
            new_asteroid = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
            new_asteroid1 = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
            asteroids.add(new_asteroid)
            asteroids.add(new_asteroid1)
        if score >= 10 and lost < 18:
            text_win = font_stat.render('ТИ ВИГРАВ! Натисни на r щоб почати заново', True, (0, 255, 0))
            window.blit(text_win, (550, 300))
            finish = True
        elif lost >= 18 and score < 10:
            text_lose = font_stat.render('Ти програв :(', True, (255, 0, 0))
            window.blit(text_lose, (550, 300))
            finish = True
        elif pygame.sprite.spritecollide(player, enemies, True):
            lives -= 1
        elif pygame.sprite.spritecollide(player, asteroids, True):
            lives -= 1
        if lives <= 0:
            finish = True
            text_lose = font_stat.render('Ти програв :(', True, (255, 0, 0))
            window.blit(text_lose, (550, 300))
    if not finish and difficulty == 3:
        window.blit(bg, (0, 0))
        text_score = font_stat.render('Рахунок: ' + str(score), True, (255, 255, 255))
        text_lost = font_stat.render('Пропущено: ' + str(lost), True, (255, 255, 255))
        text_lives = font_stat.render('Кількість життів: ' + str(lives), True, (255, 255, 255))
        window.blit(text_score, (20, 20))
        window.blit(text_lost, (20, 50))
        window.blit(text_lives, (20, 80))
        player.update()
        player.reset()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_m]:
            finish = True
            menu = True
            for e in enemies:
                e.kill()
            for b in bullets:
                b.kill()
            for a in asteroids:
                a.kill()
        if reload_time:
            cur_time = time()
            if cur_time - last_time >= 2.5:
                shots = 5
                reload_time = False
            else:
                wait_text = font_stat1.render('Зачекай! Зараз йде перезарядка', True, (255, 0, 0))
                window.blit(wait_text, (550, 300))
        enemies.update()
        enemies.draw(window)
        asteroids.update()
        asteroids.draw(window)
        bullets.update()
        bullets.draw(window)
        if pygame.sprite.groupcollide(bullets, enemies, True, True):
            score += 1
            new_enemy1 = Enemy("ufo.png", randint(10, width-70), 0, randint(3, 6), (60, 65))
            enemies.add(new_enemy1)
        if pygame.sprite.groupcollide(bullets, asteroids, True, True):
            new_asteroid = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
            new_asteroid1 = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
            asteroids.add(new_asteroid)
            asteroids.add(new_asteroid1)
        if score >= 12 and lost < 15:
            text_win = font_stat.render('ТИ ВИГРАВ! Натисни на r щоб почати заново', True, (0, 255, 0))
            window.blit(text_win, (550, 300))
            finish = True
        elif lost >= 15 and score < 12:
            text_lose = font_stat.render('Ти програв :(', True, (255, 0, 0))
            window.blit(text_lose, (550, 300))
            finish = True
        elif pygame.sprite.spritecollide(player, enemies, True):
            lives -= 1
        elif pygame.sprite.spritecollide(player, asteroids, True):
            lives -= 1
        if lives <= 0:
            finish = True
            text_lose = font_stat.render('Ти програв :(', True, (255, 0, 0))
            window.blit(text_lose, (550, 300))
    if not finish and difficulty == 4:
        window.blit(bg, (0, 0))
        text_score = font_stat.render('Рахунок: ' + str(score), True, (255, 255, 255))
        text_lost = font_stat.render('Пропущено: ' + str(lost), True, (255, 255, 255))
        text_lives = font_stat.render('Кількість життів: ' + str(lives), True, (255, 255, 255))
        window.blit(text_score, (20, 20))
        window.blit(text_lost, (20, 50))
        window.blit(text_lives, (20, 80))
        player.update()
        player.reset()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_m]:
            finish = True
            menu = True
            for e in enemies:
                e.kill()
            for b in bullets:
                b.kill()
            for a in asteroids:
                a.kill()
        if reload_time:
            cur_time = time()
            if cur_time - last_time >= 3:
                shots = 5
                reload_time = False
            else:
                wait_text = font_stat1.render('Зачекай! Зараз йде перезарядка', True, (255, 0, 0))
                window.blit(wait_text, (550, 300))
        enemies.update()
        enemies.draw(window)
        asteroids.update()
        asteroids.draw(window)
        bullets.update()
        bullets.draw(window)
        if pygame.sprite.groupcollide(bullets, enemies, True, True):
            score += 1
            new_enemy1 = Enemy("ufo.png", randint(10, width-70), 0, randint(3, 6), (60, 65))
            enemies.add(new_enemy1)
        if pygame.sprite.groupcollide(bullets, asteroids, True, True):
            new_asteroid = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
            new_asteroid1 = Enemy("asteroid.png", randint(10, width-70), 0, randint(1, 3), (60, 65))
            asteroids.add(new_asteroid)
            asteroids.add(new_asteroid1)
        elif pygame.sprite.spritecollide(player, enemies, True):
            lives -= 1
        elif pygame.sprite.spritecollide(player, asteroids, True):
            lives -= 1
        if lives <= 0:
            finish = True
            text_end = font_stat.render('Ваш рахунок: ' + str(score), True, (255, 0, 0))
            window.blit(text_end, (550, 300))
    if finish:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game_over = True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    restart = True
    pygame.display.update()
    clock.tick(FPS)