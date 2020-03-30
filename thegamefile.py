"""
Micro Project 4
"""

import pygame
import cv2

# this is the main file for the project with all of the classes and functions that will be called

class Obstacles():
#creates a class that for the obstacles
    def __init__(self, x_position, y_position):
        #initilizes each obstical with an x & y position
        pass


class Runner():
#creates a class for the character in the game
    def __init__(self, x_position=middle):
    #initilizes the character with a starting x position (no y position because the background moves not the character)
        pass


class Timer():
#creates a timer that serves
    def __init__(self, minute=0, second=0, millisecond=0):

        pass


class Best_Time():
#class to save the high score/best time
    pass


def init_game():
    pass


def read_card():
    # if open cv reads left arrow
        return "left"
    # if open cv reads right arrow
        return "right"
    # if open cv does not read anything
        return "stay"    


def move_left():
    # if read_card returns left shift the runner to the lane dirrectly to the left of thier current position
    # if the runner is in the furthest left lane do not allow the runner to move further
    pass


def move_right():
    # if read_card returns right shift the runner to the lane dirrectly to the right
    # if the runner is in the furthest right lane do not allow the runner to move further
    pass


def generate_obstacles():
    # randomly generates obsticals for the runner to dodge
    # as time passes it creates more obsticals
    pass


def crash():
    # when runner hits an obstical with 0 lives the game ends and the end screen shows
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
