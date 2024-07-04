# Fruits Detection using YOLO

## Overview
This project utilizes the YOLO (You Only Look Once) object detection algorithm to detect different types of fruits in images. It includes a web interface where users can upload images and get predictions on the types of fruits present in the images.

## Directory Structure
/content
│
├── app.py                   # Main application script
├── runs                     # Directory for prediction and training outputs
│   ├── detect               # Directory for detection-related outputs
│   │   └── predict          # Directory for predicted images
│   ├── train                # Directory for training-related outputs
│   │   ├── weights          # Directory for trained model weights
│   │   │   └── best.pt      # Best trained model weights
├── static                   # Static files for the web application
│   ├── styles.css           # CSS styles for the web interface
│   ├── uploads              # Folder for uploaded images
│   └── predictions          # Folder for predicted images
├── templates                # HTML templates for the web application
│   └── index.html           # Main HTML template
├── Inference                # Directory holding sample inference images
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   ├── 5.png
│   ├── 6.png
│   ├── 7.png
│   ├── 8.png
│   ├── 9.png
│   ├── 10.png
│   ├── 11.png
│   ├── 12.png
│   ├── 13.png
│   └── 14.png
├── requirements.txt         # List of dependencies for the project
├── Fruits_Detection.ipynb   # Jupyter Notebook for the project
└── README.md                # README file for the project

/content
│
├── app.py # Main application script
├── runs # Contains prediction outputs and training logs
│ ├── detect # Directory for detection-related outputs (e.g., predicted images)
│ │ ├── predict # Predicted images
│ │ │ ├── 1.png
│ │ │ ├── 2.png
│ │ │ ├── ... # Predicted images
│ ├── train # Directory for training-related files (e.g., weights, logs)
│ │ ├── weights # Trained YOLO model weights
│ │ │ └── best.pt # Best trained model weights
│ │ ├── logs # Training logs
│ │ │ └── ... # Training log files
├── static # Static files for the web application
│ ├── styles.css # CSS styles for the web interface
│ ├── uploads # Folder for uploaded images
│ └── predictions # Folder for predicted images
├── templates # HTML templates for the web application
│ └── index.html # Main HTML template
├── Inference # Directory holding sample inference images
│ ├── 1.png
│ ├── 2.png
│ ├── 3.png
│ ├── 4.png
│ ├── 5.png
│ ├── 6.png
│ ├── 7.png
│ ├── 8.png
│ ├── 9.png
│ ├── 10.png
│ ├── 11.png
│ ├── 12.png
│ ├── 13.png
│ ├── 14.png
├── requirements.txt # List of dependencies for the project
├── Fruits_Detection.ipynb # Jupyter Notebook for the project
└── README.md # This README file




## Fruits-360 Dataset

The project uses the Fruits-360 dataset, a collection of images encompassing 131 different fruit classes. It includes a total of 90,483 images, split into 67,692 training images and 22,688 test images. Each class has a substantial number of images, ensuring robust training and testing of machine learning models.

- **Total Images:** 90,483
- **Training Images:** 67,692
- **Test Images:** 22,688
- **Image Size:** 100x100 pixels (original size varies)
- **Classes:** 131 fruit types

The dataset is structured in directories for training and testing, with each fruit type having its own folder.

## Technologies Used

- **Python:** Programming language used for development.
- **Flask:** Web framework used for creating the web interface.
- **YOLOv5:** Object detection model used for detecting fruits in images.
- **OpenCV:** Library used for image processing tasks.
- **Pillow (PIL):** Python Imaging Library used for opening and manipulating images.
- **Torch:** Deep learning library used for loading the YOLO model and making predictions.
- **pyngrok:** Library used for creating secure tunnels to localhost.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Fruits_Detection.git
   cd Fruits_Detection


