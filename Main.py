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
Name_screen=pg.display.set_caption('Color Chellange')
clock=pg.time.Clock()

class Button:
    mouseIsOver=False
    mouseIsDown=False
    mouseIsUp=False
    
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

font=pg.font.Font('freesansbold.ttf', 20)

def t (str_t, x, y, Color):
    text=font.render(str_t, True, Black, Color)
    textRect=text.get_rect()
    textRect.center=(x, y)
    return text, textRect

text, textRect = t('Цвэт', Window.center_x, Window.center_y-Button.heigth-10, Red)
text1, textRect1 = t('1', Window.center_x-Distance_to_Center_x-Button.width+15, Window.center_y+Distance_to_Button+Button.width/2-10, Green)

view_x=Window.center_x
view_y=Window.center_y

btn_Main=Button(Red, view_x-Button.width/2, view_y-100, Button.width, Button.heigth)
btn_1=Button(Green, view_x-Button.width/2-Distance_to_Center_x-Button.width+30, view_y+Distance_to_Button, Button.width-20, Button.heigth-20)
btn_2=Button(Green, view_x-Button.width/2+10, view_y+Distance_to_Button, Button.width-20, Button.heigth-20)
btn_3=Button(Green, view_x+Button.width/2-10+Distance_to_Center_x, view_y+Distance_to_Button, Button.width-20, Button.heigth-20)

isMouseDown=False
isMouseClick=False
running=True
while running:
    screen.fill(White)
    screen.blit(text, textRect)
    clock.tick(FPS)
    
    list_events=pg.event.get() # Список событий
    for event in list_events:
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.MOUSEMOTION:
            mouse_x, mouse_y=event.pos # Коорды мышки
            btn_1.mouseIsOver=btn_1.is_over(mouse_x, mouse_y)
            btn_2.mouseIsOver=btn_2.is_over(mouse_x, mouse_y)
            btn_3.mouseIsOver=btn_3.is_over(mouse_x, mouse_y)
        if event.type==pg.MOUSEBUTTONDOWN and event.button==1:
            isMouseDown=True
        if event.type==pg.MOUSEBUTTONUP and event.button==1:
            if isMouseDown:
                isMouseClick=True
                
    if isMouseClick:
        isMouseDown=isMouseClick=False
        if btn_1.mouseIsOver:
            print("1")
        if btn_2.mouseIsOver:
            print("2")
        if btn_3.mouseIsOver:
            print("3")
            
    btn_Main.draw(screen)
    btn_1.draw(screen)
    btn_2.draw(screen)
    btn_3.draw(screen)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    pg.display.update()
          
pg.quit()