import cv2
from deepface import DeepFace
# Load video from webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # Analyze emotion
    results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

    # Display emotion on frame
    emotion = results[0]['dominant_emotion']
    cv2.putText(frame, f'Emotion: {emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Emotion Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
