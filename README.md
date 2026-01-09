# 🐦 Flappy Bird with Hand Gesture Controls

An interactive reimagining of **Flappy Bird**, controlled entirely through **hand gestures** using a webcam. This project combines **computer vision**, **real-time gesture recognition**, and **game development** using **MediaPipe**, **OpenCV**, and **Pygame**.

The game replaces traditional keyboard input with a natural **pinch (index finger + thumb) gesture**, demonstrating how vision-based input can be integrated into real-time interactive systems.

---

## 📌 Project Overview
This project explores an alternative human–computer interaction (HCI) paradigm by enabling players to control Flappy Bird using hand gestures captured through a webcam.

Key ideas behind the project:
- Replace keyboard/mouse input with **vision-based gestures**
- Use **MediaPipe Hands** for accurate landmark detection
- Integrate gesture input seamlessly into a real-time Pygame loop

The result is a fully playable game that reacts to natural hand movements.

---

## ✋ Gesture-Based Controls

### Primary Gesture – “Click / Flap”
- **Gesture:** Bring the **index finger and thumb together** (pinch)
- **Action:** Bird flaps upward

This gesture was chosen after experimentation because it is:
- Easy to detect reliably
- Less sensitive to noise than spatial box-based methods
- Intuitive for repeated actions

### Exit Gesture
- Moving the index finger near the **top of the camera frame** exits the game

---

## 🧠 Technologies Used
- **Python**
- **Pygame** – rendering, audio, game loop
- **OpenCV** – webcam capture and frame processing
- **MediaPipe Hands** – real-time hand landmark detection

---

## 🎮 Game Features
- Real-time hand gesture control
- Live webcam feed with hand landmark overlay
- Classic Flappy Bird mechanics (pipes, gravity, scoring)
- Audio feedback (hit, point, flap sounds)
- Smooth integration of vision input with game physics

---

## 📁 Project Structure
```text
FlappyBirdWithGestures/
│
├── main.py                 # Flappy Bird with gesture-based controls
├── FlappyBird.py           # Classic Flappy Bird (keyboard-controlled)
├── HandTracking.py         # Standalone hand landmark detection demo
├── TestGestureClicker.py   # Gesture click detection prototype
│
├── gallery/
│   ├── images/             # Sprites and UI assets
│   ├── audio/              # Game sound effects
│   └── favicon.ico
```

---

## 🧪 Development & Experimentation
Before implementing the final game, multiple prototypes were created:

- **HandTracking.py**  
  Tested MediaPipe’s ability to track hand landmarks and visualize them reliably.

- **TestGestureClicker.py**  
  Experimented with detecting a pinch gesture by measuring distance between thumb and index finger landmarks.

- **FlappyBird.py**  
  Implemented a traditional keyboard-controlled version to isolate and test game logic.

These experiments informed the final design decisions used in `main.py`.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Webcam
- Required libraries:
  - pygame
  - opencv-python
  - mediapipe

Install dependencies:
```bash
pip install pygame opencv-python mediapipe
```

---

## ▶️ Running the Game
```bash
python main.py
```

A webcam window will open alongside the game window. Make sure your hand is clearly visible to the camera.

---

## 📈 Skills Demonstrated
- Computer vision with MediaPipe
- Gesture recognition and tracking
- Real-time input processing
- Game loop integration with external sensors
- Human–computer interaction (HCI) design

---

## 🧠 Learning Outcomes
- Translating raw vision data into game controls
- Handling real-time CV pipelines alongside rendering loops
- Designing robust gesture-based input systems
- Managing multi-library integration in Python

---

## 🏷️ Portfolio Note
This project highlights the intersection of:
- **Computer Vision**
- **Interactive Systems**
- **Game Development**

---

## 🔮 Future Improvements
- Gesture calibration for different hand sizes
- Difficulty scaling based on reaction time
- Support for multiple gestures (pause, restart)
- Improved robustness under varying lighting conditions

---

**Author:** Spondan Bandyopadhyay

---
