# AI-Powered Image Prediction: Bike or Car

## Repository Outline

Explanation about the content of each file and folder:

1. model_building.ipynb - Notebook containing data processing with Python, starting from loading dataset, EDA process, data augmentation, model training, and model evaluation.
2. model_inf.ipynb - Data Inference notebook containing activities from loading the model to performing classification.
3. url.txt - File containing the Dataset URL, Deployment URL, and the best model link.
4. Deployment - Folder containing related files to perform deployment to HuggingFace.

## Problem Background

The Deep Learning model (Computer Vision) that I developed has the ability to detect and classify objects as either a `Bike` or a `Car`. Basically, this model is made to be applied in parking lots or building garages. Since the function of this model is classification, it can be used to count the number of parking users based on their vehicle type. This helps to determine the optimal parking capacity for motorcycles and cars. Furthermore, if developed further, this model can also automate parking fees based on the vehicle type.

## Project Output

The output of this project is a Computer Vision model that can classify Motorcycles and Cars.

## Data

The dataset used is a collection of images, consisting of 2,000 images of bikes and 2,000 images of cars. These images have different sizes, so I performed feature engineering using `ImageDataGenerator`.

## Method

In this project, I initially tried to perform model improvement by adding more layers and adjusting the parameters to get better accuracy. However, I found that the base model actually performed more consistently during testing. The improvement attempt resulted in a "failure" (likely due to overfitting or unstable loss), which is why I chose to use the base model for the final deployment. It provides the most reliable classification for detecting bikes and cars in different lighting and angles.

## Stacks

1. Programming Language : Python
2. Tools                : Visual Studio Code, HuggingFace, GitHub, Streamlit
3. Library              : pandas, numpy, scipy, seaborn, matplotlib, tensorflow, pickle, streamlit,plotly, pillow

## Reference

URL Dataset     : https://www.kaggle.com/datasets/utkarshsaxenadn/car-vs-bike-classification-dataset

URL Deployment  : https://huggingface.co/spaces/shakurhs/Computer_Vision_BikeorCar

URL Model       : Best Model https://huggingface.co/spaces/shakurhs/Computer_Vision_BikeorCar/blob/main/model1_checkpoint.keras

                  GDrive Folder https://drive.google.com/drive/folders/1cD5YXnsDM5h51ZcXKgItThOTkNpLklv8?usp=drive_link

---