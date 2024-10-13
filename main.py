import pygame, sys

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("小游戏程序")

FPS = 60
exit = False

x = 0
y = 0

clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)

last_time = pygame.time.get_ticks()

while not exit:
    clock.tick(FPS)
    fps = clock.get_fps()
    current_time = pygame.time.get_ticks()
    delta = (current_time - last_time) / 1000
    last_time = current_time
    # screen.blit()

    for event in pygame.event.get():
        # print(event.type ,pygame.QUIT)
        match event.type:
            case pygame.QUIT:
                exit = True
            case pygame.KEYDOWN:
                match event.key:
                    case _:
                        pass
            case _:
                pass

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        x -= 100 * delta
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        x += 100 * delta
    if pygame.key.get_pressed()[pygame.K_UP]:
        y -= 100 * delta
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        y += 100 * delta

    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),pygame.Rect(x,y,30,30))
    fps_text = font.render("FPS:{:.2f} Delta:{:.4f}s".format(fps,delta),True,(255,255,255))
    screen.blit(fps_text,fps_text.get_rect())
    pygame.display.flip()
pygame.quit()