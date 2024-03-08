import mediapipe as mp
import cv2

leave = False
i = 0

hands = mp.solutions.hands
hands_mesh = hands.Hands(static_image_mode=True, max_num_hands=1 , min_detection_confidence=0.7)
draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
ret, temp_frm = cap.read()

while ret:
    click = False
    ret, frm = cap.read()
    rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
    # frm = cv2.rectangle(frm, (225, 250), (475, 300), (255, 0, 0), 2)
    # cv2.putText(frm, "JUMP", (333, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
    
    
    op = hands_mesh.process(rgb)
    if op.multi_hand_landmarks:
        landmarks = []
        for handlms in op.multi_hand_landmarks:
            for lm in handlms.landmark:
                # print(lm)
                lmx = int(lm.x * 640)
                lmy = int(lm.y * 480)
                landmarks.append([lmx, lmy])
            draw.draw_landmarks(frm, handlms, hands.HAND_CONNECTIONS)
        fore_finger = (landmarks[8][0], landmarks[8][1])
        center = fore_finger
        thumb = (landmarks[4][0], landmarks[4][1])
        
        if thumb[1]-center[1]<15:
            click = True
            
        elif center[1] < 65:
            leave = True
            
    if click:
        i+=1
        print("Click...",i)
    
    
    cv2.imshow("WindowDisplay", frm)
    if cv2.waitKey(1) == 27 or leave:
        cv2.destroyAllWindows()
        cap.release()
        break