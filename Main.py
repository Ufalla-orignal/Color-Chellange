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
    def __init__(self, color, x, y, width, height, border):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.border=border
        
    def draw(self, screen_):
        pg.draw.rect(screen_, self.color, (self.x, self.y, self.width, self.height), self.border, 5)
        
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

# Создание кнопок и всякого
btn_Main=Button(BLACK, view_x-Button.width/2, view_y-100, Button.width, Button.heigth, 3)
btn_1=Button(generate_color(), view_x-Button.width/2-Distance_to_Center_x-Button.width+30, view_y+Distance_to_Button, Button.width-20, Button.heigth-20, 0)
btn_2=Button(generate_color(), view_x-Button.width/2+10, view_y+Distance_to_Button, Button.width-20, Button.heigth-20, 0)
btn_3=Button(generate_color(), view_x+Button.width/2-10+Distance_to_Center_x, view_y+Distance_to_Button, Button.width-20, Button.heigth-20, 0)
btn_Again=Button(GREEN, view_x-Button.width-50, view_y+100, Button.width-20, Button.heigth-20, 0)
btn_Quit=Button(RED, view_x+50, view_y+100, Button.width-20, Button.heigth-20, 0)

def Circle_1():
    pg.draw.circle(screen, RED, (Window.center_x+230, Window.center_y-150), 8)
def Circle_2():
    pg.draw.circle(screen, RED, (Window.center_x+250, Window.center_y-150), 8)
def Circle_3():
    pg.draw.circle(screen, RED, (Window.center_x+270, Window.center_y-150), 8)

Score = 0

# И текста
textWin, textRectWin = t('You Win! Next!', Window.center_x, Window.center_y+120)
textWrong, textRectWrong = t('Wrong. Next try.', Window.center_x, Window.center_y+120)
textScoreText, textRectScoreText = t('Score: ', Window.center_x-210, Window.center_y-150)
textScore, textRectScore = t(str(Score), Window.center_x-170, Window.center_y-150)
textLife, textRectLife = t('Life: ', Window.center_x+198, Window.center_y-150)
textLose, textRectLose = t('You Lose, Nice job...', Window.center_x, Window.center_y-20)
textAgain, textRectAgain = t('Again', Window.center_x-60-Button.width/2, Window.center_y+120)
textQuit, textRectQuit = t('Quit', Window.center_x+40+Button.width/2, Window.center_y+120)

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

Life = 3
isMouseDown=False
isMouseClick=False
running=True
Win = 1
Lose = 2
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
            btn_Again.mouseIsOver=btn_Again.is_over(mouse_x, mouse_y)
            btn_Quit.mouseIsOver=btn_Quit.is_over(mouse_x, mouse_y)
        if event.type==pg.MOUSEBUTTONDOWN and event.button==1:
            isMouseDown=True
        if event.type==pg.MOUSEBUTTONUP and event.button==1:
            if isMouseDown:
                isMouseClick=True
                
    if isMouseClick:
        isMouseDown=isMouseClick=False
        if btn_1.mouseIsOver and n==1:
            Win_or_Lose = Win
        elif btn_2.mouseIsOver and n==2:
            Win_or_Lose = Win
        elif btn_3.mouseIsOver and n==3:
            Win_or_Lose = Win
        else:
            Win_or_Lose = Lose
        if btn_Again.mouseIsOver:
            Win_Btn()
            win_color, n = Win_Btn()
            btn_1.color = generate_color()
            btn_2.color = generate_color()
            btn_3.color = generate_color()
            text, textRect = t(str(win_color)[1:-1], Window.center_x, Window.center_y-Button.heigth-10)
            Score = 0
            textScore, textRectScore = t(str(Score), Window.center_x-170, Window.center_y-150)
            Life = 3
            Win_or_Lose = 0
            Win_number = 0
        if btn_Quit.mouseIsOver:
            running = False

    if Win_or_Lose == Win:
        Win_Btn()
        win_color, n = Win_Btn()
        btn_1.color = generate_color()
        btn_2.color = generate_color()
        btn_3.color = generate_color()
        text, textRect = t(str(win_color)[1:-1], Window.center_x, Window.center_y-Button.heigth-10)
        Win_number = Win
        Score += 1
        textScore, textRectScore = t(str(Score), Window.center_x-170, Window.center_y-150)
    
    elif Win_or_Lose == Lose:
        Win_number = Lose
        Life -= 1
        textScore, textRectScore = t(str(Score), Window.center_x-170, Window.center_y-150)
    
    Win_or_Lose = 0
    
    screen.blit(textScoreText, textRectScoreText)
    screen.blit(textScore, textRectScore)
    screen.blit(textLife, textRectLife)
    
    if Life == 3:
        Circle_1()
        Circle_2()
        Circle_3()
        btn_Main.draw(screen)
        btn_1.draw(screen)
        btn_2.draw(screen)
        btn_3.draw(screen)
        screen.blit(text, textRect)
        if Win_number == Win:
            screen.blit(textWin, textRectWin)
        elif Win_number == Lose:
            screen.blit(textWrong, textRectWrong)
    elif Life == 2:
        Circle_1()
        Circle_2()
        btn_Main.draw(screen)
        btn_1.draw(screen)
        btn_2.draw(screen)
        btn_3.draw(screen)
        screen.blit(text, textRect)
        if Win_number == Win:
            screen.blit(textWin, textRectWin)
        elif Win_number == Lose:
            screen.blit(textWrong, textRectWrong)
    elif Life == 1:
        Circle_1()
        btn_Main.draw(screen)
        btn_1.draw(screen)
        btn_2.draw(screen)
        btn_3.draw(screen)
        screen.blit(text, textRect)
        if Win_number == Win:
            screen.blit(textWin, textRectWin)
        elif Win_number == Lose:
            screen.blit(textWrong, textRectWrong)
    else:
        btn_Quit.draw(screen)
        btn_Again.draw(screen)
        screen.blit(textLose, textRectLose)
        screen.blit(textAgain, textRectAgain)
        screen.blit(textQuit, textRectQuit)
    
    pg.display.update()
          
pg.quit()