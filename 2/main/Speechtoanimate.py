import serial
import speech_recognition as sr
import cv2
import numpy as np

r = sr.Recognizer()
mic = sr.Microphone()
specificWords = ["bank", "bridge", "bus", "doctor", "dog", "food",
"hello", "hospital", "how", "left", "mountain", "much", "no", "north",
"play", "right", "run", "school", "shop", "south", "telephone",
"thank you", "time", "train", "turn", "water"]

print("Start talking!")

def playVideo(filename):
    global cap
    cap = cv2.VideoCapture(filename)
    
    if (cap.isOpened()== False):
        print("Error opening video file")
    
    while(cap.isOpened()):
        
    # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
        # Display the resulting frame
            cv2.imshow('Spoken', frame)
            
        # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    
    # Break the loop
        else:
            break
    
    # When everything done, release
    # the video capture object
    


while True:
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)
    if words in specificWords:
        filename = words+".mp4"
        playVideo(filename)
        

    else:
        letters = list(words)
        for letter in letters:
            filename = letter+".mp4"
            playVideo(filename)
    cap.release()
    cv2.destroyAllWindows()
