# 🧙‍♂️ Harry Potter Invisibility Cloak using OpenCV

This mini-project recreates the **Harry Potter–style Invisible Cloak** effect using **OpenCV** and **NumPy** in Python.  
By detecting a specific color (blue here) from the webcam and replacing that color with the background, it creates an *illusion of invisibility* in real time.  

---

## 🎬 Demo

📹 **Project Video:**  
[![Watch the demo video](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://youtu.be/YOUR_VIDEO_ID)  
*(Attach your video link or replace the above with a local video file — `demo.mp4`)*  

---

## 🧠 How It Works

1. The camera first captures the **background** (without the person).  
2. When the person enters the frame wearing a **specific color cloak** (default: blue), the program detects that color using the **HSV color space**.  
3. That colored region is replaced with the **previously captured background**, making the cloak area appear *invisible*.  
4. The result is shown live using **OpenCV’s video window**.

---

## ⚙️ Requirements


- Python 
- OpenCV
- Numpy
- A working webcam



