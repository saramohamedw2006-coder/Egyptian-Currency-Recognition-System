# Egyptian Currency Recognition System for the Blind

AI-powered wearable system for recognizing Egyptian banknotes and calculating total money for visually impaired individuals using Computer Vision and Text-to-Speech technologies.

## Project Overview

This project was developed as part of Alexandria STEM School research work (2023–2024).

The system uses:

* Raspberry Pi
* Webcam / Raspberry Pi Camera
* Microsoft Azure Custom Vision
* Python
* Text-to-Speech (Arabic Voice Output)

The wearable glove captures images of Egyptian banknotes, detects their denomination using AI, and announces the value using Arabic speech output.

## Features

* Detect Egyptian banknotes
* Arabic voice feedback
* Calculates total money
* Fast operational time
* High detection accuracy
* Designed for visually impaired users

## Technologies Used

* Python
* OpenCV
* Microsoft Azure Custom Vision
* gTTS (Google Text To Speech)
* Raspberry Pi
* Computer Vision

## Dataset

* 800 self-collected images
* Different lighting conditions
* Multiple banknote angles
* Augmented using:

  * Rotation
  * Flipping
  * Scaling
  * Noise backgrounds

## Detection Accuracy

Average confidence level ranges from:

* 88.6% to 96.3%

Average operational time:

* 1.05 seconds

## Project Structure

```text
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file and add:

```env
API_KEY=YOUR_API_KEY
API_ENDPOINT=YOUR_API_ENDPOINT
```

## Controls

| Key | Function                   |
| --- | -------------------------- |
| K   | Capture image              |
| T   | Speak total money          |
| N   | Remove last detected value |
| Q   | Quit program               |

## Future Improvements

* Use Raspberry Pi Camera V2
* Improve detection under low lighting
* Add 1 EGP support
* Expand dataset size

## License

This project is for educational and research purposes.
