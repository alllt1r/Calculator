import pygame
import sys
FPS = 60
WIN_WIDTH = 500
WIN_HEIGHT = 500
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
BLACK = (0, 0, 0)
GREY = (105, 105, 105)
BR_GREY = (200, 200, 200)
RED = (255, 0, 0)

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Calculator')
rect_w = 480
rect_h = 60
w = 80
h = 80
mouseDown = False
f1 = pygame.font.SysFont('arial', 49)
f2 = pygame.font.SysFont('arial', 20)
f3 = pygame.font.SysFont('Calibri_bold', 30)
var1 = 0
var2 = 0
type = 1
type2 = 1
res = 0
mid = 0
sign = ""
results = 0
def print_text(message, ax, ay, font_color, font_size):
    font_type = pygame.font.SysFont('Calibri_bold', font_size)
    text = font_type.render(message, True, font_color)
    sc.blit(text, (ax + 3, ay + 4))

def draw_rect():
    pygame.draw.rect(sc, WHITE, (10, 100, w, h))
    pygame.draw.rect(sc, WHITE, (110, 100, w, h))
    pygame.draw.rect(sc, WHITE, (210, 100, w, h))
    pygame.draw.rect(sc, WHITE, (310, 100, w, h))
    pygame.draw.rect(sc, WHITE, (310, 100, w, h))
    pygame.draw.rect(sc, WHITE, (410, 100, w, h))
    pygame.draw.rect(sc, WHITE, (10, 200, w, h))
    pygame.draw.rect(sc, WHITE, (110, 200, w, h))
    pygame.draw.rect(sc, WHITE, (210, 200, w, h))
    pygame.draw.rect(sc, WHITE, (310, 200, w, h))
    pygame.draw.rect(sc, WHITE, (410, 200, w, h))
    pygame.draw.rect(sc, WHITE, (10, 300, w, h))
    pygame.draw.rect(sc, WHITE, (110, 300, w, h))
    pygame.draw.rect(sc, WHITE, (210, 300, w, h))
    pygame.draw.rect(sc, WHITE, (310, 300, w, h))
    pygame.draw.rect(sc, WHITE, (410, 300, w, h))
    pygame.draw.rect(sc, WHITE, (110, 400, w, h))
    pygame.draw.rect(sc, WHITE, (310, 400, w, h))
    pygame.draw.rect(sc, WHITE, (410, 400, w, h))

def MouseButtonDown(text):
    global mouseDown, results, var1, var2, mid, sign, res, type, type2
    if mouseDown == True:
        print(text)
        mouseDown = False
        if text == "x":
            sign = "x"
            var1 = mid
            mid = 0
            type = 2
            type2 = 1
            results = str(var1) + f" {sign} "
        elif text == "+":
            sign = "+"
            var1 = mid
            mid = 0
            type = 2
            type2 = 1
            results = str(var1) + f" {sign} "
        elif text == "-":
            sign = "-"
            var1 = mid
            mid = 0
            type = 2
            type2 = 1
            results = str(var1) + f" {sign} "
        elif text == "/":
            sign = "/"
            var1 = mid
            mid = 0
            type = 2
            type2 = 1
            results = str(var1) + f" {sign} "
        elif text == "." and type2 == 1:
            type2 = 2
            mid = mid / 10 * 10
            if type == 1:
                var1 = mid
                results = str(var1)
            if type == 2:
                var2 = mid
                results = str(var1) + f" {sign} " + str(var2)
        elif text == "." and type2 == 2:
            pass

        elif text == "C":
            mid = 0
            type2 = 1
            if type == 1:
                var1 = mid
                results = str(var1)
            if type == 2:
                var2 = mid
                results = str(var1) + f" {sign} " + str(var2)
        elif text == "AC":
            var1 = 0
            var1 = 0
            res = 0
            results = 0
            mid = 0
            type = 1
            type2 = 1

        elif text == "=":
            var2 = mid
            mid = 0
            if sign == "x": res = (var1 * var2)
            if sign == "+": res = (var1 + var2)
            if sign == "-": res = (var1 - var2)
            if sign == "/":
                res = (var1 / var2)
                if var1 % var2 == 0:
                    res = int(res)
            mid = res
            results = str(var1) + f" {sign} " + str(var2) + " = " + str(res)
        elif -1 < int(text) < 10:
            if type2 == 1:
                mid = mid * 10 + int(text)
            elif type2 == 2:
                print("asd")
                mid = float(str(int(mid)) + "." + text)
                type2 = 3
            elif type2 == 3:
                print("asd")
                mid = float(str(mid) + text + "") #(int(mid) * 10 + int(text)) + (mid - int(mid))
            if type == 1:
                var1 = mid
                results = str(var1)
            if type == 2:
                var2 = mid
                results = str(var1) + f" {sign} " + str(var2)
            print(mid)


calc = True
while calc:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        else: mouseDown = False
    pygame.draw.rect(sc, GREY, (10, 20, rect_w, rect_h))
    draw_rect()
    mouse = pygame.mouse.get_pos()
    #print(mouse)
    click = pygame.event.get()

    if 100 < mouse[1] < 180:
        if 10 < mouse[0] < 90:
            pygame.draw.rect(sc, BR_GREY, (10, 100, w, h))
            MouseButtonDown("7")
        if 110 < mouse[0] < 190:
            pygame.draw.rect(sc, BR_GREY, (110, 100, w, h))
            MouseButtonDown("8")
        if 210 < mouse[0] < 290:
            pygame.draw.rect(sc, BR_GREY, (210, 100, w, h))
            MouseButtonDown("9")
        if 310 < mouse[0] < 390:
            pygame.draw.rect(sc, BR_GREY, (310, 100, w, h))
            MouseButtonDown("AC")
        if 410 < mouse[0] < 490:
            pygame.draw.rect(sc, BR_GREY, (410, 100, w, h))
            MouseButtonDown("C")
    if 200 < mouse[1] < 280:
        if 10 < mouse[0] < 90:
            pygame.draw.rect(sc, BR_GREY, (10, 200, w, h))
            MouseButtonDown("4")
        if 110 < mouse[0] < 190:
            pygame.draw.rect(sc, BR_GREY, (110, 200, w, h))
            MouseButtonDown("5")
        if 210 < mouse[0] < 290:
            pygame.draw.rect(sc, BR_GREY, (210, 200, w, h))
            MouseButtonDown("6")
        if 310 < mouse[0] < 390:
            pygame.draw.rect(sc, BR_GREY, (310, 200, w, h))
            MouseButtonDown("x")
        if 410 < mouse[0] < 490:
            pygame.draw.rect(sc, BR_GREY, (410, 200, w, h))
            MouseButtonDown("/")
    if 300 < mouse[1] < 380:
        if 10 < mouse[0] < 90:
            pygame.draw.rect(sc, BR_GREY, (10, 300, w, h))
            MouseButtonDown("1")
        if 110 < mouse[0] < 190:
            pygame.draw.rect(sc, BR_GREY, (110, 300, w, h))
            MouseButtonDown("2")
        if 210 < mouse[0] < 290:
            pygame.draw.rect(sc, BR_GREY, (210, 300, w, h))
            MouseButtonDown("3")
        if 310 < mouse[0] < 390:
            pygame.draw.rect(sc, BR_GREY, (310, 300, w, h))
            MouseButtonDown("+")
        if 410 < mouse[0] < 490:
            pygame.draw.rect(sc, BR_GREY, (410, 300, w, h))
            MouseButtonDown("-")
    if 400 < mouse[1] < 480:
        if 110 < mouse[0] < 190:
            pygame.draw.rect(sc, BR_GREY, (110, 400, w, h))
            MouseButtonDown("0")
        if 310 < mouse[0] < 390:
            pygame.draw.rect(sc, BR_GREY, (310, 400, w, h))
            MouseButtonDown(".")
        if 410 < mouse[0] < 490:
            pygame.draw.rect(sc, BR_GREY, (410, 400, w, h))
            MouseButtonDown("=")

    print_text('7', 40, 130, BLACK, 30)
    print_text('8', 140, 130, BLACK, 30)
    print_text('9', 240, 130, BLACK, 30)
    print_text('4', 40, 230, BLACK, 30)
    print_text('5', 140, 230, BLACK, 30)
    print_text('6', 240, 230, BLACK, 30)
    print_text('1', 40, 330, BLACK, 30)
    print_text('2', 140, 330, BLACK, 30)
    print_text('3', 240, 330, BLACK, 30)
    print_text('0', 140, 430, BLACK, 30)
    print_text('AC', 335, 130, BLACK, 30)
    print_text('C', 440, 130, BLACK, 30)
    print_text('X', 340, 230, BLACK, 30)
    print_text('/', 442, 230, BLACK, 30)
    print_text('+', 340, 330, BLACK, 30)
    print_text('—', 437, 330, BLACK, 30)
    print_text('.', 342, 430, BLACK, 30)
    print_text('=', 440, 430, BLACK, 30)
    sc.blit(f1.render(str(mid), True, BLACK), (10, 12))
    sc.blit(f2.render(str(results), True, BLACK), (10, 56))

    pygame.display.update()   
    clock.tick(FPS)