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
    r = rnd.randint(0, 255)
    g = rnd.randint(0, 255)
    b = rnd.randint(0, 255)
    return (r, g, b)

def t (str_t, x, y):
    text=font.render(str_t, True, BLACK)
    textRect=text.get_rect()
    textRect.center=(x, y)
    return text, textRect

# Color это что -то такое (255, 67, 90)
def color_to_str(color):
    return str(color)[1:-1]

# Не изменяется
pg.init()
screen=pg.display.set_mode((Window.width, Window.heigth))
pg.display.set_caption('Color Challenge')
font=pg.font.Font('freesansbold.ttf', 20)
clock=pg.time.Clock()

Distance_to_Center_x=50
Button.width=130
Button.heigth=60
Distance_to_Button=10

view_x=Window.center_x
view_y=Window.center_y

colors = [generate_color(), generate_color(), generate_color()]
btns = []
# Создание кнопок
btn_Main=Button(RED, view_x-Button.width/2, view_y-100, Button.width, Button.heigth)
# btn_1=Button(colors[0], view_x-Button.width/2-Distance_to_Center_x-Button.width+30, view_y+Distance_to_Button, Button.width-20, Button.heigth-20)
# btn_2=Button(colors[1], view_x-Button.width/2+10, view_y+Distance_to_Button, Button.width-20, Button.heigth-20)
# btn_3=Button(colors[2], view_x+Button.width/2-10+Distance_to_Center_x, view_y+Distance_to_Button, Button.width-20, Button.heigth-20)

btns.append(Button(colors[0], view_x-Button.width/2-Distance_to_Center_x-Button.width+30, view_y+Distance_to_Button, Button.width-20, Button.heigth-20))
btns.append(Button(colors[1], view_x-Button.width/2+10, view_y+Distance_to_Button, Button.width-20, Button.heigth-20))
btns.append(Button(colors[2], view_x+Button.width/2-10+Distance_to_Center_x, view_y+Distance_to_Button, Button.width-20, Button.heigth-20))


# Выбор победной кнопки
# def FirstB():
#     return color_to_str(btn_1.color)
# 
# def SecondB():
#     return color_to_str(btn_2.color)
# 
# def ThirdB():
#     return color_to_str(btn_3.color)

# func_arr = [FirstB, SecondB, ThirdB]
rnd_function_index = rnd.randint(0, len(btns)-1)
# func_arr[rnd_function_index]()

# И текста
text, textRect = t(color_to_str(btns[rnd_function_index].color), Window.center_x, Window.center_y-Button.heigth-10)
text1, textRect1 = t('1', Window.center_x-Distance_to_Center_x-Button.width+20, Window.center_y+Distance_to_Button+Button.width/2-45)
text2, textRect2 = t('2', Window.center_x, Window.center_y+Distance_to_Button+Button.width/2-45)
text3, textRect3 = t('3', Window.center_x+Distance_to_Center_x+Button.width-20, Window.center_y+Distance_to_Button+Button.width/2-45)

isMouseDown=False
isMouseClick=False
running=True
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
        if btn_1.mouseIsOver:
            btn_1.color=generate_color()
        if btn_2.mouseIsOver:
            btn_2.color=generate_color()
        if btn_3.mouseIsOver:
            btn_3.color=generate_color()
            
    btn_Main.draw(screen)
    btn_1.draw(screen)
    btn_2.draw(screen)
    btn_3.draw(screen)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    pg.display.update()
          
pg.quit()