# Fall Detection System

> Deep learning-based fall detection system using computer vision and real-time classification.

## About the Project

This project aims to detect falls in real-time using a deep learning model trained on image data.  
Using computer vision and TensorFlow, the system can recognize whether a person has fallen or not based on webcam input.

## File Information

- **README.txt**: General information about the project.
- **falltracker.h5**: The trained deep learning model used for real-time fall detection.
- **FallDetection.ipynb** and **FallDetection.py**: Python scripts to run the fall detection system, with or without Jupyter Notebook.
- **.ipynb_checkpoints/**: Jupyter Notebook checkpoints needed for running `FallDetection.ipynb`.
- **ModelCreation.ipynb**: Notebook showing how the model was trained, including data augmentation and training steps.
- **Data/**: Folder containing original images and labels used for training.
- **aug_data/**: Augmented data used to improve model performance during training.
- **Bonus/**: Contains two CSV files from additional studies:
  - `CSV_ACCELERATION.csv`: Study based on acceleration data for fall detection (incomplete).
  - `CSV_ELDERLY.csv`: Study based on elderly movement data, which was not used due to overly perfect data limiting realistic analysis.

## How to See the Result

1. Install the required libraries:

```bash
pip install opencv-python
pip install tensorflow
pip install numpy```
