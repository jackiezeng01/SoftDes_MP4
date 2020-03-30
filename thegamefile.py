"""
Micro Project 4
"""

import pygame
import cv2

# this is the main file for the project with all of the classes and functions that will be called

# hypothetical x positions of lanes.
global LEFT_LANE = 50
global MIDDLE_LANE = 100
global RIGHT_LANE = 150
global TOP_Y = 0
global BOTTOM_Y = 0
obstacles = [] #This stores all obstacles in a list and loops through the list
#to draw each one
pygame.time.set_timer(USEREVENT+1, random.randrange(2000, 3500)) # Will trigger
# every 2 - 3.5 seconds. This is the timer that sets off obstacle generation.

class Runner():
#creates a class for the character in the game
    def __init__(self, background, x = MIDDLE_LANE, y = BOTTOM_Y, lives = 3):
        '''
        initilizes the character with a starting x position. y position is at the
        Bottom of the page because the background moves and not the character.

        background: image
        x: initial x position (int)
        y: initial y position (int)
        lives: int
        '''
        pass
    def draw(self):
        '''
        Draws the character on the screen with the appropriate size and position.
        '''
        pass
    def move(self, direction):
        '''
        Moves runner in the direction specified by the OpenCV camera
        feedback. Changes the x location of the character to one of the
        three global lane variables.

        direction: data from OpenCV that dictates left, right, or straight
            if direction == "left" and self.x != LEFT_LANE:
                self.x += -50
            if direction == "right" and self.x != RIGHT_LANE:
                self.x += 50
            if direction == "straight":
                pass
        '''
        pass
    def minus_life(self):
        '''
        Subtracts one from life of the Runner.
        '''
        pass

class Obstacles():
#creates a class that for the obstacles
    def __init__(self, background, x, y=TOP_Y):
        '''
        initilizes the obstacle with a starting x position. y position is at the
        top of the page because it will move downwards.

        background: image
        x: random lane that will be inputted when generated (int)
        y: initial y position (int)
        '''
        pass
    def draw(self):
        '''
        draws obstacle on the screen
        '''
        pass
    def move(self):
        '''
        keeps obstacle on the same lane while increasing the y position so it
        moves down the screen towards the player.
        '''
        pass

def redrawWindow():
    '''
    redraws elements so that it can update every frame

    draws the following:
    background
    Runner
    Loops through every obstacle in the obstacles list, draw it in the window.
    '''
    #code drawing stuff.
    pygame.display.update()
    pass

class Game():
    def __init__(self):
        '''
        initializes attributes of the game:

        Frames per second
        Clock
        Background
        Size of screen
        Creates Runner class
        Creates Obstacles class
        '''
        Runner = Runner(background)
    def run(self):
        '''
        Runs the game and updates frames
        '''
        RUNNING = true
        while RUNNING:
            #if lives is less than 0, then RUNNING becomes false

            # updates frame with all of the new drawings
            redrawWindow()

            #moves runner based on direction of open cv arrows
            Runner.move(read_card())

            #generate obstacles if userevent timer is true.
            if event.type == USEREVENT+1:
                r = random.randrange(0,3)
                if r == 0:
                    obstacles.append(Obstacles(background, x = LEFT_LANE))
                elif r == 1:
                    obstacles.append(Obstacles(background, x = MIDDLE_LANE))
                elif r == 2:
                    obstacles.append(Obstacles(background, x = RIGHT_LANE))

            #moves obstacles: updates obstacle position or removes it if it
            #goes off the screen.
            for obstacle in obstacles:
                obstacles.move()
                # If our obstacle is off the screen we will remove it
                 if obstacle.x < obstacle.width * -1:
                     obstacles.pop(obstacles.index(obstacle))

            # insert code that manages collisions: if it touches the player
            # then the obstacle deletes, the player loses a life, the player's
            # turn starts over

def read_card():
    # if open cv reads left arrow
        return "left"
    # if open cv reads right arrow
        return "right"
    # if open cv does not read anything
        return "stay"

test = True

class Camera(): #not finished but close, lol
    '''
    Class containing all gathering of data from the Camera feed.
    designed to have minimal interpreting in this class and instead interface
    with another class to find the meaning in the image data.
    '''
    def __init__(self, left, right):

        # initalize the feed
        self.cap = cv2.VideoCapture(0)

        # create the ORB data from images to check the feed with
        self.leftORB = init_templates(left)
        self.rightORB = init_template(right)

        # check that camera is available
        if not (self.cap.isOpened()):
            print('No camera detected,\n please run with a Camera')

        # generate the ORBs templates for the left and right pointing arrows

    def orbs_filter(self, temp):
        # save the template image
        self.img = cv2.imread(temp, 0)

        # turn on ORB detector
        self.orb = cv2.ORB_create()

        # find the keypoints with ORB
        self.keypoints = orb.detect(self.img, None)

        # find the descriptors with ORB
        self.keypoints, self.descriptor = orb.detectAndCompute(self.img, self.keypoints)

        # draw keypoints' location
        self.orbtemplate = cv2.drawKeypoints(self.img, self.keypoints, None, color=(0,255,0), flags=0)

        return self.orbtemplate

    def get_feed(self):
        '''
        This function returns the video feed after converting it to a grayscale for further interpreting
        '''

        # while the camera may be on, the camera could be reading a file or feed type
        # that it cannot handle this double checks that the input type is correct.
        self.everythingGood, self.frame = cap.read()
        if self.everythingGood == True:

            # Converting the Video frame into a grayscale image
            self.grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return self.grayscale

    def image_converter(self, image, EdgeThres = (100, 255), pMatches = 300):

            # using the CannyEdge Detector to simply image and store it
            self.edge = cv2.Canny(image, EdgeThres[0], EdgeThres[1])

            # using ORBs detection to
            self.orbprocessed = cv2.orbs_filter(image)

            # Since this uses a lot of external input a testing function is made to clarify
            # what it is that the edge dectectors are finding
            if test:
                # Unfiltered Video Feed
                cv2.imshow('Real', self.frame)
                # Filtered Video Feed
                cv2.imshow('Edge', self.edge)
                # ORB filtered Video Feed
                cv2.imshow('ORBs', self.orbprocessed)
                # Escape the Video feed, and properly(?) close the windows/camera
                if cv2.waitKey(20) == ord('q'):
                    break
def __main__():
