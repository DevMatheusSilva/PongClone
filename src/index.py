import pygame

pygame.init()

# variaveis config
screen = pygame.display.set_mode((858, 525))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Poggers")

# cores
white = (255,255,255)

# variaveis de sprite
rack2_pos = screen.get_width() - 20

# sprites
rack1 = pygame.Rect(0, 0, 20, 80)
r1_up_point = rack1.topleft
r1_down_point = rack1.bottomleft
rack2 = pygame.Rect(rack2_pos, 0, 20, 80)

# variaveis de movimento
mov_speed = 10
r1_move_down = False
r1_move_up = False
r2_move_down = False
r2_move_up = False

# loop principal
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # config de movimento
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                r2_move_up = True
            elif event.key == pygame.K_s:
                r1_move_up = True
            elif event.key == pygame.K_DOWN:
                r2_move_down = True
            elif event.key == pygame.K_x:
                r1_move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                r2_move_up = False
            elif event.key == pygame.K_s:
                r1_move_up = False
            elif event.key == pygame.K_DOWN:
                r2_move_down = False
            elif event.key == pygame.K_x:
                r1_move_down = False
    
    screen.fill("black")
    
    # logica de movimento
    if r1_move_up:
        rack1.y -= mov_speed
    if r1_move_down:
        rack1.y += mov_speed
    if r2_move_up:
        rack2.y -= mov_speed
    if r2_move_down:
        rack2.y += mov_speed
    
    # logica de colisao r1
    if rack1.y < 0:
        rack1.y = 0
    elif rack1.y + rack1.height > screen.get_height():
        rack1.y = screen.get_height() - rack1.height

    # logica de colisao r2
    if rack2.y < 0:
        rack2.y = 0
    elif rack2.y + rack2.height > screen.get_height():
        rack2.y = screen.get_height() - rack2.height
        
    pygame.draw.rect(screen, white, rack1)
    pygame.draw.rect(screen, white, rack2)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
