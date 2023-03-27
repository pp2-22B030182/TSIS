import pygame
import datetime

pygame.init()

size = w,h = (1310,1030)

time = datetime.datetime.now()

angle = -(int(time.strftime("%S")) * 6) - 6
anglem = -(int(time.strftime("%M")) * 6) + (int(time.strftime("%S")) * 6 /  60) - 54

def rotate(image, rect, angle):
    new_image = pygame.transform.rotate(image, angle)
    rect = new_image.get_rect(center = rect.center)
    return new_image, rect

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Mickey clock')

mickey = pygame.image.load('1.jpg')
seconds = pygame.image.load('seconds (1).png')
minutes = pygame.image.load('minutes (1).png')

imagem = pygame.Surface(size, pygame.SRCALPHA)
imagem.blit(minutes, (475,360))
newm = imagem
rectm = imagem.get_rect(center = (w//2,h//2))

images = pygame.Surface((63,h), pygame.SRCALPHA)
images.blit(seconds, (0,0))
news = images
rects = images.get_rect(center = (w//2,h//2))

done = False
clock = pygame.time.Clock()

FPS = 60
while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(mickey,(0,0))
    screen.blit(images,rects)
    screen.blit(imagem,rectm)
    images, rects = rotate(news, rects, angle)
    imagem, rectm = rotate(newm, rectm, anglem)

    angle -= 0.1
    anglem -= 0.1/60
    pygame.display.update()

pygame.quit()