import pygame, random

#### Inicializace
pygame.init()
screen_sizes = (1100, 600)
screen = pygame.display.set_mode(screen_sizes)
pygame.display.set_caption("Hunting Game")
favicon = pygame.image.load("images/favicon.png")
pygame.display.set_icon(favicon)

#### Definování
### In-game
score = 0
lives = 3
time = 120
goal = 15

target_pos = (random.randint(32, screen_sizes[0]-32), random.randint(89, screen_sizes[1]-32))
bomb1_pos = (random.randint(32, screen_sizes[0]-32), random.randint(89, screen_sizes[1]-32))
bomb1_pos = (random.randint(32, screen_sizes[0]-32), random.randint(89, screen_sizes[1]-32))
bomb1_pos = (random.randint(32, screen_sizes[0]-32), random.randint(89, screen_sizes[1]-32))

### Technické
## Čas, délky a velikosti
fps = 60
clock = pygame.time.Clock()

## Barvy
black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)
gold = pygame.Color("#ffd700")
background = pygame.Color("#cfccb5")

## Média
# obrázky
favicon_rect = favicon.get_rect()
favicon_rect.topleft = (15, 15)

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

heart2_image = pygame.image.load("images/heart.png")
heart2_image_rect = character_image.get_rect()

heart3_image = pygame.image.load("images/heart.png")
heart3_image_rect = character_image.get_rect()

heart_empty1_image = pygame.image.load("images/heart-empty.png")
heart_empty1_image_rect = character_image.get_rect()

heart_empty2_image = pygame.image.load("images/heart-empty.png")
heart_empty2_image_rect = character_image.get_rect()

heart_empty3_image = pygame.image.load("images/heart-empty.png")
heart_empty3_image_rect = character_image.get_rect()

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

# texty

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
