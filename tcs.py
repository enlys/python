import pygame,sys,random
from pygame.locals import *
red=pygame.Color(255,0,0)
white=pygame.Color(255,255,255)
black=pygame.Color(0,0,0)

def gameover():
    pygame.quit()
    sys.exit()



def main():
    pygame.init()
    fps=pygame.time.Clock()

    play1=pygame.display.set_mode((640,480))
    pygame.display.set_caption('贪吃蛇')

    snake=[100,100]
    snakebody=[[100,100],[80,100],[60,100]]
    targ=[300,300]
    target=1
    direct='right'
    change= direct

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                if event.key==K_RIGHT:
                    change='right'
                if event.key == K_LEFT:
                    change = 'left'
                if event.key == K_UP:
                    change = 'up'
                if event.key == K_DOWN:
                    change = 'down'
                if event.key==K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        if change =='left' and not direct=='right':
            direct=change
        if change =='right' and not direct=='left':
            direct=change
        if change =='up' and not direct=='down':
            direct=change
        if change =='down' and not direct=='up':
            direct=change

        if direct=='right':
            snake[0]+=20
        if direct == 'left':
            snake[0] -=20
        if direct == 'up':
            snake[1] -= 20
        if direct == 'down':
            snake[1] += 20

        snakebody.insert(0,list(snake))
        if snake[0]==targ[0] and snake[1]==targ[1]:
            target=0
        else:
            snakebody.pop()

        if target==0:
            x=random.randrange(1,32)
            y=random.randrange(1,24)
            targ=[int(x*20),int(y*20)]
            target=1

        play1.fill(black)
        for poist in snakebody:
            pygame.draw.rect(play1,white,Rect(poist[0],poist[1],20,20))
            pygame.draw.rect(play1, red, Rect(targ[0], targ[1], 20, 20))

        pygame.display.flip()

        if snake[0]>620 or snake[0]<0:
            gameover()
        elif snake[1]>460 or snake[1]<0:
            gameover()

        fps.tick(6)


if __name__=='__main__':
    main()







