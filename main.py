import os
import cv2
import requests
import threading
import time
import json
from gtts import gTTS
from playsound import playsound
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_endpoint = os.getenv("API_ENDPOINT")
api_key = os.getenv("API_KEY")

headers = {
    'Prediction-Key': api_key,
    'Content-Type': 'application/octet-stream',
}

alpha = 0.70

language = 'ar'
totalMoney = 0
last = 0
image_filename = "image.jpg"


def talk(mytext):
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    playsound('welcome.mp3')

    if os.path.exists("welcome.mp3"):
        os.remove("welcome.mp3")


def execute_prediction(frame, i):
    global totalMoney, last

    talk("الصورة التقطت")

    cv2.imwrite(image_filename, frame)
    print(f"Frame captured and saved as {image_filename}")

    with open(image_filename, 'rb') as image_file:
        image_data = image_file.read()

    try:
        response = requests.post(
            api_endpoint,
            headers=headers,
            data=image_data
        )

        api_data = json.loads(response.text)

        if 'predictions' in api_data:
            predictions = api_data['predictions']

            if predictions:
                first_prediction = predictions[0]

                probability = first_prediction.get('probability', 0.0)
                tagname = first_prediction.get('tagName', '')

                if probability < alpha:
                    talk("برجاء اعادة المحاولة")

                else:
                    print(f"Probability: {probability}")
                    print(f"TagName: {tagname}")

                    last = int(tagname.split("_")[0])

                    talk(f"{last} جنيه")

                    totalMoney += last

    except Exception as e:
        print("Error:", e)
        talk("حدث خطأ أثناء المعالجة")


def capture_frames():
    global totalMoney, last

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'k' to capture a frame from the webcam.")

    i = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not capture frame.")
            break

        cv2.imshow('Press "k" to capture', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('k'):
            threading.Thread(
                target=execute_prediction,
                args=(frame, i)
            ).start()

            i += 1

        elif key == ord('q'):
            break

        elif key == ord('t') and totalMoney != 0:
            talk(f"المبلغ الكلي {totalMoney} جنيه")
            totalMoney = 0

        elif key == ord('n'):
            talk("تم مسحها")
            totalMoney -= last

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    webcam_thread = threading.Thread(target=capture_frames)

    webcam_thread.start()

    time.sleep(2)

    print("Press Ctrl+C to stop the application.")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        webcam_thread.join()
        print("Application stopped.")

