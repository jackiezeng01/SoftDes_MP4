"""
Micro Project 4
"""

import pygame
import cv2

# this is the main file for the project with all of the classes and functions that will be called

# hypothetical x positions of lanes.
global left_lane = 50
global middle_lane = 100
global right_lane = 150
global top_y = 0

class Runner():
#creates a class for the character in the game
    def __init__(self, screen, x = middle_lane, y = 150):
        #initilizes the character with a starting x position. y position is at the
        #bottom of the page because the background moves not the character.
    def draw(self):
        #draws the character on the screen
    def move(self, direction):
        ''' Moves runner in the direction specified by the OpenCV camera
            feedback. Changes the x location of the character to one of the
            three global lane variables.

            self: the runner
            direction: string saying either "left", "right", or "no change"
        '''
    pass

class Obstacles():
#creates a class that for the obstacles
    def __init__(self, screen, x, y=0):
        #initilizes each obstacle with an x (one of the three lanes) & y
        #position
    def draw(self):
        #draws obstacle on the screen
    def move(self):
        #keeps obstacle on the same lane while increasing the y position so it
        #moves down the screen towards the player.
    pass

class Timer():
#creates a timer that serves
    def __init__(self, minute=0, second=0, millisecond=0):

    pass


class Best_Time():
#class to save the high score/best time
    pass


class Game():
    def __init__(self):
        '''

        '''
        self.FPS = 25

        pygame.init()

        self.fpsClock = pygame.time.Clock()

        self.background = pygame.image.load('background.jpg')
        self.size = self.width, self.height = self.background.get_size()

        self.screen = pygame.display.set_mode(self.size,0,32)

        self.ball = Ball(self.screen, 100, 100)

        self.player1 = Player(self.screen, 35, self.height/2)
        self.player2 = Player(self.screen, self.width-35, self.height/2)

        print self.screen.get_rect().center


        font = pygame.font.SysFont("", 72)

        self.text_paused = font.render("PAUSE", True, (255, 0, 0))

        print self.text_paused.get_rect()

        screen_rect = self.screen.get_rect()
        self.text_rect = self.text_paused.get_rect()
        self.text_rect.center = screen_rect.center

        print self.text_rect

def read_card():
    "if open cv reads left arrow"
        return "left"
    "if open cv reads right arrow"
        return "right"
    "if open cv does not read anything"
        return "stay"
    pass

def generate_obstacles():
    "randomly generates obsticals for the runner to dodge"
    "as time passes it creates more obsticals"

    if
    pass


def crash():
    "when runner hits an obstical with 0 lives the game ends and the end screen shows"
    pass

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

    def init_templates(self, temp, orbs):
        # save the template image
        self.img = cv2.imread(temp, 0)

        # Initiate ORB detector
        orb = cv.ORB_create()

        # find the keypoints with ORB
        keypoints = orb.detect(img, None)

        # compute the descriptors with ORB
        keypoints, descriptor = orb.compute(img, keypoints)

        # draw only keypoints location,not size and orientation
        orbtemplate = cv.drawKeypoints(img, keypoints, None, color=(0,255,0), flags=0)

        return orbtemplate

    def get_feed(self):
        '''
        This function returns the vidnumORBseo feed after converting it to a grayscale for further interpreting
        '''

        # while the camera may be on, the camera could be reading a file or feed type
        # that it cannot handle this double checks that the input type is correct.
        self.everythingGood, self.frame = cap.read()
        if self.everythingGood == True:

            # Converting the Video frame into a grayscale image
            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return grayscale

    def image_converter(self, image, EdgeThres = (100, 255), pMatches = 300, OrbThres = 90):

            # using the CannyEdge Detector to simply image and store it
            self.edge = cv2.Canny(image, EdgeThres[0], EdgeThres[1])

            # using ORBs detection to
            self.orbprocessed =

            # Since this uses a lot of external input a testing function is made to clarify
            # what it is that the edge dectectors are finding
            if test:
                # Unfiltered Video Feed
                cv2.imshow('Real', frame)
                # Filtered Video Feed
                cv2.imshow('Edge', edge)
                # ORB filtered Video Feed
                cv2.imshow('ORBs', orbprocessed)
                # Escape the Video feed, and properly(?) close the windows/camera
                if cv2.waitKey(20) == ord('q'):
                break



    def get_feed(self, EdgeThres = (100, 255), pMatches = 300, OrbThres = 90, t = True):
        '''
        By inputing the desired threshold for the Canny Edge detector,
        as well as the number of ORBs for the templates, and the
        threshold for the number of matches needed for a positive fit.

        This function will return the data of the video feed converted into the
        '''

        everythingGood, frame = cap.read()
        # while the camera may be on, the camera could be reading a file or feed type
        # that it cannot handle this double checks that the input type is correct.
        if everythingGood == True:

            # Converting the Video frame into a grayscale image
            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # using the Cannyedge Detector package in the OpenCV Library to simply image
            edge = cv2.Canny(grayscale, 50, 220)

            # Since this uses a lot of external input a testing function is made to clarify
            # what it is that the edge dectectors are finding
            if t:
                # Unfiltered Video Feed
                cv2.imshow('Real', frame)
                # Filtered Video Feed
                cv2.imshow('Edge', edge)
                # Escape the Video feed, and properly(?) close the windows/camera
                if cv2.waitKey(20) == ord('q'):
                break
def __main__():
    cam = Camera()
