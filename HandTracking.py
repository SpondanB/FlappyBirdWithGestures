import mediapipe as mp
import cv2

# to get the video from the webcam
cap = cv2.VideoCapture(0)

# initiallizing all the mediapipe solutions needed
hands = mp.solutions.hands
hands_mesh = hands.Hands(static_image_mode=True, min_detection_confidence=0.7)
draw = mp.solutions.drawing_utils

# reads the frame and the return the value that the camera is working or not
ret, frm = cap.read()

while ret:
    ret, frm = cap.read()
    # helps convert bgr to rgb color format
    rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
    
    # using hand_mesh to get all the hand landmarks
    op = hands_mesh.process(rgb)
    # multi hand landmarks is a list containing all the landmarks
    if op.multi_hand_landmarks:
        for i in op.multi_hand_landmarks:
            # this is to draw the lines and landmarks on the screen
            draw.draw_landmarks(frm, i, hands.HAND_CONNECTIONS)
    
    # this shows the camera feed window
    cv2.imshow("WindowDisplay", frm)
    # an escape sequence
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
    
