import pygame, math, random, functions
from functions import *

#### Inicializace
pygame.init()
screen_sizes = (1200, 650)
screen = pygame.display.set_mode(screen_sizes)
pygame.display.set_caption("Hunting Game (Beta 0.3.0)")
favicon = pygame.image.load("images/favicon.png")
pygame.display.set_icon(favicon)

#### Definování
### In-game
score = 0
goal = 25
lives = 3
hearts = [True, True, True]
npc_direction = "topleft"
time = 80
boost = 400
regen_seed = 1600
is_regen_rendered = False
regen_timer = 0
regen_warning = False
regen_warning_timer = 0
regen_warning_counter = 0
win = False
message = None
character_spawn = (screen_sizes[0]//2, screen_sizes[1]//2)
npc_spawn = (screen_sizes[0]//2-90, screen_sizes[1]//2-70)
npc_step_y = random.randint(2, 6)
npc_step_x = random.randint(2, 6)
character_speed = 5
target_pos = random_pos(28, screen_sizes[0], screen_sizes[1], character_spawn)
default_regen_pos = (-1000, -1000)
regen_pos = default_regen_pos
bomb1_pos = random_pos(46, screen_sizes[0], screen_sizes[1], character_spawn, target_pos)
bomb2_pos = random_pos(46, screen_sizes[0], screen_sizes[1], character_spawn, target_pos)
bomb3_pos = random_pos(46, screen_sizes[0], screen_sizes[1], character_spawn, target_pos)

### Technické
## Čas, délky a velikosti
fps = 60
time_counter = 0
clock = pygame.time.Clock()

## Barvy
black = (0, 0, 0)
white = (255, 255, 255)
gray = (130, 130, 130)
light_green = pygame.Color("#90ee90")
light_green2 = pygame.Color("#94ffbf")
light_red = pygame.Color("#ffa1b6")
cream = pygame.Color("#fcf5ca")
gold = pygame.Color("#ffd700")

background = pygame.Color("#cfccb5")
boost_bar_color = light_green

## Média
# obrázky
favicon_medium = pygame.image.load("images/favicon-medium.png")
favicon_medium_rect = favicon_medium.get_rect()
favicon_medium_rect.topleft = (10, 6)

character_image = pygame.image.load("images/character.png")
character_image_rect = character_image.get_rect()
character_image_rect.center = character_spawn

target_image = pygame.image.load("images/target.png")
target_image_rect = target_image.get_rect()
target_image_rect.center = target_pos

bomb1_image = pygame.image.load("images/bomb.png")
bomb1_image_rect = character_image.get_rect()
bomb1_image_rect.center = bomb1_pos

bomb2_image = pygame.image.load("images/bomb.png")
bomb2_image_rect = character_image.get_rect()
bomb2_image_rect.center = bomb2_pos

bomb3_image = pygame.image.load("images/bomb.png")
bomb3_image_rect = character_image.get_rect()
bomb3_image_rect.center = bomb3_pos

npc_image = pygame.image.load("images/npc.png")
npc_image_rect = character_image.get_rect()
npc_image_rect.center = npc_spawn

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

heart_regen_image = pygame.image.load("images/heart-regen.png")
heart_regen_image_rect = heart_regen_image.get_rect()
heart_regen_image_rect.center = default_regen_pos

heart_regen_light_image = pygame.image.load("images/heart-regen-light.png")
heart_regen_light_image_rect = heart_regen_light_image.get_rect()
heart_regen_light_image_rect.center = default_regen_pos

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

npc_wall_sound = pygame.mixer.Sound("media/npc_wall.wav")
npc_wall_sound.set_volume(.3)

regen_sound = pygame.mixer.Sound("media/regen.wav")
regen_sound.set_volume(.3)

regen_warning_sound = pygame.mixer.Sound("media/regen_warning.wav")
regen_warning_sound.set_volume(.3)

clock_tick_sound = pygame.mixer.Sound("media/clock_tick.wav")
clock_tick_sound.set_volume(1.9)

sprint_sound = pygame.mixer.Sound("media/sprint.wav")
sprint_sound.set_volume(.2)

## Písmo
# fonty
heading_font = pygame.font.SysFont("arial", 38, True)
final_font = pygame.font.SysFont("kokila", 64, True)

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
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        if boost > 0:
            if sprint_sound.get_num_channels() == 0:
                sprint_sound.play()
            boost_bar_color = light_green2
            boost -= 3
            character_speed = 9
        else:
            sprint_sound.stop()
            boost_bar_color = light_green
            character_speed = 5
    else:
        sprint_sound.stop()
        boost_bar_color = light_green
        character_speed = 5
        if boost < 400:
            boost += 1
    diagonal_speed_modifier = character_speed-math.sqrt(character_speed**2/2)
    if pygame.key.get_pressed()[pygame.K_UP] and character_image_rect.top > 100:
        if pygame.key.get_pressed()[pygame.K_LEFT] and character_image_rect.left > 0:
            character_image_rect.x -= character_speed-diagonal_speed_modifier
            character_image_rect.y -= character_speed-diagonal_speed_modifier
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and character_image_rect.right < screen_sizes[0]:
            character_image_rect.x += character_speed-diagonal_speed_modifier
            character_image_rect.y -= character_speed-diagonal_speed_modifier
        elif pygame.key.get_pressed()[pygame.K_DOWN] and character_image_rect.bottom < screen_sizes[1]:
            pass
        else:
            character_image_rect.y -= character_speed
    elif pygame.key.get_pressed()[pygame.K_DOWN] and character_image_rect.bottom < screen_sizes[1]:
        if pygame.key.get_pressed()[pygame.K_LEFT] and character_image_rect.left > 0:
            character_image_rect.x -= character_speed-diagonal_speed_modifier
            character_image_rect.y += character_speed-diagonal_speed_modifier
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and character_image_rect.right < screen_sizes[0]:
            character_image_rect.x += character_speed-diagonal_speed_modifier
            character_image_rect.y += character_speed-diagonal_speed_modifier
        elif pygame.key.get_pressed()[pygame.K_UP] and character_image_rect.top > 100:
            pass
        else:
            character_image_rect.y += character_speed
    elif pygame.key.get_pressed()[pygame.K_LEFT] and character_image_rect.left > 0:
        if pygame.key.get_pressed()[pygame.K_UP] and character_image_rect.top > 100:
            character_image_rect.y -= character_speed-diagonal_speed_modifier
            character_image_rect.x -= character_speed-diagonal_speed_modifier
        elif pygame.key.get_pressed()[pygame.K_DOWN] and character_image_rect.bottom < screen_sizes[1]:
            character_image_rect.y += character_speed-diagonal_speed_modifier
            character_image_rect.x -= character_speed-diagonal_speed_modifier
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and character_image_rect.right < screen_sizes[0]:
            pass
        else:
            character_image_rect.x -= character_speed
    elif pygame.key.get_pressed()[pygame.K_RIGHT] and character_image_rect.right < screen_sizes[0]:
        if pygame.key.get_pressed()[pygame.K_UP] and character_image_rect.top > 100:
            character_image_rect.y -= character_speed-diagonal_speed_modifier
            character_image_rect.x += character_speed-diagonal_speed_modifier
        elif pygame.key.get_pressed()[pygame.K_DOWN] and character_image_rect.bottom < screen_sizes[1]:
            character_image_rect.y += character_speed-diagonal_speed_modifier
            character_image_rect.x += character_speed-diagonal_speed_modifier
        elif pygame.key.get_pressed()[pygame.K_LEFT] and character_image_rect.left > 0:
            pass
        else:
            character_image_rect.x += character_speed

    if character_image_rect.colliderect(target_image_rect):
        score += 1
        collect_sound.play()
        if score == goal:
            win = True
            message = "Vyhráli jste!"
            break
        target_pos = random_pos(28, screen_sizes[0], screen_sizes[1], character_image_rect.center)
        bomb1_pos = random_pos(46, screen_sizes[0], screen_sizes[1], character_image_rect.center, target_pos)
        bomb2_pos = random_pos(46, screen_sizes[0], screen_sizes[1], character_image_rect.center, target_pos)
        bomb3_pos = random_pos(46, screen_sizes[0], screen_sizes[1], character_image_rect.center, target_pos)
        target_image_rect.center = target_pos
        bomb1_image_rect.center = bomb1_pos
        bomb2_image_rect.center = bomb2_pos
        bomb3_image_rect.center = bomb3_pos
    if character_image_rect.colliderect(bomb1_image_rect):
        boom_sound.play()
        hit_sound.play()
        bomb1_pos = random_pos(46, screen_sizes[0], screen_sizes[1], character_image_rect.center, target_pos)
        bomb1_image_rect.center = bomb1_pos
        hearts = minusHeart(hearts)
    if character_image_rect.colliderect(bomb2_image_rect):
        boom_sound.play()
        hit_sound.play()
        bomb2_pos = random_pos(46, screen_sizes[0], screen_sizes[1], character_image_rect.center, target_pos)
        bomb2_image_rect.center = bomb2_pos
        hearts = minusHeart(hearts)
    if character_image_rect.colliderect(bomb3_image_rect):
        boom_sound.play()
        hit_sound.play()
        bomb3_pos = random_pos(46, screen_sizes[0], screen_sizes[1], character_image_rect.center, target_pos)
        bomb3_image_rect.center = bomb3_pos
        hearts = minusHeart(hearts)
    if character_image_rect.colliderect(npc_image_rect):
        npc_sound.play()
        hit_sound.play()
        npc_direction = "topleft"
        npc_spawn = random_pos(50, screen_sizes[0], screen_sizes[1], character_image_rect.center)
        npc_image_rect.topright = npc_spawn
        hearts = minusHeart(hearts)
    if character_image_rect.colliderect(heart_regen_image_rect) or character_image_rect.colliderect(heart_regen_light_image_rect):
        regen_sound.play()
        hearts = plusHeart(hearts)
        heart_regen_image_rect.center = default_regen_pos
        heart_regen_light_image_rect.center = default_regen_pos
        is_regen_rendered = False
    if not hearts[0]:
        message = "Umřeli jste!"
        break

    ### Periodické renderování
    screen.fill(background)
    pygame.draw.rect(screen, gray, (0, 0, screen_sizes[0], 70))
    pygame.draw.rect(screen, cream, (0, 55, screen_sizes[0], 45))
    screen.blit(favicon_medium, favicon_medium_rect)
    screen.blit(game_name_text, game_name_text_rect)
    timer_text = heading_font.render(f"Timer: {time_to_minutes(time)}", True, gold)
    score_text = heading_font.render(f"Score: {score}", True, gold)
    screen.blit(timer_text, timer_text_rect)
    screen.blit(score_text, score_text_rect)
    if hearts[0]:
        screen.blit(heart1_image, heart1_image_rect)
    else:
        screen.blit(heart_empty1_image, heart_empty1_image_rect)
    if hearts[1]:
        screen.blit(heart2_image, heart2_image_rect)
    else:
        screen.blit(heart_empty2_image, heart_empty2_image_rect)
    if hearts[2]:
        screen.blit(heart3_image, heart3_image_rect)
    else:
        screen.blit(heart_empty3_image, heart_empty3_image_rect)

    pygame.draw.rect(screen, gray, (775, 68, 410, 20), 0, 10)
    pygame.draw.rect(screen, boost_bar_color, (780, 73, boost, 10), 0, 10)

    if npc_direction == "topleft":
        if npc_image_rect.top > 100 and npc_image_rect.left > 0:
            npc_image_rect.top -= npc_step_y
            npc_image_rect.left -= npc_step_x
        if npc_image_rect.top <= 100 or npc_image_rect.left <= 0:
            npc_step_y = random.randint(2, 6)
            npc_step_x = random.randint(2, 6)
            npc_direction = "bottomleft"
            npc_wall_sound.play()
    elif npc_direction == "bottomleft":
        if npc_image_rect.bottom < screen_sizes[1] and npc_image_rect.left > 0:
            npc_image_rect.bottom += npc_step_y
            npc_image_rect.left -= npc_step_x
        if npc_image_rect.bottom >= screen_sizes[1] or npc_image_rect.left <= 0:
            npc_step_y = random.randint(2, 6)
            npc_step_x = random.randint(2, 6)
            npc_direction = "bottomright"
            npc_wall_sound.play()
    elif npc_direction == "bottomright":
        if npc_image_rect.bottom < screen_sizes[1] and npc_image_rect.right < screen_sizes[0]:
            npc_image_rect.bottom += npc_step_y
            npc_image_rect.left += npc_step_x
        if npc_image_rect.bottom >= screen_sizes[1] or npc_image_rect.left >= screen_sizes[0]:
            npc_step_y = random.randint(2, 6)
            npc_step_x = random.randint(2, 6)
            npc_direction = "topright"
            npc_wall_sound.play()
    elif npc_direction == "topright":
        if npc_image_rect.top > 100 and npc_image_rect.right < screen_sizes[0]:
            npc_image_rect.top -= npc_step_y
            npc_image_rect.right += npc_step_x
        if npc_image_rect.top <= 100 or npc_image_rect.right >= screen_sizes[0]:
            npc_step_y = random.randint(2, 6)
            npc_step_x = random.randint(2, 6)
            npc_direction = "topleft"
            npc_wall_sound.play()

    screen.blit(npc_image, npc_image_rect)
    screen.blit(bomb1_image, bomb1_image_rect)
    screen.blit(bomb2_image, bomb2_image_rect)
    screen.blit(bomb3_image, bomb3_image_rect)
    screen.blit(target_image, target_image_rect)
    screen.blit(character_image, character_image_rect)

    if not hearts[1]:
        regen_seed = 950
    elif not hearts[2]:
        regen_seed = 1600
    else:
        regen_seed = False
    if not is_regen_rendered and chance(regen_seed):
        is_regen_rendered = True
        regen_timer = 0
        regen_warning_counter = 0
        regen_warning_timer = 0
        regen_warning = False
        regen_pos = random_pos(60, screen_sizes[0], screen_sizes[1], character_image_rect.center)
        heart_regen_image_rect.center = regen_pos
        screen.blit(heart_regen_image, heart_regen_image_rect)
    elif is_regen_rendered:
        regen_timer += 1
        if regen_warning_counter == 4:
            is_regen_rendered = False
            heart_regen_image_rect.center = default_regen_pos
            heart_regen_light_image_rect.center = default_regen_pos
        elif regen_timer > 550:
            if regen_warning:
                heart_regen_light_image_rect.center = regen_pos
                screen.blit(heart_regen_light_image, heart_regen_light_image_rect)
                regen_warning_timer += 1
                if regen_warning_timer == fps//2:
                    regen_warning = False
                    regen_warning_timer = 0
                elif regen_warning_timer == 1:
                    regen_warning_sound.play()
            else:
                heart_regen_image_rect.center = regen_pos
                screen.blit(heart_regen_image, heart_regen_image_rect)
                regen_warning_timer += 1
                if regen_warning_timer == fps//2:
                    regen_warning = True
                    regen_warning_timer = 0
                elif regen_warning_timer == 1:
                    regen_warning_counter += 1
        elif regen_timer <= 550:
            screen.blit(heart_regen_image, heart_regen_image_rect)

    ## Update
    pygame.display.update()
    time_counter += 1
    if time_counter == fps:
        time_counter = 0
        time -= 1
        if time == 3 or time == 2 or time == 1:
            pygame.mixer.music.set_volume(.05)
            clock_tick_sound.play()
        elif time == 0:
            message = "Čas vypršel!"
            break
    clock.tick(fps)

## Konec hry
if lets_continue:
    pygame.mixer.music.stop()
    screen.fill(background)
    pygame.draw.rect(screen, gray, (0, 0, screen_sizes[0], 70))
    pygame.draw.rect(screen, cream, (0, 55, screen_sizes[0], 45))
    screen.blit(favicon_medium, favicon_medium_rect)
    screen.blit(game_name_text, game_name_text_rect)
    timer_text = heading_font.render(f"Timer: {time_to_minutes(time)}", True, gold)
    score_text = heading_font.render(f"Score: {score}", True, gold)
    screen.blit(timer_text, timer_text_rect)
    screen.blit(score_text, score_text_rect)
    if hearts[0]:
        screen.blit(heart1_image, heart1_image_rect)
    else:
        screen.blit(heart_empty1_image, heart_empty1_image_rect)
    if hearts[1]:
        screen.blit(heart2_image, heart2_image_rect)
    else:
        screen.blit(heart_empty2_image, heart_empty2_image_rect)
    if hearts[2]:
        screen.blit(heart3_image, heart3_image_rect)
    else:
        screen.blit(heart_empty3_image, heart_empty3_image_rect)
    pygame.draw.rect(screen, gray, (775, 68, 410, 20), 0, 10)
    pygame.draw.rect(screen, boost_bar_color, (780, 73, boost, 10), 0, 10)
    screen.blit(npc_image, npc_image_rect)
    screen.blit(bomb1_image, bomb1_image_rect)
    screen.blit(bomb2_image, bomb2_image_rect)
    screen.blit(bomb3_image, bomb3_image_rect)
    screen.blit(target_image, target_image_rect)
    if is_regen_rendered:
        if regen_warning:
            screen.blit(heart_regen_light_image, heart_regen_light_image_rect)
        else:
            screen.blit(heart_regen_image, heart_regen_image_rect)
    if win:
        win_sound.play()
        pygame.draw.rect(screen, gray, (screen_sizes[0]//2-396, screen_sizes[1]//2-121, 800, 250))
        pygame.draw.rect(screen, light_green2, (screen_sizes[0]//2-400, screen_sizes[1]//2-125, 800, 250))
    else:
        loose_sound.play()
        pygame.draw.rect(screen, gray, (screen_sizes[0]//2-396, screen_sizes[1]//2-121, 800, 250))
        pygame.draw.rect(screen, light_red, (screen_sizes[0]//2-400, screen_sizes[1]//2-125, 800, 250))
    final_text = final_font.render(message, False, black)
    final_text_rect = final_text.get_rect()
    final_text_rect.center = (screen_sizes[0]//2, screen_sizes[1]//2)
    screen.blit(final_text, final_text_rect)
    while lets_continue:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lets_continue = False
pygame.quit()
