"""
Micro Project 4
by declanketchum, jackiezeng01, & lxbtlr
"""

import pygame
import cv2

# hypothetical x positions of lanes.
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
        '''
        if direction == "left" and self.x != LEFT_LANE:
            self.x += -50
        if direction == "right" and self.x != RIGHT_LANE:
            self.x += 50
        if direction == "straight":
            pass
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
        global LEFT_LANE = 50
        global MIDDLE_LANE = 100
        global RIGHT_LANE = 150
        global TOP_Y = 0
        global BOTTOM_Y = 0
        Runner = Runner(background)
        # (pygame being down prevented any other progress here)
    def run(self):
        '''
        Runs the game and updates frames
        '''
        RUNNING = True
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

class Camera(): 
    '''
    Class containing all gathering of data from the Camera feed.
    designed to have minimal interpreting in this class and instead interface
    with another class to find the meaning in the image data.
    '''
    def __init__(self, left, right):
        ''' 
        given the base 'right' and 'left' images, the function initializes all necessary pieces of opencv
        as well as converts the images into SIFT templates
        '''
        # initalize the feed
        self.cap = cv2.VideoCapture(0)

        # check that camera is available
        if not (self.cap.isOpened()):
            print('No camera detected,\n please run with a Camera')
        self.rightImage = cv2.imread(right, 0)
        self.leftImage = cv2.imread(left, 0)

        # initiating SIFT detector: SIFT being the feature detector
        self.sift = cv2.SIFT()

        # we will be using the FLANN index KDtree algorithm, which is marked by 0
        self.FLANN_INDEX_KDTREE = 0
        self.index_params = dict(algorithm = self.FLANN_INDEX_KDTREE, trees = 5)
        self.search_params = dict(checks = 50)

        # needed intialization of FLANN
        self.flann = cv2.FlannBasedMatcher(self.index_params, self.search_params)
        
        # create the SIFT data from images to check the feed with
        # kp = Keypoints of the image, Des = the descriptors of the keypoints
        self.leftkp, self.leftDes = sift.detectAndCompute(self.leftImage,None)
        self.rightkp, self.rightDes = sift.detectAndCompute(self.rightImage,None)

    def detect_sign(self, videoFrame = self.get_feed()):
        '''
        using FLANN knn we're able to generate the unique features with SIFT for both of the templates and the incoming video feed
        Next, we run KNN and on the features of the templates and the incoming video feed inorder to see:
        1. whether one of the templates crosses one of the minimum thresholds, 
        2. if more than one does, then check to see if one of them has a significantly greater number of matches
        based entirely off of OpenCV's FLANN (only change is logic of comparing the sign templates)
        https://bit.ly/2UtZMEL 
        '''
        
        self.framekp, self.frameDes = sift.detectAndCompute(self.videoFrame,None)
        # using nearest neighbor, we will find the matches between the left and right templates
        self.leftMatches = flann.knnMatch(self.frameDes,self.leftDes,k=2)
        self.rightMatches = flann.knnMatch(self.frameDes,self.rightDes,k=2)

        # good stores all the *good* matches
        self.goodLeft = []
        self.goodRight = []

        # use lowe's ratio test to evaluate matches
        for m,n in self.leftMatches:
            if m.distance < 0.7*n.distance:
                self.goodLeft.append(m)
        for m,n in self.rightMatches:
            if m.distance < 0.7*n.distance:
                self.goodRight.append(m)

        # threshold of matches necessary: out of 50 possible features we expect at least 20 to be present
        self.minMatchCount = 20
        if (len(self.goodRight) > self.minMatchCount) and (len(self.goodLeft) <= self.minMatchCount):
            return "left"
        if (len(self.goodLeft) > self.minMatchCount and (len(self.gootRight) <= self.minMatchCount):
            return "right"
        else:
            return "straight"

    def get_feed(self):
        '''
        This function returns the video feed after converting it to grayscale for further interpreting
        '''

        # while the camera may be on, the camera could be reading a file or feed type
        # that it cannot handle this double checks that the input type is correct.
        self.everythingGood, self.frame = cap.read()
        if self.everythingGood == True:

            # Converting the Video frame into a grayscale image
            self.grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return self.grayscale

def __main__():
    game = Game().run()