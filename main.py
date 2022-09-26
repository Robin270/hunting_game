import pygame, random, functions
from functions import *

#### Inicializace
pygame.init()
screen_sizes = (1200, 650)
screen = pygame.display.set_mode(screen_sizes)
pygame.display.set_caption("Hunting Game")
favicon = pygame.image.load("images/favicon.png")
pygame.display.set_icon(favicon)

#### Definování
### In-game
score = 0
goal = 15
lives = 3
heart1 = True
heart2 = True
heart3 = True
time = 120

# target_pos = (random.randint(32, screen_sizes[0]-32), random.randint(89, screen_sizes[1]-32))
# bomb1_pos = (random.randint(32, screen_sizes[0]-32), random.randint(89, screen_sizes[1]-32))
# bomb1_pos = (random.randint(32, screen_sizes[0]-32), random.randint(89, screen_sizes[1]-32))
# bomb1_pos = (random.randint(32, screen_sizes[0]-32), random.randint(89, screen_sizes[1]-32))

### Technické
## Čas, délky a velikosti
fps = 60
clock = pygame.time.Clock()

## Barvy
black = (0, 0, 0)
white = (255, 255, 255)
gray = (130, 130, 130)
light_green = pygame.Color("#90ee90")
cream = pygame.Color("#fcf5ca")
gold = pygame.Color("#ffd700")
background = pygame.Color("#cfccb5")

## Média
# obrázky
favicon_medium = pygame.image.load("images/favicon-medium.png")
favicon_medium_rect = favicon_medium.get_rect()
favicon_medium_rect.topleft = (10, 6)

character_image = pygame.image.load("images/character.png")
character_image_rect = character_image.get_rect()
character_image_rect.center = (screen_sizes[0]//2, screen_sizes[1]//2)

target_image = pygame.image.load("images/target.png")
target_image_rect = target_image.get_rect()
target_image_rect.center = target_pos

bomb1_image = pygame.image.load("images/bomb.png")
bomb1_image_rect = character_image.get_rect()

bomb2_image = pygame.image.load("images/bomb.png")
bomb2_image_rect = character_image.get_rect()

bomb3_image = pygame.image.load("images/bomb.png")
bomb3_image_rect = character_image.get_rect()

npc_image = pygame.image.load("images/npc.png")
npc_image_rect = character_image.get_rect()

heart1_image = pygame.image.load("images/heart.png")
heart1_image_rect = character_image.get_rect()
heart1_image_rect.topleft = (80, 68)

heart2_image = pygame.image.load("images/heart.png")
heart2_image_rect = character_image.get_rect()
heart2_image_rect.topleft = (112, 68)

heart3_image = pygame.image.load("images/heart.png")
heart3_image_rect = character_image.get_rect()
heart3_image_rect.topleft = (144, 68)

heart_empty1_image = pygame.image.load("images/heart-empty.png")
heart_empty1_image_rect = character_image.get_rect()
heart_empty1_image_rect.topleft = (80, 68)

heart_empty2_image = pygame.image.load("images/heart-empty.png")
heart_empty2_image_rect = character_image.get_rect()
heart_empty2_image_rect.topleft = (112, 68)

heart_empty3_image = pygame.image.load("images/heart-empty.png")
heart_empty3_image_rect = character_image.get_rect()
heart_empty3_image_rect.topleft = (144, 68)

# zvuky
pygame.mixer.music.load("media/music.wav")
pygame.mixer.music.set_volume(.16)
pygame.mixer.music.play(-1, .0)

collect_sound = pygame.mixer.Sound("media/collect.wav")
collect_sound.set_volume(.3)

win_sound = pygame.mixer.Sound("media/win.wav")
win_sound.set_volume(.3)

boom_sound = pygame.mixer.Sound("media/boom.wav")
boom_sound.set_volume(.3)

hit_sound = pygame.mixer.Sound("media/hit.wav")
hit_sound.set_volume(.3)

loose_sound = pygame.mixer.Sound("media/loose.wav")
loose_sound.set_volume(.3)

npc_sound = pygame.mixer.Sound("media/npc.wav")
npc_sound.set_volume(.3)

## Písmo
# fonty
heading_font = pygame.font.SysFont("arial", 38, True)
bar_font = pygame.font.SysFont("kokila", 30)

# texty
game_name_text = heading_font.render("Hunting Game", True, gold)
game_name_text_rect = game_name_text.get_rect()
game_name_text_rect.topleft = (57, 5)

timer_text = heading_font.render(f"Timer: {time_to_minutes(time)}", True, gold)
timer_text_rect = game_name_text.get_rect()
timer_text_rect.topleft = (490, 5)

score_text = heading_font.render(f"Score: {score}", True, gold)
score_text_rect = game_name_text.get_rect()
score_text_rect.topleft = (960, 5)

#### Hlavní herní cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
            quit_game = True
    ### Zachycování eventů
        ## Pomocí event


    ## Mimo event
    if pygame.key.get_pressed()[pygame.K_UP] and character_image_rect.top > 84:
        character_image_rect.y -= 5
    elif pygame.key.get_pressed()[pygame.K_DOWN] and character_image_rect.bottom < screen_sizes[1]:
        character_image_rect.y += 5
    elif pygame.key.get_pressed()[pygame.K_LEFT] and character_image_rect.left > 0:
        character_image_rect.x -= 5
    elif pygame.key.get_pressed()[pygame.K_RIGHT] and character_image_rect.right < screen_sizes[0]:
        character_image_rect.x += 5
    
    if character_image_rect.colliderect(target_image_rect):
        score += 1
        collect_sound.play()
        if score == goal:
            break
        target_pos = (random.randint(32, screen_sizes[0]-32), random.randint(89, screen_sizes[1]-32))
        target_image_rect.center = target_pos

    ### Periodické renderování
    screen.fill(background)
    pygame.draw.rect(screen, gray, (0, 0, screen_sizes[0], 70))
    pygame.draw.rect(screen, cream, (0, 55, screen_sizes[0], 45))
    screen.blit(favicon_medium, favicon_medium_rect)
    screen.blit(game_name_text, game_name_text_rect)
    screen.blit(timer_text, timer_text_rect)
    screen.blit(score_text, score_text_rect)

    if heart1:
        screen.blit(heart1_image, heart1_image_rect)
    else:
        screen.blit(heart_empty1_image, heart_empty1_image_rect)
    if heart2:
        screen.blit(heart2_image, heart2_image_rect)
    else:
        screen.blit(heart_empty2_image, heart_empty2_image_rect)
    if heart3:
        screen.blit(heart3_image, heart3_image_rect)
    else:
        screen.blit(heart_empty3_image, heart_empty3_image_rect)
    
    pygame.draw.rect(screen, gray, (350, 68, 800, 20))
    pygame.draw.rect(screen, light_green, (360, 73, 780, 10))


    ## Update
    pygame.display.update()
    clock.tick(fps)

## Konec hry
if not lets_continue:
    pygame.quit()
else:
    pygame.mixer.music.stop()
    win_sound.play()
    screen.fill(background)
    
    while lets_continue:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lets_continue = False
pygame.quit()
