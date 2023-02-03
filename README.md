# Traffic Sign Detection and Recognition

Detecting and recognizing traffic signs in images and video streams. It uses computer vision and machine learning techniques to identify and classify various traffic signs, such as stop signs, yield signs, and speed limit signs.


https://user-images.githubusercontent.com/29041010/216681247-8f8a9ca0-2666-4ab4-bedb-c448c2245e51.mp4

NOTE: The left slider that show numbers is part of the original video our model draw the detection bounres and recognize the sign




## Requirements
- Python 3.7 or later
- OpenCV
- TensorFlow 2.x
- Numpy

## Usage
we used GTSRB & GTSDB datasets for this project

* The classification part :
use Classifier.ipynb in the colab folder to train and generate the weights file
* The detection part :
  * For the detector we used YOLOV3 you can change the configuration of the model through the YOLO Model Configuration folder 
  * For preparing the dataset use the data preparation folder
  * use detector.ipynb in the colab folder to train and generate the weights file
* Merging
  * use Connection between Classifier and Detector.ipynb to connect the classifier with the detector and to test on images/videos
* The Application
  * For testing only images from the GTSRB dataset as my machine couldn't handle the detection part or the connection between the two models we depend on colab
* NOTES: 
  * The notebooks are well commented and organized so no need to explain more details


## Models
The repository includes YOLO for detecting traffic signs and a pure trained model for the recognizing. 

## conclusion 
  - the recognition model achieved 99.3% using Inception architecture With Data Augmentation and trained it for 200 epoch
  - <p>the detection model achieved 91%</p>
    <img src="https://user-images.githubusercontent.com/29041010/216661055-047af709-9fbb-4914-b8ab-b37444c1279c.png"  width="400" height="400" />
  - when we run the test video on colab it processing speed was 0.5 Frame/s we used a feature in openCV and the result was 1 Frame/s
    we didn't know where is the issue but if you want to contribute it will be a great help
## Note
Since This Project is based on machine learning techniques this readMe file is written with the help of ChatGPT :)
