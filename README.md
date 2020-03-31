# SoftDes_MP4

# Game Play:
This game shows an arial shot of a runner that can be in one of three lanes from left to right. The runner does not move up or down the screen; the background is always moving towards the bottom of the screen making it look like the character is running towards the top. Obsticals randomly appear in the background and move towards the runner. The runner has to move to a different lane to avoid the obstical. The player uses thier computer camera to control the runner's movement. To move the runner left the user would hold a left pointing arrow to the camera. The player has three lives to start will. Each time the runner hits an obstical, one life is lost. When there are zero lives the game is over. The point of the game is to run for as long as possible.


# Libraries and Packages
This game uses opencv to access the computer camera and collect data from the images to detect which way the arrows are pointing.
The game also uses pygame to render the display and to keep a timer. 

# Classes 

Runner  
This class creates the runner object which moves to avoid obsticals that appear.
The 'init' funcion initilizes the runner at the bottom middle of the screen with 3 lives.
The 'draw' function puts the runner on the screen in front of the background image.
The 'move' function causes the runner to move between lanes when the camera is shown an arrow. 
The 'minus_life' function subtracts one life from the runner's life count when they hit an obsitcal

Obstacle 
This class creates obstical objects that can be randomly generated and put in the runners path. 
The 'init' function initilizes the obstical in the background, at the top of the page, in one of the three lanes.
The 'draw' function draws the obstical on the screen. 
The 'move' function moves the obstical towards the runner.

Game 
The 'init' function initializes the game by: starting the clock, setting the background, size of screen and frames per second, and by creating the runner and object classes.
The 'run' function runs the game by updating the frame with any new obsticals and changes in the runners location, and by moving the background and obsticals towards the runner. 




Github ecosystem steps:
# First setting up Contributing: 
1. Fork (on github website for repo)
2. Clone in terminal to file directory
3. git remote -v
4. git remote add upstream "use the git repo address we had before"
# Updating local repo to master:
1. git pull upstream master
# Committing Upstream:
1. git add .
2. git commit -m ""
3. git status    (make sure there are no gaps between your code and last push)
4. git push
5. then deal with pull requests https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork
