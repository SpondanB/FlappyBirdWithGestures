import mediapipe as mp
import cv2
import random
import sys
import pygame

fps = 24
screen_width = 289
screen_height = 511
screen = pygame.display.set_mode((screen_width,screen_height))
icon = pygame.image.load('gallery/favicon.ico').convert_alpha()
pygame.display.set_icon(icon)
ground_y = screen_height*0.8
game_images = {}
game_sounds = {}
player = 'gallery/images/bird.png'
background = 'gallery/images/background.png'
pipe = 'gallery/images/pipe.png'
title = 'gallery/images/title.png'
leave = False

hands = mp.solutions.hands
hands_mesh = hands.Hands(static_image_mode=True, max_num_hands=1 , min_detection_confidence=0.7)
draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
ret, temp_frm = cap.read()

def welcomeScreen():
    player_x = int(screen_width/8)
    player_y = int((screen_height - game_images['player'].get_height())/2)
    message_x = int((screen_width - game_images['message'].get_width())/2)
    message_y = int(screen_height*0.2)
    title_x = int((screen_width - game_images['message'].get_width())/2)
    title_y = int(screen_height*0.2)
    base_x = 0
    
    ret, temp_frm = cap.read()
    
    while ret:
        click = False
        leave = False
        ret, frm = cap.read()
        rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
        op = hands_mesh.process(rgb)
        if op.multi_hand_landmarks:
            landmarks = []
            for handlms in op.multi_hand_landmarks:
                for lm in handlms.landmark:
                    # print(lm)
                    lmx = int(lm.x * 640)
                    lmy = int(lm.y * 480)
                    landmarks.append([lmx, lmy])
                    if len(landmarks) >=9:
                        break
                draw.draw_landmarks(frm, handlms, hands.HAND_CONNECTIONS)
            fore_finger = (landmarks[8][0], landmarks[8][1])
            center = fore_finger
            thumb = (landmarks[4][0], landmarks[4][1])
            
            if thumb[1]-center[1]<20:
                print("click")
                click = True
                return
                
            elif center[1] < 65:
                leave = True
                pygame.quit()
                cv2.destroyAllWindows()
                cap.release()
                sys.exit()
        cv2.imshow("CameraWindow", frm)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or leave:
                pygame.quit()
                cv2.destroyAllWindows()
                cap.release()
                sys.exit()
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP) or click:
                return
            else:
                screen.blit(game_images['background'],(0,0))    
                screen.blit(game_images['message'],(message_x,message_y))
                screen.blit(game_images['player'],(player_x,player_y))
                screen.blit(game_images['base'],(base_x,ground_y))
                screen.blit(game_images['title'],(title_x,title_y))
                pygame.display.update()
                fps_clock.tick(fps)

def mainGame():
    score = 0
    player_x = int(screen_width/8)
    player_y = int(screen_height/2)
    base_x = 0
 
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()
 
    upperPipes = [
        {'x': screen_width+200, 'y': newPipe1[0]['y']},
        {'x': screen_width+200+(screen_width/2), 'y': newPipe2[0]['y']}
    ]
 
    lowerPipes = [
        {'x': screen_width+200, 'y': newPipe1[1]['y']},
        {'x': screen_width+200+(screen_width/2), 'y': newPipe2[1]['y']}
    ]
 
    pipeVelX = -4
 
    playerVelY = -9
    playerMaxVelY = 10
    # playerMinVelY = -8
    playerAccY = 1
 
    playerFlapVel = -8
    playerFlapped = False
 
    ret, temp_frm = cap.read()
 
    while ret:
        click = False
        leave = False
        ret, frm = cap.read()
        rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
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
            
            if thumb[1]-center[1]<20:
                click = True
                if player_y > 0:
                    playerVelY = playerFlapVel 
                    playerFlapped = True
                    # game_sounds['wing'].play()
                
            elif center[1] < 65:
                leave = True
                pygame.quit()
                cv2.destroyAllWindows()
                cap.release()
                sys.exit()
        
        cv2.imshow("CameraWindow", frm)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or leave:
                pygame.quit()
                cv2.destroyAllWindows()
                cap.release()
                sys.exit()
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP) or click:
                if player_y > 0:
                    playerVelY = playerFlapVel 
                    playerFlapped = True
                    # game_sounds['wing'].play()
 
        crashTest = isCollide(player_x, player_y, upperPipes, lowerPipes)
        if crashTest:
            # high_score = max(score, high_score)
            # print(f"[COLLIDED]\nHIGH SCORE: {high_score}\tSCORE:{score}")
            return
 
        playerMidPos = player_x + game_images['player'].get_width()/2  
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + game_images['pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos + 4:
                score +=1
                print(f"Your Score is {score}")
                game_sounds['point'].play()
 
        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY
 
        if playerFlapped:
            playerFlapped = False
        playerHeight = game_images['player'].get_height()
        player_y = player_y + min(playerVelY, ground_y - player_y - playerHeight)   
 
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x']  += pipeVelX
 
        if 0<upperPipes[0]['x']<5:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])   
 
        if upperPipes[0]['x'] < -game_images['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)   
 
        screen.blit(game_images['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            screen.blit(game_images['pipe'][0], (upperPipe['x'], upperPipe['y']))
            screen.blit(game_images['pipe'][1], (lowerPipe['x'], lowerPipe['y']))
        screen.blit(game_images['base'], (base_x, ground_y))    
        screen.blit(game_images['player'], (player_x, player_y))
 
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += game_images['numbers'][digit].get_width()
        Xoffset = (screen_width - width)/2 
 
        for digit in myDigits:
            screen.blit(game_images['numbers'][digit], (Xoffset, screen_height*0.12))
            Xoffset += game_images['numbers'][digit].get_width()
        pygame.display.update()
        fps_clock.tick(fps)

def isCollide(player_x, player_y, upperPipes, lowerPipes):
    if player_y>ground_y-25 or player_y<0:
        game_sounds['hit'].play()
        return True
 
    for pipe in upperPipes:
        pipeHeight = game_images['pipe'][0].get_height()
        if (player_y < pipeHeight + pipe['y']) and (abs(player_x - pipe['x']) < game_images['pipe'][0].get_width() - 15):
            game_sounds['hit'].play()
            return True
 
    for pipe in lowerPipes:
        if (player_y + game_images['player'].get_height() > pipe['y']) and (abs(player_x - pipe['x']) < game_images['pipe'][0].get_width() - 15):
            game_sounds['hit'].play()
            return True
 
    return False
 
 
def getRandomPipe():
    pipeHeight = game_images['pipe'][0].get_height()    
    offset = screen_height/3
    y2 = offset + random.randrange(0, int(screen_height - game_images['base'].get_height() - 1.2*offset))
    pipeX = screen_width + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},
        {'x': pipeX, 'y': y2}
    ]
    return pipe


if __name__ == "__main__":
    pygame.init() 
    fps_clock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')
    
    ret, frm = cap.read()
    cv2.imshow("CameraWindow", frm)
    
    game_images['numbers'] = (
        pygame.image.load('gallery/images/0.png').convert_alpha(),
        pygame.image.load('gallery/images/1.png').convert_alpha(),
        pygame.image.load('gallery/images/2.png').convert_alpha(),
        pygame.image.load('gallery/images/3.png').convert_alpha(),
        pygame.image.load('gallery/images/4.png').convert_alpha(),
        pygame.image.load('gallery/images/5.png').convert_alpha(),
        pygame.image.load('gallery/images/6.png').convert_alpha(),
        pygame.image.load('gallery/images/7.png').convert_alpha(),
        pygame.image.load('gallery/images/8.png').convert_alpha(),
        pygame.image.load('gallery/images/9.png').convert_alpha()
        )
    game_images['message'] = pygame.image.load('gallery/images/message.png').convert_alpha()
    game_images['base'] = pygame.image.load('gallery/images/base.png').convert_alpha()
    game_images['pipe'] = (
        pygame.transform.rotate(pygame.image.load(pipe).convert_alpha(), 180),
        pygame.image.load(pipe).convert_alpha()
        )
    game_images['background'] = pygame.image.load(background).convert_alpha()
    game_images['player'] = pygame.image.load(player).convert_alpha()
    game_images['title'] = pygame.image.load(title).convert_alpha()
 
    #Game Sounds
    game_sounds['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    game_sounds['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    game_sounds['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    game_sounds['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    game_sounds['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')
 
    # ret, frm = cap.read()
    # cv2.imshow("WindowDisplay", frm)
    
    while ret:
        ret, frm = cap.read()
        cv2.imshow("CameraWindow", frm)
        welcomeScreen()
        mainGame()

