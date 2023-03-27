import pygame
import os
import re

mylist = []

def name(n):
    font = pygame.font.SysFont('Arial Black',60)
    song = font.render(mylist[n],True,(0,0,0))
    screen.blit(song,(200,310))
    pygame.display.update()

with os.scandir() as x:
    for i in x:
        if i.is_file():
            if re.findall(".mp3",i.name):
                mylist.append(i.name)
        

print(mylist)

pygame.init()

pygame.mixer.init()

size = weigth, heigth = (600,600)

RED = (255,0,0)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Makstyn muzykasy")

screen.fill(RED)

font = pygame.font.SysFont("Arial Black",60)

text = font.render("Music player",True,(0,0,0))

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(mylist[0])
pygame.mixer.music.play()

done = False
pause = False

cnt = 0
pos = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            cnt += 1
            if cnt == 2:
                cnt = 0
            else:
                pos += cnt
                pygame.mixer.music.load(mylist[pos])
                pygame.mixer.music.play()
                cnt = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            pause = not pause
            if pause:
                pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            pause = not pause
            if not pause:
                pygame.mixer.music.unpause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            cnt += 1
            if cnt == 2:
                cnt = 0
            else:
                pos -= cnt
                pygame.mixer.music.load(mylist[pos])
                pygame.mixer.music.play()
                cnt = 0
        if event.type == SONG_END:
            cnt += 1
            if cnt == 2:
                cnt = 0
            else:
                pos += cnt
                pygame.mixer.music.load(mylist[pos])
                pygame.mixer.music.play()
                cnt = 0
    name(pos)
    screen.fill(RED)
    screen.blit(text,(100,230))
    pygame.display.update()

pygame.quit()