import cv2

# Initialize the tracker
tracker = cv2.TrackerCSRT_create()  # You can change to other trackers like KCF, MIL, etc.

# Capture video from webcam
cap = cv2.VideoCapture(0)

# Read the first frame
ret, frame = cap.read()
if not ret:
    print("Failed to read from webcam")
    cap.release()
    cv2.destroyAllWindows()
    exit()

# Select the bounding box
bbox = cv2.selectROI("Select Object", frame, False)
cv2.destroyWindow("Select Object")

# Initialize the tracker with the selected region
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Update tracker
    success, bbox = tracker.update(frame)
    
    if success:
        x, y, w, h = map(int, bbox)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
    else:
        cv2.putText(frame, "Tracking lost", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    
    # Display the frame
    cv2.imshow("Object Tracking", frame)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
