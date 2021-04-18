import pygame as pg
import random as rnd

# Константы
FPS=30
RED=(255, 0, 0)
WHITE=(255, 255, 255)
GREEN=(0, 255, 0)
BLACK=(0, 0, 0)

# Классы и функции
class Window:
    width=640
    heigth=480
    center_x=width/2
    center_y=heigth/2

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
        
def generate_color():
    r=rnd.randint(0, 255)
    g=rnd.randint(0, 255)
    b=rnd.randint(0, 255)
    return (r, g, b)

def t (str_t, x, y):
    text=font.render(str_t, True, BLACK)
    textRect=text.get_rect()
    textRect.center=(x, y)
    return text, textRect

# Не изменяется
pg.init()
screen=pg.display.set_mode((Window.width, Window.heigth))
pg.display.set_caption('Color Chellange')
font=pg.font.Font('freesansbold.ttf', 20)
clock=pg.time.Clock()

Distance_to_Center_x=50
Button.width=130
Button.heigth=60
Distance_to_Button=10

view_x=Window.center_x
view_y=Window.center_y

# Создание кнопок
btn_Main=Button(WHITE, view_x-Button.width/2, view_y-100, Button.width, Button.heigth)
btn_1=Button(generate_color(), view_x-Button.width/2-Distance_to_Center_x-Button.width+30, view_y+Distance_to_Button, Button.width-20, Button.heigth-20)
btn_2=Button(generate_color(), view_x-Button.width/2+10, view_y+Distance_to_Button, Button.width-20, Button.heigth-20)
btn_3=Button(generate_color(), view_x+Button.width/2-10+Distance_to_Center_x, view_y+Distance_to_Button, Button.width-20, Button.heigth-20)

# И текста
textWin, textRectWin = t('You Win! Next!', Window.center_x, Window.center_y+120)
textLose, textRectLose = t('You Lose...', Window.center_x, Window.center_y+120)

# win btn
def Win_Btn():
    n = rnd.randint(1,3)
    win_color = ()
    if (n==1):
        win_color = btn_1.color
    elif (n==2):
        win_color = btn_2.color
    elif (n==3):
        win_color = btn_3.color
    return win_color, n
win_color, n = Win_Btn()
text, textRect = t(str(win_color)[1:-1], Window.center_x, Window.center_y-Button.heigth-10) 

isMouseDown=False
isMouseClick=False
running=True
Win_or_Lose = 0 # Победа или нет
Win_number = 0 # Определяет что писать
while running:
    screen.fill(WHITE)
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
        if btn_1.mouseIsOver and n==1:
            Win_or_Lose = 1
        elif btn_2.mouseIsOver and n==2:
            Win_or_Lose = 1
        elif btn_3.mouseIsOver and n==3:
            Win_or_Lose = 1
        else:
            Win_or_Lose = 2

    if Win_or_Lose==1:
        Win_Btn()
        win_color, n = Win_Btn()
        btn_1.color = generate_color()
        btn_2.color = generate_color()
        btn_3.color = generate_color()
        text, textRect = t(str(win_color)[1:-1], Window.center_x, Window.center_y-Button.heigth-10)
        Win_number = 1
    
    elif Win_or_Lose==2:
        Win_number = 2
    
    Win_or_Lose = 0
    
    if Win_number == 1:
        screen.blit(textWin, textRectWin)
    elif Win_number == 2:
        screen.blit(textLose, textRectLose)
    
    btn_Main.draw(screen)
    btn_1.draw(screen)
    btn_2.draw(screen)
    btn_3.draw(screen)
    screen.blit(text, textRect)
    pg.display.update()
          
pg.quit()