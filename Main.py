import pygame as pg
import random as rnd

FPS=30

class Window:
    width=640
    heigth=480
    center_x=width/2
    center_y=heigth/2

pg.init()
screen=pg.display.set_mode((Window.width, Window.heigth))
Name_screen=pg.display.set_caption('JoKe GaMe')
clock=pg.time.Clock()

class Button:
    width=0
    # Конструктор
    def __init__(self, color, x, y, width, height):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        
    def draw(self, screen_):
        pg.draw.rect(screen_, self.color, (self.x, self.y, self.width, self.height))
        
    def is_over(self, mouse_x, mouse_y):
        return self.x<=mouse_x<=self.x+self.width and \
           self.y<=mouse_y<=self.y+self.heigth
        
    def jumpto(self, x, y):
        self.x=x
        self.y=y
        
    
Red=(255, 0, 0)
White=(255, 255, 255)
Green=(0, 255, 0)
Black=(0, 0, 0)

Distance_to_Center_x=50
Button.width=130
Button.heigth=60
Distance_to_Button=10

#font=pg.font.Font('freesansbold.ttf', 18)
#text=font.render('Да или нет?', True, Black, White)
#textRect=text.get_rect()
#textRect.center=(Window.center_x, Window.center_y-60)

view_x=Window.center_x
view_y=Window.center_y

btn_Main=Button(Red, view_x-Button.width/2, view_y-100, Button.width, Button.heigth)
btn_1=Button(Green, view_x-Distance_to_Center_x-Button.width, view_y+Distance_to_Button, Button.width, Button.heigth)
btn_2=Button(Green, view_x+Distance_to_Center_x, view_y+Distance_to_Button, Button.width, Button.heigth)

running=True
while running:
    screen.fill(White)
    #screen.blit(text, textRect)
    clock.tick(FPS)
    
    list_events=pg.event.get() # Список событий
    for event in list_events:
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.MOUSEMOTION:
            mouse_x, mouse_y=event.pos # Коорды мышки
            #if btn_no.is_over(mouse_x, mouse_y):
             #   new_x=rnd.randint(0, Window.width)
              #  new_y=rnd.randint(0, Window.heigth)
              #  btn_no.jumpto(new_x, new_y)
            
    btn_Main.draw(screen)
    btn_1.draw(screen)
    btn_2.draw(screen)
    pg.display.update()
          
pg.quit()
