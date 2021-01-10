# KMEANS ALGORITHM GUI
# BY @HOANGNDST 2020 AKA @ARCH-TECHS

import pygame

from random import randint
from sklearn.cluster import KMeans

import math

pygame.init()

def cre_tex_render(str):
    font = pygame.font.SysFont('sans', 30)
    return font.render(str, True, (255, 255, 255))
def cre_tex_render15(str):
    font = pygame.font.SysFont('sans', 15)
    return font.render(str, True, (255, 255, 255))

def distance (p1 , p2):
    return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))


screen = pygame.display.set_mode((1200, 700))

pygame.display.set_caption("Kmeans Algorithm")

running = True

clock = pygame.time.Clock()

# value
K = 0
points = []
clusters = [] #RANDOM Points
labels = []
#error = 0

# color
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

color_random = [green, red, blue, purple, yellow, cyan, black, white1]



# font

text_minus = cre_tex_render("-")
text_plus = cre_tex_render("+")
text_run = cre_tex_render15("R U N")
text_error = cre_tex_render15("E R R O R")
text_random = cre_tex_render15("R A N D O M")
text_algorithm = cre_tex_render15("USE ALGORITHM")
text_reset = cre_tex_render15("RESET")
text_num_of_points = cre_tex_render15("NUMBER OF POINTS")

while running:
    clock.tick(60)
    screen.fill(BACKGROUND)
# ------------------------------------------------------------------------------------------------------------
    # Draw UI
    # Draw REC
    pygame.draw.rect(screen, white, (10, 10, 1180, 600))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (11, 11, 1178, 598))

    # Draw K -
    pygame.draw.rect(screen, white, (50, 640, 30, 30))
    screen.blit(text_minus, (60, 635))
    # Draw rec1
    pygame.draw.rect(screen, white, (82, 640, 96, 30))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (83, 641, 94, 28))
    # Draw K +
    pygame.draw.rect(screen, white, (180, 640, 30, 30))
    screen.blit(text_plus, (186, 638))
    # K value
    font = pygame.font.SysFont('sans', 15)
    text_k = font.render("K   =   ", True, (255, 255, 255))
    value_k = font.render(str(K), True, (105, 255, 148))
    screen.blit(text_k, (105, 647))
    screen.blit(value_k, (148, 647))

# -----------------------------------------------------------------------------------------------------------
    # space = 50
    # RUN
    pygame.draw.rect(screen, (255, 255, 255), (180 + 30 + 50, 640, 80, 30))
    pygame.draw.rect(screen, white, (180 + 30 + 50 + 1, 641, 78, 28))
    screen.blit(text_run, (278, 647))
    # RANDOM
    pygame.draw.rect(screen, (255, 255, 255), (390, 640, 110, 30))
    pygame.draw.rect(screen, white, (390 + 1, 641, 108, 28))
    screen.blit(text_random, (400 + 2, 647))
    
    # NUMBER OF POINTS
    
    pygame.draw.rect(screen, (255, 110, 110), (550, 620, 180, 40))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (550 + 1, 621, 180 - 2, 40 - 2))
    pygame.draw.rect(screen, (255, 110, 110), (710, 620, 110, 40))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (711, 621, 110 - 2, 40 - 2))
    screen.blit(text_num_of_points, (555, 630))

    # ERROR
    temp = 35
    temp_y = 620 + 35
    pygame.draw.rect(screen, (255, 110, 110), (550, temp_y, 180, temp))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (550 + 1, temp_y + 1, 180 - 2, temp - 2))
    pygame.draw.rect(screen, (255, 110, 110), (710, temp_y, 110, temp))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (711, temp_y + 1, 110 - 2, temp - 2))
    screen.blit(text_error, (590, 665))
    # ALGORITHM
    pygame.draw.rect(screen, (255, 255, 255), (870, 640, 150, 30))
    pygame.draw.rect(screen, white, (870 + 1, 641, 150 - 2, 28))
    screen.blit(text_algorithm, (870 + 13, 647))
    # RESET
    pygame.draw.rect(screen, (255, 255, 255), (1070, 640, 80, 30))
    pygame.draw.rect(screen, white, (1070 + 1, 641, 80 - 2, 28))
    screen.blit(text_reset, (1085, 647))
    # END Draw UI
# ------------------------------------------------------------------------------------------------------------    
    # mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #print(mouse_x, mouse_y)
    # Draw mouse position
    if 11 < mouse_y < 11 + 598 and 11 < mouse_x < 11 + 1178:
        mouse_pos = font.render("[ " + str(mouse_x - 11) + " : " + str(mouse_y - 11) + " ]", True, (80, 250, 123))
        screen.blit(mouse_pos, (mouse_x + 15, mouse_y))
        pygame.draw.circle(screen, (255, 255, 255), (mouse_x, mouse_y), 5)


    # excute 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("EXIT")
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 11 < mouse_y < 11 + 598 and 11 < mouse_x < 11 + 1178:
                labels = []
                p = [mouse_x - 11, mouse_y - 11]
                points.append(p)

            # Click on K- button
            if 640 < mouse_y < 640 + 30 and 50 < mouse_x < 50 + 30:
                print("K- executed")
                if K > 0:
                    K = K - 1
            # Click on K+ button
            if 640 < mouse_y < 640 + 30 and 180 < mouse_x < 180 + 30:
                print("K+ executed")
                if K < 8:
                    K = K + 1
            
            # Click run
            if 640 < mouse_y < 640 + 30 and 180 + 30 + 50 < mouse_x < 180 + 30 + 50 + 80 and clusters != []:
                # Change points color look like the closest clusters ---------------------------------------
                labels = []
                for p in points:
                    distances_to_cl = []
                    for c in clusters:
                        dis = distance(p, c)
                        distances_to_cl.append(dis)
                    
                    min_distance = min(distances_to_cl)
                    labels.append(distances_to_cl.index(min_distance))
                # Change clusters position ------------------------------------------------------------------
                for i in range(len(clusters)):
                    sum_x = 0
                    sum_y = 0
                    count = 0
                    for j in range(len(points)):
                        if labels[j] == i:
                            sum_x = sum_x + points[j][0]
                            sum_y = sum_y + points[j][1]
                            count = count + 1

                    if count != 0:
                        clusters[i][0] = sum_x/count
                        clusters[i][1] = sum_y/count


                print("RUN executed")
           
            
            # Click random
            if 640 < mouse_y < 640 + 30 and 390 < mouse_x < 390 + 110:
                clusters = []
                labels = []
                for i in range(K):
                    cl = [randint(10, 1178 - 10), randint(10, 598 - 10)]
                    clusters.append(cl)
                print("RANDOM executed")
            # ERROR
            # ALGORITHM
            if 640 < mouse_y < 640 + 30 and 870 < mouse_x < 870 + 150:
                try:
                    kmeans =  KMeans(n_clusters = K).fit(points)
                    clusters = kmeans.cluster_centers_
                    labels = kmeans.predict(points)
                    print(kmeans.cluster_centers_)
                except:
                    print(" No points")
                print("ALGORITHM executed")

            # RESET
            if 640 < mouse_y < 640 + 30 and 1070 < mouse_x < 1070 + 80:
                points = []
                clusters = []
                labels = []
                K = 0
                print("RESET executed")
# -------------------------------------------------------------------------------------------------

    # Draw points
    for i in range(len(points)):
        pygame.draw.circle(screen, (255, 255, 255), (points[i][0] + 11, points[i][1] + 11), 8)
        if labels == []:
            pygame.draw.circle(screen, BACKGROUND_PANEL, (points[i][0] + 11, points[i][1] + 11), 7)
        else:
            pygame.draw.circle(screen, color_random[labels[i]], (points[i][0] + 11, points[i][1] + 11), 7)

    # Draw RANDOM points
    for i in range(len(clusters)):
        pygame.draw.circle(screen, (10, 10, 10), (int(clusters[i][0]) + 11, int(clusters[i][1]) + 11), 11)
        pygame.draw.circle(screen, color_random[i], (int(clusters[i][0]) + 11, int(clusters[i][1]) + 11), 8)

    # ERROR
    error = 0

    if labels != [] and clusters != []:
        for i in range(len(points)):
            error = error + int(distance(points[i], clusters[labels[i]]))
        ERROR = font.render(str(error), True, red)
        screen.blit(ERROR, (745, 664))
    # NUMBER OF POINTS
    NUM = cre_tex_render15(str(len(points)))
    screen.blit(NUM, (755, 630))

    pygame.display.flip()

pygame.quit()

