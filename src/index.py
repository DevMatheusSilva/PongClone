import pygame

pygame.init()

# variaveis config
screen = pygame.display.set_mode((858, 525))
clock = pygame.time.Clock()
running = True
game_start = False

pygame.display.set_caption("Poggers")

# variaveis de fonte
font1 = pygame.font.SysFont("Monospace", 50, True, False)
font2 = pygame.font.SysFont("Monospace", 20, False, False)

# cores
white = (255,255,255)

# variaveis de sprite
rack2_pos = screen.get_width() - 20

# rack sprite
rack1 = pygame.Rect(10, 0, 20, 80)
r1_up_point = rack1.topleft
r1_down_point = rack1.bottomleft
rack2 = pygame.Rect(rack2_pos - 10, 0, 20, 80)

# ball sprite
ball_radius = 10
ball = pygame.Rect(screen.get_width() // 2 - ball_radius, screen.get_height() // 2 - ball_radius, ball_radius*2, ball_radius*2)
ball_sp_x = 5
ball_sp_y = 5

# variaveis de movimento
mov_speed = 10
r1_move_down = False
r1_move_up = False
r2_move_down = False
r2_move_up = False

# variaveis de score
player1 = 0
player2 = 0

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_start = True
    
    if not(game_start):
        text = font2.render("Instruções", True, white)
        t1 = font2.render("1.Clique com o mouse para começar a jogar", True, white)
        t2 = font2.render("2. S e X controlam o Player 1", True, white)
        t3 = font2.render("3. Seta Cima e Seta Baixo controlam o Player 2", True, white)
        title = font1.render("POGGERS", True, white)
        
        screen.blit (text, ((screen.get_width() - text.get_width()) // 2, 20))
        screen.blit (t1, ((screen.get_width() - t1.get_width()) // 2, 100))
        screen.blit (t2, ((screen.get_width() - t2.get_width()) // 2, 150))
        screen.blit (t3, ((screen.get_width() - t3.get_width()) // 2, 200))
        screen.blit (title, ((screen.get_width() - title.get_width()) // 2, 300))
        
    if game_start:
        screen.fill("black")
        
        # renderização da pontuação
        score_player1 = font1.render(f"{player1}" , True, white)
        score_player2 = font1.render(f"{player2}" , True, white)
        screen.blit(score_player1, (200, 10))
        screen.blit(score_player2, (rack2_pos - 210, 10))
        
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

        #logica de movimento bola
        ball.x += ball_sp_x
        ball.y += ball_sp_y
        
        # logica de colisao vertical bola
        if ball.top <= 0 or ball.bottom >= screen.get_height():
            ball_sp_y = -ball_sp_y
            
        # logica colisao com as racks
        if ball.colliderect(rack1) or ball.colliderect(rack2):
            ball_sp_x = -ball_sp_x
        
        # logica de colisao com as laterais
        if ball.left <= 0:
            ball.x = screen.get_width() // 2
            ball.y = screen.get_height() // 2
            player2 += 1
        elif ball.right >= screen.get_width():
            ball.x = screen.get_width() // 2
            ball.y = screen.get_height() // 2
            player1 += 1
            
        pygame.draw.rect(screen, white, rack1)
        pygame.draw.rect(screen, white, rack2)
        pygame.draw.ellipse(screen, white, ball)
        
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
