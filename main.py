import pygame
pygame.init()

sc_width = 750
sc_height = 650
screen = pygame.display.set_mode((sc_width,sc_height))
pygame.display.set_caption('Хрестики-нулики')
screen.fill((237,175,255))

background_img = pygame.image.load('img/bg_without_cells.png')
background_img = pygame.transform.scale (background_img, (500, 500))


cross_img = pygame.image.load('img/cross.png')
cross_img = pygame.transform.scale (cross_img, (130, 130))

list_cross = [cross_img]

zero_img = pygame.image.load('img/zero.png')
zero_img = pygame.transform.scale (zero_img, (130, 130))

cell_img = pygame.image.load('img/cell.png')
cell_img = pygame.transform.scale (cell_img, (130, 130))


cell1_win = pygame.image.load('img/cell_win.png')
cell1_win = pygame.transform.scale(cell1_win, (130,130))




screen.blit(background_img, (125, 50))

screen.blit(cell_img, (150, 75)) # = 1
screen.blit(cell_img, (150, 233)) # = 4
screen.blit(cell_img, (150, 390)) # = 7

screen.blit(cell_img, (305, 75)) # = 2
screen.blit(cell_img, (305, 233)) # = 5
screen.blit(cell_img, (305, 390))# = 8

screen.blit(cell_img, (465, 75)) # = 3
screen.blit(cell_img, (465, 233)) # = 6
screen.blit(cell_img, (465, 390))# = 9


step = ['cross']

list_cell = [ 0,0,0,
              0,0,0,
              0,0,0 ] 


def who_turn(x,y, number):
    if step[0] == 'cross':
        screen.blit(list_cross[0], (x,y))
        step[0] = 'zero'    
        list_cell[number] = 1
    elif step[0] == 'zero':
        screen.blit(zero_img, (x,y))
        step[0] = 'cross'  
        list_cell[number] = 2
    
count_win = 0 
step_of_win = True


def start_game():
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                X_Y = event.pos
                if count_win == 0:
                    # Перший рядок (3 комірки (горизонтально))
                    # перша комірка
                    if 150 <= X_Y[0] <= 280 and 75 <= X_Y[1] <= 205:
                        if step[0] == 'cross' and list_cell[0] == 0:
                            who_turn(150, 75, 0)
                        elif step[0] == 'zero' and list_cell[0] == 0:
                            who_turn(150, 75, 0)

                    # друга комірка
                    elif 305 <= X_Y[0] <= 435 and 75 <= X_Y[1] <= 205 :
                        if step[0] == 'cross' and list_cell[1] == 0:
                            who_turn(305, 75, 1)
                        elif step[0] == 'zero' and list_cell[1] == 0:
                            who_turn(305, 75, 1)

                    # третя комірка        
                    elif 465 <= X_Y[0] <= 595 and 75 <= X_Y[1] <= 205:
                        if step[0] == 'cross'and list_cell[2] == 0:
                            who_turn(465, 75, 2)
                        elif step[0] == 'zero' and list_cell[2] == 0:
                            who_turn(465, 75, 2)
                        
                
                    #Другий рядок (3 комірки (горизонтально))
                    # четверта комірка 
                    if 150 <= X_Y[0] <= 280 and 233 <= X_Y[1] <= 363:
                        if step[0] == 'cross' and list_cell[3] == 0:
                            who_turn(150,233, 3)
                        elif step[0] == 'zero' and list_cell[3] == 0:
                            who_turn(150,233, 3)
                            
                    # п'ята комірка       
                    elif 305 <= X_Y[0] <= 435 and 233 <= X_Y[1] <= 363:
                        if step[0] == 'cross' and list_cell[4] == 0:
                            who_turn(305, 233, 4)
                        elif step[0] == 'zero' and list_cell[4] == 0: 
                            who_turn(305, 233, 4)

                    # шоста комірка        
                    elif 465 <= X_Y[0] <= 595 and 233 <= X_Y[1] <= 363:
                        if step[0] == 'cross' and list_cell[5] == 0:
                            who_turn(465, 233, 5)
                        elif step[0] == 'zero' and list_cell[5] == 0:
                            who_turn(465, 233 , 5)       

                    #Третій рядок (3 комірки (горизонтально))
                    # сьома комірка
                    if 150 <= X_Y[0] <= 280 and 390 <= X_Y[1] <= 520:
                        if step[0] == 'cross' and list_cell[6] == 0:
                            who_turn(150,390, 6)
                        elif step[0] == 'zero' and list_cell[6] == 0:
                            who_turn(150,390, 6)

                    # восьма комірка        
                    elif 305 <= X_Y[0] <= 435 and 390 <= X_Y[1] <= 520:
                        if step[0] == 'cross' and list_cell[7] == 0:
                            who_turn(305, 390, 7)
                        elif step[0] == 'zero' and list_cell[7] == 0:
                            who_turn(305, 390, 7)

                    # дев'ята комірка
                    elif 465 <= X_Y[0] <= 595 and 390 <= X_Y[1] <= 520:
                        if step[0] == 'cross'  and list_cell[8] == 0:
                            who_turn(465, 390, 8)
                        elif step[0] == 'zero' and list_cell[8] == 0:
                            who_turn(465, 390, 8)
                            
                
                def horizontal_win():
                    global count_win
                    global step_of_win
                    if count_win == 0:
                        # перемога для хрестика по горизонталі
                        # перший рядок
                        if list_cell[0] == 1 and list_cell[1] == 1 and list_cell[2] == 1:
                            screen.blit(cell1_win, (150, 75))
                            screen.blit(cell1_win, (305, 75))
                            screen.blit(cell1_win, (465, 75))
                                                    
                            # відображення хрестиків
                            screen.blit(list_cross[0], (150, 75))
                            screen.blit(list_cross[0], (305, 75))
                            screen.blit(list_cross[0], (465, 75))
                            count_win += 1
                            step_of_win = False
                            #cross_img.delete()
                            #pygame.quit()
                            #pygame.register_quit(start_game)
                            del list_cross[0]

                        # другий рядок
                        if list_cell[3] == 1 and list_cell[4] == 1 and list_cell[5] == 1:
                            screen.blit(cell1_win, (150, 233))
                            screen.blit(cell1_win, (305, 233))
                            screen.blit(cell1_win, (465, 233))

                            # відображення хрестиків
                            screen.blit(cross_img, (150, 233))
                            screen.blit(cross_img, (305, 233))
                            screen.blit(cross_img, (465, 233))
                            count_win += 1
                            step_of_win = False

                        # третій рядок
                        if list_cell[6] == 1 and list_cell[7] == 1 and list_cell[8] == 1:
                            screen.blit(cell1_win, (150, 390))
                            screen.blit(cell1_win, (305, 390))
                            screen.blit(cell1_win, (465, 390))

                            # відображення хрестиків
                            screen.blit(cross_img, (150, 390))
                            screen.blit(cross_img, (305, 390))
                            screen.blit(cross_img, (465, 390))
                            count_win += 1
                            step_of_win = False

                        # перемога для нулика по горизонталі
                        # перший рядок
                        elif list_cell[0] == 2 and list_cell[1] == 2 and list_cell[2] == 2:
                            screen.blit(cell1_win, (150, 75))
                            screen.blit(cell1_win, (305, 75))
                            screen.blit(cell1_win, (465, 75))

                            #відображення нуликів
                            screen.blit(zero_img, (150, 75))                    
                            screen.blit(zero_img, (305, 75))
                            screen.blit(zero_img, (465, 75))
                            count_win += 1
                            step_of_win = False
                            
                        # другий рядок
                        elif list_cell[3] == 2 and list_cell[4] == 2 and list_cell[5] == 2:
                            screen.blit(cell1_win, (150, 233))
                            screen.blit(cell1_win, (305, 233))
                            screen.blit(cell1_win, (465, 233))

                            #відображення нуликів
                            screen.blit(zero_img, (150, 233))
                            screen.blit(zero_img, (305, 233))
                            screen.blit(zero_img, (465, 233))
                            count_win += 1
                            step_of_win = False

                        # третій рядок
                        elif list_cell[6] == 2 and list_cell[7] == 2 and list_cell[8] == 2:
                            screen.blit(cell1_win, (150, 390))
                            screen.blit(cell1_win, (305, 390))
                            screen.blit(cell1_win, (465, 390))

                            #відображення нуликів
                            screen.blit(zero_img, (150, 390))
                            screen.blit(zero_img, (305, 390))
                            screen.blit(zero_img, (465, 390))
                            count_win += 1
                            step_of_win = False
                horizontal_win()


                def vertical_win():
                    global count_win
                    global step_of_win
                    if count_win == 0:
                        # перемога для хрестика по вертикалі
                        # перша колонка
                        if list_cell[0] == 1 and list_cell[3] == 1 and list_cell[6] == 1:
                            screen.blit(cell1_win, (150, 75))
                            screen.blit(cell1_win, (150, 233))
                            screen.blit(cell1_win, (150, 390))

                            # відображення хрестика
                            screen.blit(cross_img, (150, 75))
                            screen.blit(cross_img, (150, 233))
                            screen.blit(cross_img, (150, 390))
                            count_win += 1
                            step_of_win = False
                            
                        # друга колонка
                        if list_cell[1] == 1 and list_cell[4] == 1 and list_cell[7] == 1:
                            screen.blit(cell1_win, (305, 75))
                            screen.blit(cell1_win, (305, 233))
                            screen.blit(cell1_win, (305, 390))

                            # відображення хрестика
                            screen.blit(cross_img, (305, 75))
                            screen.blit(cross_img, (305, 233))
                            screen.blit(cross_img, (305, 390))
                            count_win += 1
                            step_of_win = False

                        # третя колонка 
                        if list_cell[2] == 1 and list_cell[5] == 1 and list_cell[8] == 1:
                            screen.blit(cell1_win, (465, 75))
                            screen.blit(cell1_win, (465, 233))
                            screen.blit(cell1_win, (465, 390))
                            
                            # відображення хрестика
                            screen.blit(cross_img, (465, 75))
                            screen.blit(cross_img, (465, 233))
                            screen.blit(cross_img, (465, 390))
                            count_win += 1
                            step_of_win = False

                        # перемога для нулика по вертикалі
                        # перша колонка
                        elif list_cell[0] == 2 and list_cell[3] == 2 and list_cell[6] == 2:
                            screen.blit(cell1_win, (150, 75))
                            screen.blit(cell1_win, (150, 233))
                            screen.blit(cell1_win, (150, 390))

                            # відображення нулика
                            screen.blit(zero_img, (150, 75))
                            screen.blit(zero_img, (150, 233))
                            screen.blit(zero_img, (150, 390))
                            count_win += 1
                            step_of_win = False

                        # друга колонка
                        elif list_cell[1] == 2 and list_cell[4] == 2 and list_cell[7] == 2:
                            screen.blit(cell1_win, (305, 75))
                            screen.blit(cell1_win, (305, 233))
                            screen.blit(cell1_win, (305, 390))

                            # відображення нулика
                            screen.blit(zero_img, (305, 75))
                            screen.blit(zero_img, (305, 233))
                            screen.blit(zero_img, (305, 390))
                            count_win += 1
                            step_of_win = False

                        # третя колонка
                        elif list_cell[2] == 2 and list_cell[5] == 2 and list_cell[8] == 2:
                            screen.blit(cell1_win, (465, 75))
                            screen.blit(cell1_win, (465, 233))
                            screen.blit(cell1_win, (465, 390))

                            # відображення нулика
                            screen.blit(zero_img, (465, 75))
                            screen.blit(zero_img, (465, 233))
                            screen.blit(zero_img, (465, 390))
                            count_win += 1
                            step_of_win = False
                vertical_win()


                def diagonal_win():
                    global count_win
                    global step_of_win
                    # перемога для хрестика по діагоналі
                    # перша діагональ
                    if count_win == 0:
                        if list_cell[0] == 1 and list_cell[4] == 1 and list_cell[8] == 1:
                            screen.blit(cell1_win, (150, 75))
                            screen.blit(cell1_win, (305, 233))
                            screen.blit(cell1_win, (465, 390))

                            # відображення хрестка
                            screen.blit(cross_img, (150, 75))
                            screen.blit(cross_img, (305, 233))
                            screen.blit(cross_img, (465, 390))
                            count_win += 1
                            step_of_win = False

                        # друга діагональ 
                        if list_cell[2] == 1 and list_cell[4] == 1 and list_cell[6] == 1:
                            screen.blit(cell1_win, (465, 75))
                            screen.blit(cell1_win, (305, 233))
                            screen.blit(cell1_win, (150, 390))

                            # відображення хрестка
                            screen.blit(cross_img, (465, 75))
                            screen.blit(cross_img, (305, 233))
                            screen.blit(cross_img, (150, 390))
                            count_win += 1
                            step_of_win = False

                        # перемога для нулика по діагоналі
                        # перша діагональ
                        elif list_cell[0] == 2 and list_cell[4] == 2 and list_cell[8] == 2:
                            screen.blit(cell1_win, (150, 75))
                            screen.blit(cell1_win, (305, 233))
                            screen.blit(cell1_win, (465, 390))

                            # відображення нулика
                            screen.blit(zero_img, (150, 75,))
                            screen.blit(zero_img, (305, 233,))
                            screen.blit(zero_img, (465, 390,))
                            count_win += 1
                            step_of_win = False
                            
                        # друга діагональ
                        elif list_cell[2] == 2 and list_cell[4] == 2 and list_cell[6] == 2:
                            screen.blit(cell1_win, (465, 75))
                            screen.blit(cell1_win, (305, 233))
                            screen.blit(cell1_win, (150, 390))
                            
                            # відображення нулика
                            screen.blit(zero_img, (465, 75,))
                            screen.blit(zero_img, (305, 233,))
                            screen.blit(zero_img, (150, 390,))
                            count_win += 1
                            step_of_win = False
                diagonal_win()

        pygame.display.flip()  
start_game()