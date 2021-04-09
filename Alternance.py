import pygame, sys

x = 310
y= 110

x2 = 210
y2 = 210

def rotate(surface, angle, x, y):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center= (x,y))
    return rotated_surface, rotated_rect

def y_positions(x, y, y_position):
    if y == 60:
        y_position = 5
    if y == 110:
        y_position = 4
    if y == 160:
        y_position = 3
    if y == 210:
        y_position = 2
    if y == 260:
        y_position = 1
    if y == 310:
        y_position = 0

    return y_position

def x_positions(x, y, x_position):
    #Position de la tondeuse
    if x == 110:
        x_position = 0
    if x == 160:
        x_position = 1
    if x == 210:
        x_position = 2
    if x == 260:
        x_position = 3
    if x == 310:
        x_position = 4
    if x == 360:
        x_position = 5

    return x_position

def mouvement(x, y, angle, orientation):
    if x < 360:
        if angle == 0 or angle == -360 or angle == 360:
            x = x + 50
            y = y + 0
            orientation = 'E'
    if y > 60:
        if angle == 90 or angle == -270 or angle == 450:
            x = x + 0
            y = y - 50
            orientation = 'N'
    if x > 60:
        if angle == 180 or angle == -180 or angle == 540:
            x = x - 50
            y = y + 0
            orientation ='W'
    if y < 320:
        if angle == 270 or angle == -90 or angle == -450:
            x = x + 0
            y = y + 50
            orientation = 'S'
    return x, y, angle, orientation

# Python code to convert string to list character-wise
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
# Driver code
str1="addaggadaga"

pygame.init()
screen = pygame.display.set_mode([1000,700])
base_font = pygame.font.Font(None,32)
form_text = ''
form_text2 = ''
origin_pic = pygame.image.load("tondeuse1.png")
origin_pic2 = pygame.image.load("tondeuse2.png")
pic =  pygame.transform.scale(origin_pic, (100,100))
pic2 =  pygame.transform.scale(origin_pic2, (100,100))
pic_rect = pic.get_rect(center= (x,y))
pic_rect2 = pic2.get_rect(center= (0,0))
angle = -90
angle2 = 90
orientation = 'S'
orientation2 = 'N'


input_rect = pygame.Rect(600,70,140,32)
input_rect2 = pygame.Rect(600,150,140,32)
button1 = pygame.Rect(600,200,265,32)
button_text1 = 'Démarrer les tondeuses'
color_active = pygame.Color('green')
color_passive = pygame.Color('grey')
color1 = color_passive
color2 = color_passive
colorButton = color_passive

activeInput1 = False
activeInput2 = False
activeButton = False
activeButton2 = False
list1 = []
list2 = []

x_position = 0
y_position = 0

x_position2 = 0
y_position2 = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Formulaire
        if event.type == pygame.KEYDOWN:
            if activeInput1 == True:
                if event.key == pygame.K_BACKSPACE:
                    form_text = form_text[:-1]
                else:
                    form_text += event.unicode
            if activeInput2 == True:
                if event.key == pygame.K_BACKSPACE:
                    form_text2 = form_text2[:-1]
                else:
                    form_text2 += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                activeInput1 = True
            else:
                activeInput1 = False
            if input_rect2.collidepoint(event.pos):
                activeInput2 = True
            else:
                activeInput2 = False
            if button1.collidepoint(event.pos):
                activeButton = True
                list1 = Convert(form_text)
                list2 = Convert(form_text2)
                if not list1 or not list2:
                    print("Vous devez insérer des instructions dans les deux champs")
                else:
                    for indice in range(len(list1)):
                        if list1[indice] == 'd' or list1[indice] == 'D':
                            angle = angle - 90
                        if list1[indice] == 'g' or list1[indice] == 'G':
                            angle = angle + 90
                        if list1[indice] == 'a' or list1[indice] == 'A':
                            x,y,angle,orientation = mouvement(x, y, angle, orientation)
                    for indice in range(len(list2)):
                        if list2[indice] == 'd' or list1[indice] == 'G':
                            angle2 = angle2 - 90
                        if list2[indice] == 'g' or list1[indice] == 'G':
                            angle2 = angle2 + 90
                        if list2[indice] == 'a' or list1[indice] == 'A':
                            x2,y2,angle2,orientation2 = mouvement(x2, y2, angle2, orientation2)
            else:
                activeButton = False

        text_surface = base_font.render(form_text,True,(0,0,0))
        text_button1 = base_font.render(button_text1, True, (0,0,0))
        text_surface2 = base_font.render(form_text2,True,(0,0,0))

    if activeInput1:
        color1 = color_active
    else:
        color1 = color_passive
    if activeInput2:
        color2 = color_active
    else:
        color2 = color_passive
    if activeButton:
        colorButton = color_active
    else:
        colorButton = color_passive

    screen.fill((255,255,255))

    y_position = y_positions(x, y, y_position)
    x_position = x_positions(x, y, x_position)
    y_position2 = y_positions(x2, y2, y_position2)
    x_position2 = x_positions(x2, y2, x_position2)


    #Affichage de la position et de l'orientation
    title1 = base_font.render('Veuillez inserer vos instructions :',True,pygame.Color(000,000,000))
    screen.blit(title1,(600,45))
    title3 = base_font.render('Position actuelle tondeuse 1 :',True,pygame.Color(000,000,000))
    screen.blit(title3,(600,390))
    title4 = base_font.render('Position actuelle tondeuse 2 :',True,pygame.Color(000,000,000))
    screen.blit(title4,(600,450))
    affiche_x = base_font.render(str(x_position),True,pygame.Color(000,000,000))
    screen.blit(affiche_x,(600,410))
    affiche_x2 = base_font.render(str(x_position2),True,pygame.Color(000,000,000))
    screen.blit(affiche_x2,(600,470))
    affiche_y = base_font.render(str(y_position),True,pygame.Color(000,000,000))
    screen.blit(affiche_y,(615,410))
    affiche_y2 = base_font.render(str(y_position2),True,pygame.Color(000,000,000))
    screen.blit(affiche_y2,(615,470))
    affiche_orientation = base_font.render(orientation,True,pygame.Color(000,000,000))
    screen.blit(affiche_orientation,(630,410))
    affiche_orientation2 = base_font.render(orientation2,True,pygame.Color(000,000,000))
    screen.blit(affiche_orientation2,(630,470))

    pygame.draw.rect(screen,color2,input_rect2,2)
    title2 = base_font.render('Veuillez insérer vos instructions:',True,pygame.Color(000,000,000))
    screen.blit(title1,(600,120))
    screen.blit(text_surface2,(input_rect2.x + 5, input_rect2.y + 5))
    input_rect2.w = max(100,text_surface2.get_width() + 10)
    pygame.draw.rect(screen,color1,input_rect,2)
    pygame.draw.rect(screen,colorButton, button1)
    pic_rotated,pic_rotated_rect = rotate(pic, angle, x, y)
    pic_rotated2,pic_rotated_rect2 = rotate(pic2, angle2, x2, y2)
    screen.blit(pic_rotated, pic_rotated_rect)
    screen.blit(pic_rotated2, pic_rotated_rect2)
    screen.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))
    screen.blit(text_button1,(button1.x + 5, button1.y + 5))
    input_rect.w = max(100,text_surface.get_width() + 10)
    pygame.display.update()
    pygame.display.flip()

