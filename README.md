# AI-Powered Image Prediction: Bike or Car

## Repository Outline

Penjelasan Mengenai Isi dari Tiap File dan Folder:

1. model_building.ipynb - Notebook yang berisi pengolahan data dengan python dimulai dari loading dataset, proses EDA, data augmentation, model training, evaluasi model.
2. model_inf.ipynb - Notebook Data Inference yang berisi kegiatan mulai dari loading model hingga melakukan klasifikasi
3. url.txt - File yang berisikan url Dataset, url Deployment, dan best model. 
4. Deployment - Folder yang berisikan file terkait untuk melakukan deployment ke HuggingFace.

## Problem Background

Model Deep Learning berupa Computer Vision yang saya kembangkan memiliki kemampuan untuk melakukan deteksi dan klasifikasi tterhadap objek berupa `Bike` atau `Car`. Pada dasarnya model ini dibuat bertujuan untuk diaplikasikan pada lapangan atau gedung parkir. Dikarenakan fungsi dari model ini adalah untuk melakukan klasifikasi, sehingga bisa dilakukan perhitungan terhadap jumlah pengguna lahan parkir berdasarkan kendaraan yang digunakan dengan maksud untuk menentukan berapa jumlah kapasitas parkir motor dan mobil yang optimal. Selain itu, jika dilakukan perkembangan lebih lanjut model ini juga dapat melakukan otomatisasi dalam menentukan harga parkir berdasarkan jenis kendaraan.

## Project Output

Output yang dihasilkan berupa model Computer Vision yang dapat melakukan klasifikasi terhadap Motor dan Mobil.

## Data

Dataset yang digunakan berupa kumpulan gambar, terdiri atas 2000 gambar motor dan 2000 gambar mobil. Gambar-gambar tersebut memiliki ukuran yang berbeda-beda sehingga dilakukan feature engineering menggunakan ImageDataGenerator.

## Method

Project ini adalah sebuah project Deep Learning untuk menentukan sebuah gambar apakah termasuk kedalam kelas `Bike` atau `Car`. Setelah melakukan upload dataset, kemudian dilakukan eksplorasi pada data tersebut. Proses selanjutnya adalah feature engineering berupa penyeragaman ukuran gambar, data augmentation, dan lainnya. Setelah itu, dengan menggunakan tensorflow, dilaksanakan model training serta model improvement. Namun terdapat kegagalan pada saat improvement sehingga model yang digunakan untuk data inference adalah base model.

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