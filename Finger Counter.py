import cv2 # OpenCV
from cvzone.HandTrackingModule import HandDetector # Allows us to use hand detection and finger counting functions by importing the HandDetector class from the cvzone library.

# Initialize HandDetector
detector = HandDetector(maxHands=1, detectionCon=0.8) # Creates an instance of the HandDetector class, Sets the maximum number of hands to detect at the same time to 1, Sets the detection confidence to 80%, meaning the detector will only recognize a hand if it is at least 80% sure.
video_capture = cv2.VideoCapture(0)  # Use primary camera

# Check if the camera is opened
if not video_capture.isOpened():
    print("Failed to open camera!")
    exit()

while True: # Creates an infinite loop that will run until explicitly broken. It is used to continuously capture frames from the video feed.
    success, frame = video_capture.read() #  Reads a frame from the video capture object (video_capture). The read() method returns two values: - success: A boolean value indicating whether the frame was successfully captured (True) or not (False). - frame: The captured frame, which is an image array.
    if not success:
        print("Failed to capture image!")
        break

    hands, frame = detector.findHands(frame, draw=True)  # Hand detection and drawing. hands, frame: This line returns two values: - hands: A list of dictionaries, where each dictionary contains information about a detected hand, including its landmarks. - frame: The modified frame with hand landmarks drawn on it, if draw=True. detector.findHands(frame, draw=True): - frame: The current video frame in which hand detection is to be performed. - draw=True: A parameter that specifies whether to draw hand landmarks on the frame. If True, the detected hand landmarks are drawn on the frame.

    if hands: #  checks if any hands were detected in the frame. The hands variable is a list that contains information about all the detected hands. If no hands are detected, this list will be empty, and the condition will evaluate to False. If at least one hand is detected, the condition will evaluate to True.
        # Get the first hand's data
        hand = hands[0] # hands is a list where each element contains information about a detected hand. hands[0] accesses the first element in this list, which represents the first detected hand.

        # Get the list of landmarks of the hand
        landmark_list = hand['lmList'] # hand['lmList'] accesses the lmList key in the dictionary hand, which contains the coordinates of these landmarks.

        if landmark_list: # Checks if the landmark list is not empty. This ensures that the landmarks have been detected for the hand.
            # Get the number of fingers up
            fingers_up = detector.fingersUp(hand) #  This method returns a list indicating which fingers are up. For example, [0, 1, 0, 0, 0] means that only the index finger is up. - fingers_up: A list where each element is 1 if the corresponding finger is up and 0 if it is down.
            print("Finger Up List:", fingers_up)  # Print finger status

            # Display text based on the number of fingers up
            if fingers_up == [0, 1, 0, 0, 0]:
                cv2.putText(frame, "1 Finger Up", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2) # Draws the text "1 Finger Up" on the frame at coordinates (50, 50). cv2.FONT_HERSHEY_SIMPLEX: The font type used for the text. 1: The font scale. (255, 0, 0): The color of the text in BGR format (blue, green, red). 2: The thickness of the text.
            elif fingers_up == [0, 1, 1, 0, 0]:
                cv2.putText(frame, "2 Fingers Up", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            elif fingers_up == [0, 1, 1, 1, 0]:
                cv2.putText(frame, "3 Fingers Up", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            elif fingers_up == [0, 1, 1, 1, 1]:
                cv2.putText(frame, "4 Fingers Up", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            elif fingers_up == [1, 1, 1, 1, 1]:
                cv2.putText(frame, "5 Fingers Up", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # Display the number of fingers shown on the video
            finger_count = sum(fingers_up) # Sums up the elements of the fingers_up list to get the total number of fingers that are up.
            cv2.putText(frame, f'Fingers: {finger_count}', (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Video", frame) # This function displays the current frame in a window titled "Video". frame is the current image/frame from the video capture that is being processed and displayed. It continuously updates the window with new frames captured from the video feed.

    if cv2.waitKey(1) & 0xFF == ord('q'): # ord('q') converts the character 'q' to its ASCII value. If the key pressed is 'q', the condition evaluates to True and the loop is broken, which stops the video capture and closes the window.
        break

video_capture.release() # This function releases the video capture object, freeing up the camera resource.
cv2.destroyAllWindows() # Closes all OpenCV windows.