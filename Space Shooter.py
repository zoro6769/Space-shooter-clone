import pygame
import random
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Space shooter!")

clock = pygame.time.Clock()

background = pygame.image.load('images/space.png').convert()
background1 = pygame.transform.scale(background, (1000, 700))

player = pygame.image.load('images/Space ship.png').convert_alpha()
player1 = pygame.transform.scale(player, (75, 100))
player_rect = player1.get_rect(midbottom = (500, 700))

enemies = []

enemy_surface = pygame.image.load('images/enemy.png').convert_alpha()
enemy1 = pygame.transform.scale(enemy_surface, (75, 75))

text = pygame.font.Font('Font/cursive.ttf', 50)

background2 = pygame.image.load('images/gameover.png')
background3 = pygame.transform.scale(background2, (1000, 700))

background_ = pygame.image.load('images/youwin.png')
backgroundyouwin = pygame.transform.scale(background_, (1000, 700))


for row in range(3):
    for col in range(8):
        enemies.append(
            enemy1.get_rect(
                topleft = (
                    100 + col * 100,
                    50 + row*100 
                )
            )
        )

lasers = []

enemy_lasers = []

gameover = False


while True:

    screen.blit(background1, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and not gameover:
            if event.key == pygame.K_SPACE:
                lasers.append(
                    pygame.Rect(
                        player_rect.centerx - 2,
                        player_rect.top,
                        5,
                        15
                )
            )
        
    if gameover == True:
        screen.blit(background3, (0, 0))
        title = text.render("GAME OVER", True, "Red")
        screen.blit(title, (350, 350))
        pygame.display.update()
        clock.tick(60)
        continue
        
    for laser in lasers:
        laser.y -= 10
    for laser in lasers:
        pygame.draw.rect(screen, "red", laser)

    lasers = [laser for laser in lasers if laser.bottom > 0]

    for laser in lasers[:]:
        for enemy in enemies[:]:
            if laser.colliderect(enemy):
                enemies.remove(enemy)
                lasers.remove(laser)
                break
   
    screen.blit(player1, player_rect)
    
    for enemy in enemies:
        screen.blit(enemy1, enemy)

    key = pygame.key.get_pressed()

    if key[pygame.K_RIGHT]:
        player_rect.right += 5

    elif key[pygame.K_LEFT]:
        player_rect.left -= 5 

    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > 1000:
        player_rect.right = 1000

    if random.randint(1, 60) == 1 and enemies:
        shooter = random.choice(enemies)

        enemy_lasers.append(
            pygame.Rect(
                shooter.centerx,
                shooter.bottom,
                15,
                5
            )
        )

    for enemy_laser in enemy_lasers:
        enemy_laser.y += 5
    for enemy_laser in enemy_lasers:
        pygame.draw.rect(screen, "orange", enemy_laser)

    enemy_lasers = [enemy_laser for enemy_laser in enemy_lasers if enemy_laser.bottom > 0]

    for enemy in enemies[:]:
        for enemy_laser in enemy_lasers[:]:
            if enemy_laser.colliderect(player_rect):
                enemy_lasers.remove(enemy_laser)
                gameover = True
                break

    if len(enemies) == 0:
        screen.blit(backgroundyouwin, (0, 0))
        win = text.render("YOU WIN", True, "green")
        screen.blit(win, (350, 350))
        pygame.display.update()
        clock.tick(60)
        continue
                
                
    
    pygame.display.update()
    clock.tick(60)