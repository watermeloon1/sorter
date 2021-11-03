import pygame
import random
import time
import numpy

from pygame.constants import KEYDOWN, KEYUP, MOUSEBUTTONDOWN, TIMER_RESOLUTION

pygame.init()

color_black = (0,0,0)
color_white = (255,255,255)
color_blue = (0,0,255)
color_dark =(100,100,100)
color_darker = (150,150,150)
color_red =(227,38,54)
color_purple =(80,0,80)

#window parameters
window_width = 1920
window_height = 1080

#sets sreen
screen = pygame.display.set_mode((window_width,window_height))
caprion = pygame.display.set_caption("sorter")
screen.fill(color_white)

game_exit = False
clock = pygame.time.Clock()
fps = 240
sorted_state = False
sorting_state = False
calculated = 0

#x coorinates, y coordinates, width, height
refresh_button = [20,20,140,40]
selection_button = [300,20,140,40]
bubble_button = [460,20,140,40]
insertion_button = [620,20,140,40]
quick_button = [780,20,140,40]
merge_button = [940,20,140,40]
heap_button = [1100,20,140,40]
gnome_button = [1260,20,140,40]
bogo_button = [1420,20,140,40]
exit_button = [1860,20,40,40]

DATA = []
DATA_length = 360

#returns a random pillar height
def RANDOM():
    return [random.randrange(1, (window_height/3)*2)]

#swap two values in a list
def swap(list,pos1,pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]

#fills up the array with random numbers
def DATA_fill():
    for x in range(DATA_length):
        extension = [2*x+1]
        DATA.extend(extension)
    random.shuffle(DATA)

#draws the pillars
def draw_pillars():
    pygame.draw.rect(screen, color_white,[0, 60, 1920, 1760])
    global length
    length = len(DATA)
    for i in range(length):
        pygame.draw.rect(screen, color_blue,
        [window_width/length*(i+.05)-1.5, window_height-DATA[i], 3, DATA[i]])

#paints the pillars red for a second
def red_pillars():
    for i in range(length):
        pygame.draw.rect(screen, color_red,
        [window_width/length*(i+.05)-1.5, window_height-DATA[i], 3, DATA[i]])
        pygame.display.update()

    time.sleep(.8)

#draws the buttons
def draw_button():

    if sorting_state or sorted_state:
        color = color_darker
    else: color = color_dark
    
    #number of calculations
    """
    global calculated
    calc_font = pygame.font.SysFont('Times New Roman', 25)
    calc_str = str(calculated)
    calc_text = calc_font.render(calc_str + " comparisons",  True, color_black)
    screen.blit(calc_text , (20,80))
    """

    #REFRESH BUTTON
    refresh_font = pygame.font.SysFont('Times New Roman', 30)
    refresh_text = refresh_font.render('refresh',  True, color_white)
    pygame.draw.rect(screen,color_purple,refresh_button)
    screen.blit(refresh_text , (48,23))

    #SELECTION SORT BUTTON
    selection_font = pygame.font.SysFont('Times New Roman', 25)
    selection_text = selection_font.render('selection',  True, color_white)
    pygame.draw.rect(screen,color,selection_button)
    screen.blit(selection_text , (325,25))

    #BUBBLE SORT BUTTON
    bubble_font = pygame.font.SysFont('Times New Roman', 25)
    bubble_text = bubble_font.render('bubble',  True, color_white)
    pygame.draw.rect(screen,color,bubble_button)
    screen.blit(bubble_text , (495,25))

    #INSERTION SORT BUTTON
    insertion_font = pygame.font.SysFont('Times New Roman', 25)
    insertion_text = insertion_font.render('insertion',  True, color_white)
    pygame.draw.rect(screen,color,insertion_button)
    screen.blit(insertion_text , (645,25))

    #QUICK SORT BUTTON
    quick_font = pygame.font.SysFont('Times New Roman', 25)
    quick_text = quick_font.render('quick',  True, color_white)
    pygame.draw.rect(screen,color,quick_button)
    screen.blit(quick_text , (820,25))

    #MERGE SORT BUTTON
    merge_font = pygame.font.SysFont('Times New Roman', 25)
    merge_text = merge_font.render('merge',  True, color_white)
    pygame.draw.rect(screen,color,merge_button)
    screen.blit(merge_text , (980,25))

    #HEAP SORT BUTTON
    heap_font = pygame.font.SysFont('Times New Roman', 25)
    heap_text = heap_font.render('heap',  True, color_white)
    pygame.draw.rect(screen,color,heap_button)
    screen.blit(heap_text , (1145,25))

    #GNOME SORT BUTTON
    gnome_font = pygame.font.SysFont('Times New Roman', 25)
    gnome_text = gnome_font.render('gnome',  True, color_white)
    pygame.draw.rect(screen,color,gnome_button)
    screen.blit(gnome_text , (1295,25))

    #BOGO SORT BUTTON
    bogo_font = pygame.font.SysFont('Times New Roman', 25)
    bogo_text = bogo_font.render('bogo',  True, color_white)
    pygame.draw.rect(screen,color,bogo_button)
    screen.blit(bogo_text , (1463,25))

    #EXIT BUTTON
    exit_font = pygame.font.SysFont('Times New Roman', 40)
    exit_text = exit_font.render('x',  True, color_white)
    pygame.draw.rect(screen,color_red,exit_button)
    screen.blit(exit_text , (1871,14))

#SELECTION SORT
def selection_sort():

    length = len(DATA)
    for i in range(length):
        min_index = i
        
        for j in range(i+1, length):
            if DATA[j] < DATA[min_index]:
                min_index = j
            
        pygame.draw.rect(screen, color_red,[window_width/length*(i+.05)-1.5, window_height-DATA[i], 3, DATA[i]])
        pygame.draw.rect(screen, color_red,[window_width/length*(min_index+.05)-1.5, window_height-DATA[min_index], 3, DATA[min_index]])
        pygame.display.update()
        
        swap(DATA,i,min_index)
        draw_pillars()
        draw_button()

        pygame.display.update()

    red_pillars()

#BUBBLE SORT !!PIROS!!
def bubble_sort():

    length = len(DATA)
    for i in range(length-1):
        for j in range(length-i-1):
            if DATA[j] > DATA[j+1]:
                swap(DATA,j,(j+1))

        draw_pillars()
        draw_button()

        pygame.display.update()  

    red_pillars()

#INSERTION SORT
def insertion_sort():

    length = len(DATA)
    for i in range(1,length):
        
        key = DATA[i]
        j = i-1
        while j >= 0 and key < DATA[j]:
            
            DATA[j+1] = DATA[j]
            j-=1
            DATA[j+1] = key
        
        if i != length-1:
            pygame.draw.rect(screen, color_red,[window_width/length*(i+1.05)-1.5, window_height-DATA[i+1], 3, DATA[i+1]])
            pygame.draw.rect(screen, color_red,[window_width/length*(j+.05)-1.5, window_height-DATA[j], 3, DATA[j]])
            pygame.display.update()

        draw_pillars()
        draw_button()

        pygame.display.update()

    red_pillars()

#QUICK SORT
def quick_sort(array, low_index,high_index):
    
    draw_button()

    if low_index <  high_index:
        pivot = partition(array,low_index,high_index)
        draw_pillars()
        draw_button()

        pygame.display.update()
        quick_sort(array,low_index,pivot-1)
        quick_sort(array,pivot+1,high_index)

#partition for quick sort
def partition(array, low_index,high_index):

    i = (low_index-1)        
    pivot = array[high_index]     
    for j in range(low_index, high_index):
        if array[j] <= pivot:

            i = i+1
            swap(array,i,j)

            draw_pillars()
            pygame.display.update()

            pygame.draw.rect(screen, color_red,[window_width/length*(i+.05)-1.5, window_height-DATA[i], 3, DATA[i]])
            pygame.draw.rect(screen, color_red,[window_width/length*(j+.05)-1.5, window_height-DATA[j], 3, DATA[j]])
            pygame.display.update()
  
    swap(array,i+1,high_index)
    return (i+1)

#MERGE SORT  !!PIROS!!
def merge_sort(array, left_index,right_index):

    if left_index < right_index:

        middle_index = left_index + (right_index-left_index)//2

        merge_sort(array,left_index,middle_index)
        merge_sort(array,middle_index + 1, right_index)
        merge(array,left_index, middle_index,right_index)

        draw_pillars()
        draw_button()
        pygame.display.update()

#merges the to halves
def merge(array, left_index,middle_index,right_index):
    n1 = middle_index -left_index +1
    n2 = right_index - middle_index

    LEFT = [0] *(n1)
    RIGHT = [0] *(n2)

    for i in range(0,n1):
        LEFT[i] = array[left_index + i]


    for j in range(0,n2):
        RIGHT[j] = array[middle_index + 1 + j]


    i = 0
    j = 0
    k = left_index

    while i < n1 and j< n2:
        if LEFT[i] <= RIGHT[j]:
            array[k] = LEFT[i]
            i += 1
        else:
            array[k] = RIGHT[j]
            j += 1
        k += 1
    
        draw_pillars()
        pygame.display.update()

    while i < n1:
        array[k] = LEFT[i]
        i +=  1
        k += 1

    while j < n2:
        array[k] = RIGHT[j]
        j +=  1
        k += 1

#creates the heaps
def heapify(array, n, i):
    max = i

    left_child = 2*i +1
    right_child = 2*i +2

    if left_child < n and array[i] < array[left_child]:
        max = left_child
    
    if right_child < n and array[max] < array[right_child]:
        max = right_child

    if max != i:
        swap(array,i,max)
        heapify(array,n,max)

        draw_button()
        draw_pillars()
        pygame.display.update()

#HEAP SORT
def heap_sort(array):

    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array,n, i)

    for i in range(n-1, 0, -1):
        swap(array,i,0)

        heapify(array,i,0)

#optimalises the gnome sort
def gnome_opt(upper_bound):

    position = upper_bound
    while position > 0 and DATA[position] < DATA[position-1]:
        swap(DATA,position,position-1)
        
        position  -= 1

#GNOME SORT
def gnome_sort():
    for i in range(len(DATA)):
        gnome_opt(i)

        pygame.draw.rect(screen, color_red,[window_width/length*(i+.05)-1.5, window_height-DATA[i], 3, DATA[i]])
        pygame.display.update()

        draw_button()
        draw_pillars()
        pygame.display.update()

#returns the maximum of the list
def maximum(array):
    maximum = array[0]
    for i in range(len(array)):
        if maximum < array[i]:
            maximum = array[i]
    return maximum

def maximum_index(array):
    maximum = 0
    end = len(array)
    for i in range(0,end):
        if array[maximum] < array[i]:
            maximum = i
    return maximum

def minimum(array):
    minimum = array[0]
    for i in range(len(array)):
        if minimum > array[i]:
            minimum = array[i]
    return minimum

def minimum_index(array):
    minimum = 0
    end = len(array)
    for i in range(0,end):
        if array[minimum] > array[i]:
            minimum = i
    return minimum

#checks if the array is sorted
def check(array):

    for i in range(0,len(array)-1):
        if array[i] > array[i+1]:
            print("INDEX1: " + str(i))
            print("INDEX1: " + str(i+1))
            return False           
                    
    return True

#BOGO SORT
def bogo_sort(array):
    
    while not check(array):
        global calculated
        calculated += 1

        if calculated == 750:
            break

        numpy.random.shuffle(array)
        draw_pillars()
        draw_button()
        pygame.display.update()
        print(calculated)

def compare(array, pos1,pos2):
    if array[pos1] == array[pos2]:
        return True
    else:
        return False

#def swap_sort(array):
    
#initialises the game
def game_init():

    draw_pillars()
    draw_button()

#refreshes game
def game_refresh():
    draw_pillars()
    TEMP = []
    TEMP_length = 360

    for x in range(TEMP_length):
        extension = [2*x+1]
        TEMP.extend(extension)

    for z in range(TEMP_length):
        DATA[z] = TEMP[z]

    random.shuffle(DATA)
    
    global sorted_state
    sorted_state = False
    
DATA_fill()

#GAME LOOP
while not game_exit:

    game_init()

    for event in pygame.event.get():

        mouse_position = pygame.mouse.get_pos()
    
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == MOUSEBUTTONDOWN and not sorted_state and not sorting_state :

            if selection_button[0] < mouse_position[0] < selection_button[0]+selection_button[2] and selection_button[1] < mouse_position[1] < selection_button[1]+selection_button[3]:
                sorting_state = True
                selection_sort()
                sorting_state = False
                sorted_state = True

            if bubble_button[0] < mouse_position[0] < bubble_button[0]+bubble_button[2] and bubble_button[1] < mouse_position[1] < bubble_button[1]+bubble_button[3]:
                sorting_state = True
                bubble_sort()
                sorting_state = False
                sorted_state = True

            if insertion_button[0] < mouse_position[0] < insertion_button[0]+insertion_button[2] and insertion_button[1] < mouse_position[1] < insertion_button[1]+insertion_button[3]:
                sorting_state = True
                insertion_sort()
                sorting_state = False
                sorted_state = True

            if quick_button[0] < mouse_position[0] < quick_button[0]+quick_button[2] and quick_button[1] < mouse_position[1] < quick_button[1]+quick_button[3]:
                sorting_state = True
                quick_sort(DATA,0,length-1)
                red_pillars()
                sorting_state = False
                sorted_state = True

            if merge_button[0] < mouse_position[0] < merge_button[0]+merge_button[2] and merge_button[1] < mouse_position[1] < merge_button[1]+merge_button[3]:
                sorting_state = True
                merge_sort(DATA,0,length-1)
                red_pillars()
                sorting_state = False
                sorted_state = True

            if heap_button[0] < mouse_position[0] < heap_button[0]+heap_button[2] and heap_button[1] < mouse_position[1] < heap_button[1]+heap_button[3]:
                sorting_state = True
                heap_sort(DATA)
                pygame.display.update()
                red_pillars()
                sorting_state = False
                sorted_state = True

            if gnome_button[0] < mouse_position[0] < gnome_button[0]+gnome_button[2] and gnome_button[1] < mouse_position[1] < gnome_button[1]+gnome_button[3]:
                sorting_state = True
                gnome_sort()
                red_pillars()
                sorting_state = False
                sorted_state = True

            if bogo_button[0] < mouse_position[0] < bogo_button[0]+bogo_button[2] and bogo_button[1] < mouse_position[1] < bogo_button[1]+bogo_button[3]:
                sorting_state = True
                bogo_sort(DATA)
                sorting_state = False
                sorted_state = True

        if event.type == MOUSEBUTTONDOWN and not sorting_state and sorted_state:
            if refresh_button[0] < mouse_position[0] < refresh_button[0]+refresh_button[2] and refresh_button[1] < mouse_position[1] < refresh_button[1]+refresh_button[3]:
                
                game_refresh()
                sorted_state = False

        if event.type == MOUSEBUTTONDOWN:
            if exit_button[0] < mouse_position[0] < exit_button[0]+exit_button[2] and exit_button[1] < mouse_position[1] < exit_button[1]+exit_button[3]:

                game_exit = True

        if event.type == KEYDOWN:
            #swap_sort(DATA)
            ()
            
        pygame.display.update()
        clock.tick(fps)
        
pygame.quit()
quit()

#HULLÁMOS RENDEZÉS
#BEHAVIOURAL SORT "Particle swarm optimization"