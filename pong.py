import pygame
pygame.init()

screen = pygame.display.set_mode ((700,500))
pygame.display.set_caption("pong")
doExit = False

clock = pygame.time.Clock()
P2Score = 0
P1Score = 0
p1x = 7
p1y = 200
p2x = 675
p2y = 200
bx = 350 #xPosition
by = 350 #yPosition
bVx = 8 #x Velocity (Horizontal speed)
bVy = 5 #Y Velociry (vertical speed)
while not doExit: #Game loop---------------------------------------------
    
    # Event Queue stuff--------------------------------------------
    clock.tick(700) #sets the FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
            
    #Game logic here-----------------------------------------------
        keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
            p1y-=5
    if keys[pygame.K_s]:
            p1y+=5
    if keys[pygame.K_UP]:
            p2y-=5
    if keys[pygame.K_DOWN]:
            p2y+=5

        #reflection ball off of side walls
    if bx < 0 or bx + 20 > 700:
            bVx *= -1
    if by < 0 or by + 20 > 500: #bounce off top or bottom wall
            bVy *= -1
            
        #reflection ball off of paddle
    if bx < p1x + 20 and by + 20 > p1y and by < p1y + 100:
            bVx *= -1
    if bx < p2x + 20 and bx + 20 > p2x and by < p2y + 100:
            bVx *= -1
        #player 2 scores
    if bx < 0:
        P2Score += 1
    if bx > 685:
        P1Score += 1
    #ball movment
    bx += bVx
    by += bVy
        
    #Render section here-----------------------------------
    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,255,255), [349,0], [349,500], 5)
    pygame.draw.rect(screen, (255,255,255), (p1x, p1y, 20, 120), 1)
    pygame.draw.rect(screen, (255,255,255), (p2x, p2y, 20, 120), 1)
    pygame.draw.circle(screen, (255,255,255), (bx, by,) , 10)
    #Display scores---------------------------------------
    font = pygame.font.Font(None,74) #uses default
    text = font.render(str(P2Score), 1, (255,255,255))
    screen.blit(text, (250,10))
    text = font.render(str(P1Score), 1, (255,255,255))
    screen.blit(text, (420,10))
    pygame.display.flip()
#end Game Loop here---------------------------------------
pygame.quit()
