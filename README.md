# FlappyBirdWithGestures
A project to make a game which is gesture controlled using opencv
<br>
<br>
The initial idea was to have a box in the center of camera window which the players hand will touch to jump i.e. play the game.
But soon it was clear that it would be a lot more tedious to work on. So we decided on ok gesture (bringing your index finger and thumb together). This made the process to check if the plyer clicks a bit more easier as we just have to calculate the distance between the markers of index and thumb.
<br>
<br>
We made 3 test programs to check if the idea is feasible or not. They are HandTracking.py , FlappyBird.py and TestGestureClicker.py. 
<br><br>
## Functioning Code
main.py - Flappy Bird with Gesture controls.
<br><br>
FlappyBird.py - Normal FlappyBird Game with keyboard controls.
<br>
HandTracking.py - To implement a hand tracking program which also draws the landmarks.
<br>
TestGestureClicker.py - To implement a gesture clicking program which prints click every time the clicking gesture is done.
