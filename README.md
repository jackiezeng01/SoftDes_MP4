# SoftDes_MP4

# Game Play:
This game shows an aerial shot of a runner that can be in one of three lanes from left to right. The runner does not move up or down the screen; the background is always moving towards the bottom of the screen making it look like the character is running towards the top. obstacles randomly appear in the background and move towards the runner. The runner has to move to a different lane to avoid the obstacle. The player uses their computer camera to control the runner's movement. To move the runner left the user would hold a left pointing arrow to the camera. The player has three lives to start will. Each time the runner hits an obstacle, one life is lost. When there are zero lives the game is over. The point of the game is to run for as long as possible.


# Libraries and Packages
This game uses opencv to access the computer camera and collect data from the images to detect which way the arrows are pointing.
The game also uses pygame to render the display and to keep a timer. 

# Classes 

Runner  
This class creates the runner object which moves to avoid obstacles that appear.
The 'init' function initializes the runner at the bottom middle of the screen with 3 lives.
The 'draw' function puts the runner on the screen in front of the background image.
The 'move' function causes the runner to move between lanes when the camera is shown an arrow. 
The 'minus_life' function subtracts one life from the runner's life count when they hit an obstacle

Obstacle 
This class creates obstacle objects that can be randomly generated and put in the runners path. 
The 'init' function initializes the obstacle in the background, at the top of the page, in one of the three lanes.
The 'draw' function draws the obstacle on the screen. 
The 'move' function moves the obstacle towards the runner.

Game 
The 'init' function initializes the game by: starting the clock, setting the background, size of screen and frames per second, and by creating the runner and object classes.
The 'run' function runs the game by updating the frame with any new obstacles and changes in the runners location, and by moving the background and obstacles towards the runner. 


