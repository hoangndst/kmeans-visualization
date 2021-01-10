# IMAGE COMPRESSION USING KMEANS ALGORITHM 
# BY @HOANGNDST 2020 AKA @ARCH-TECHS


from numpy.core.numeric import convolve
from pygame import display, image, mouse, surfarray
from pygame.constants import MOUSEBUTTONDOWN
from sklearn import cluster
from sklearn.cluster import KMeans
import pygame
import numpy


pygame.init()

screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Image Compression")
font = pygame.font.SysFont('sans', 15)
usr_text = ""
K = ""
save_name = ""
clock = pygame.time.Clock()

running = True


#---------------------------------------------
# COLOR 
BACKGROUND = (40, 42, 54)
BACKGROUND_PANEL = (33, 34, 44)
white = (125, 125, 125)
white1 = (225, 225, 225)
black = (0, 0, 0)
blue = (35, 165, 255)
cyan = (139, 233, 253)
green = (80, 250, 123)
purple = (255, 121, 198)
red = (255, 85, 85)
yellow = (241, 250, 140)
gray = (100, 100, 100)
# IMAGE

# KMEANS ALGORITHM
inputtext = False
input_image = False

save = False
save_in = False
K_in = False
K_input = False

condition_to_cv = False
convert = False

a_img_in = 0
b_img_in = 0
img_in_x_pos = 15
img_in_y_pos = 0

a_img2 = 0
b_img2 = 0
img2_x_pos = 1200 - 15 - 550
img2_y_pos = 0

image_2 = numpy.zeros((10, 10, 3), dtype = numpy.uint8)  
array_in = numpy.zeros((10, 10, 3), dtype = numpy.uint8)

# WHILE RUNNING -------------------------------------------------
while running:
    clock.tick(60)
    screen.fill(BACKGROUND_PANEL)
    # KMEANS ALGORITHM
     
    # DRAW UI --------------------------------------------------------------------------------

    # IMAGE IN-OUT BACKGROUND
    pygame.draw.rect(screen, white1, (15 - 1, 50, 560 - 9, 401))
    pygame.draw.rect(screen, white1, (1200 - 15 - 550 - 1, 50, 560 - 9, 401))
    pygame.draw.rect(screen, black, (15, 50, 550, 400))
    pygame.draw.rect(screen, black, (1200 - 15 - 550, 50, 550, 400))
    #
    #
    # BUTTOM 
    pygame.draw.rect(screen, white1, (30 - 1, 500 - 1, 200 + 2, 40 + 2))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (30, 500, 200, 40))
    text_name = font.render("Type image's name...", True, gray)
    screen.blit(text_name, (50, 510))
    
    pygame.draw.rect(screen, white1, (425 - 1, 500 - 1, 100 + 2, 40 + 2))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (425, 500, 100, 40))
    text1 = font.render("RESET", True, blue)
    screen.blit(text1, (447, 512))

    pygame.draw.rect(screen, white1, (240 - 1, 500 - 1, 80 + 2, 40 + 2))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (240, 500, 80, 40))
    text2 = font.render("INPUT", True, white1)
    screen.blit(text2, (257, 512))
    
    pygame.draw.rect(screen, white1, (1200 - 100 - 100 - 1, 500 - 1, 150 + 2, 40 + 2))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (1200 - 100 - 100, 500, 150, 40))
    text3 = font.render("CONVERT", True, white1)
    screen.blit(text3, (1035, 512))
    
    pygame.draw.rect(screen, white1, (666 - 1, 500 - 1, 150 + 2, 40 + 2))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (666, 500, 150, 40))
    text4 = font.render("INPUT K", True, gray)
    screen.blit(text4, (700 + 5, 512))
    
    pygame.draw.rect(screen, white1, (666 + 150 + 10 - 1, 500 - 1, 80 + 2, 40 + 2))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (666 + 150 + 10, 500, 80, 40))
    text5 = font.render("INPUT", True, white1)
    screen.blit(text5, (843, 512))

    pygame.draw.rect(screen, white1, (400 - 1, 620 - 1, 200 + 2, 40 + 2))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (400, 620, 200, 40))
    text1 = font.render("Type image's name...", True, gray)
    screen.blit(text1, (425, 630))

    pygame.draw.rect(screen, white1, (400 + 200 + 10 - 1, 620 - 1, 80 + 2, 40 + 2))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (400 + 200 + 10, 620, 80, 40))
    text_save = font.render("SAVE", True, white1)
    screen.blit(text_save, (628, 632))

    # INPUT
    image_in_surf = pygame.surfarray.make_surface(array_in)
    image_in_surf = pygame.transform.scale(image_in_surf, (int(a_img_in), int(b_img_in)))
    screen.blit (image_in_surf, (img_in_x_pos, img_in_y_pos))


    # OUTPUT
    if convert == True:
        image_2_surf = pygame.surfarray.make_surface(image_2)
        image_2_surf_out = pygame.transform.scale(image_2_surf, (a_img_in, b_img_in))
        screen.blit(image_2_surf_out, (img2_x_pos, img2_y_pos))
        pygame.draw.rect(screen, green, (1200 - 100 - 100 - 1, 500 - 1, 150 + 2, 40 + 2))
        pygame.draw.rect(screen, BACKGROUND_PANEL, (1200 - 100 - 100, 500, 150, 40))
        text3 = font.render("CONVERTED", True, white1)
        screen.blit(text3, (1030, 512))
        
    if inputtext == True:
        pygame.draw.rect(screen, black, (30, 500, 200, 40))
        text = font.render(usr_text, True, (225, 225, 225))
        screen.blit(text, (50, 510))
    if K_in == True:
        pygame.draw.rect(screen, black, (666, 500, 150, 40))
        text_k_in = font.render(K, True, white1)
        screen.blit(text_k_in, (700 + 5, 512))
    if save_in == True:
        pygame.draw.rect(screen, black, (400, 620, 200, 40))
        text_save_name = font.render(save_name, True, white1)
        screen.blit(text_save_name, (425, 630))      
    # END DRAW UI

    # GET MOUSE_POS
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # print(str(mouse_x) + " " + str(mouse_y))
    # EXCUTE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
           # INPUT IMAGE'S NAME
            if 30 < mouse_x < 30 + 200 and 500 < mouse_y < 540:
                inputtext = True
                input_image = False
            else:
                inputtext = False
            # RESET

            if 425 < mouse_x < 425 + 100 and 500 < mouse_y < 540:
                K = ""
                usr_text = ""
                save_name = ""
                inputtext = False
                input_image = False

                K_in = False
                K_input = False

                condition_to_cv = False
                convert = False

                a_img_in = 0
                b_img_in = 0
                img_in_x_pos = 15
                img_in_y_pos = 0

                a_img2 = 0
                b_img2 = 0
                img2_x_pos = 1200 - 15 - 550
                img2_y_pos = 0

                image_2 = numpy.zeros((10, 10, 3), dtype = numpy.uint8)  
                array_in = numpy.zeros((10, 10, 3), dtype = numpy.uint8) 

            # TYPE K
            if 666 < mouse_x < 666 + 150 and 500 < mouse_y < 540:
                K_in = True
            else:
                K_in = False
            # INPUT K BUTTON
            if 666 + 150 + 10 < mouse_x < 666 + 150 + 10 + 80 and 500 < mouse_y < 540:
                K_input = True
            # INPUT IMAGE BUTTON
            if 240 < mouse_x < 240 + 80 and 500 < mouse_y < 540:
                K = ""
                input_image = True
            else:
                input_image = False 
            # CONVERT BUTTON
            if 1000 < mouse_x < 1000 + 150 and 500 < mouse_y < 540 and K_input == True:
                try:
                    
                    image = pygame.image.load(usr_text)
                    array = pygame.surfarray.pixels3d(image)
                    width = array.shape[0]
                    height = array.shape[1]
                    array = array.reshape(width * height, 3)
                    image_2 = numpy.zeros((width, height, 3), dtype = numpy.uint8)                        
                    kmeans = KMeans(n_clusters = int(K)).fit(array)
                    labels = kmeans.predict(array)
                    clusters = kmeans.cluster_centers_
                    index = 0
                    for i in range(width):
                        for j in range(height):
                            image_2[i][j] = clusters[labels[index]]
                            index += 1
                    K_input = False
                    convert = True
                except:
                    K_input = False
            # IMAGE NAME TO SAVE
            if 400 < mouse_x < 600 and 620 < mouse_y < 620 + 40:
                save_in = True
            else:
                save_in = False
            if 620 < mouse_x < 620 + 80 and 620 < mouse_y < 620 + 40:
                save = True
            else:
                save = False
            
        if inputtext == True:        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    usr_text = usr_text
                elif event.key == pygame.K_BACKSPACE:
                    usr_text = usr_text[:-1]
                else:
                    usr_text += event.unicode
        if K_in == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    K = K
                elif event.key == pygame.K_BACKSPACE:
                    K = K[:-1]
                else:
                    K += event.unicode
        if save_in == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    save_name = save_name
                elif event.key == pygame.K_BACKSPACE:
                    save_name = save_name[:-1]
                else:
                    save_name += event.unicode
    if input_image == True:
        try:
            image_2 = numpy.zeros((10, 10, 3), dtype = numpy.uint8) 
            pygame.draw.rect(screen, green, (240 - 1, 500 - 1, 80 + 2, 40 + 2))
            pygame.draw.rect(screen, BACKGROUND_PANEL, (240, 500, 80, 40))
            text2 = font.render("INPUT", True, white1)
            screen.blit(text2, (257, 512))
            
            image_in = pygame.image.load(usr_text)
            array_in = pygame.surfarray.pixels3d(image_in)
            
            width = array_in.shape[0]
            height = array_in.shape[1]
            
            # POS Mission
            if width > height:
                a_img_in = 550
                if width < 500:
                    b_img_in = int((width / 550) * height)
                if width >= 500:
                    b_img_in = int((500 / width) * height)
                img_in_y_pos = 50 + 400 - b_img_in
                img2_y_pos = img_in_y_pos
            if height > width:
                b_img_in = 400
                if height < 400:
                    a_img_in = int((height / 400) * width)
                if height >= 400:
                    a_img_in = int((400 / height) * width)
                img_in_y_pos = 50
                img2_y_pos = img_in_y_pos
        except:
            pygame.draw.rect(screen, black, (30, 500, 200, 40))
            text_er = font.render("NOT FOUND", True, red)
            screen.blit(text_er, (52, 512))
    if save == True:
        out = pygame.surfarray.make_surface(image_2)
        pygame.image.save(out, save_name + ".png")
        
        pygame.draw.rect(screen, green, (400 + 200 + 10 - 1, 620 - 1, 80 + 2, 40 + 2))
        pygame.draw.rect(screen, BACKGROUND_PANEL, (400 + 200 + 10, 620, 80, 40))
        text_save = font.render("SAVED", True, white1)
        screen.blit(text_save, (627, 632))

    pygame.display.flip()
    # print(save)

pygame.quit()
