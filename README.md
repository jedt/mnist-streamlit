# mnist-streamlit

Machine learning Handwritten digit recognition using the MNIST database and Streamlit

Introduction
According to Wikipedia, the MNIST stands for Modified National Institute of Standards and Technology database is a large database of handwritten digits that is commonly used for training various image processing systems. The MNIST database consists of 60,000 training images and 10,000 testing images, which are digits written by high school students and employees of the United States Census Bureau.
The dataset is considered the "hello, world" of machine learning. Each image is small, 28x28 pixels, and labeled according to its numeric representation.
Streamlit is a Python library that lets anyone transform Python scripts into single-page web apps in just a few lines of code.

This project aims to train a model in Pytorch that would predict any user-drawn digits from their browser. 

## Features
The project provides a Jupyter Notebook [training code](https://github.com/jedt/mnist-streamlit/blob/main/train_mnist.ipynb) for the digit classifier and a web app enabling the model to predict new user-drawn digits from the web app via HTML5 canvas.
The [model](https://github.com/jedt/mnist-streamlit/blob/main/model.py) is a convolutional neural network (CNN) and is specifically designed for image classification or, more precisely, for the MNIST dataset.

## Getting Started
To be able to run the project, make sure Python 3.9 or later is installed and run:
`pip install -r requirements.txt`

To test the pre-trained classifier model included in the repo:

`streamlit run app.py`

To train a new model, open the jupyter notebook

`jupyter notebook train_mnist.ipynb`

<img src="https://lh3.googleusercontent.com/u/0/drive-viewer/AEYmBYSLJIQkSjR0SqTfOHK8k2GlnboTtxsurrFlNanm6VPqgljQlHDDr3mm3jFPnSL_HGM9ufLXgzzixQxNm-OpiZrm9CTynQ=w2992-h1624" class="ndfHFb-c4YZDc-HiaYvf-RJLb9c" alt="Displaying screenshot-mnist.gif" aria-hidden="true" width="400">

## Training accuracy results

```
Train Epoch: 70 	Average Loss: 0.006639	Accuracy: 99.76%
Train Epoch: 71 	Average Loss: 0.007192	Accuracy: 99.78%
Train Epoch: 72 	Average Loss: 0.005899	Accuracy: 99.81%
Train Epoch: 73 	Average Loss: 0.005731	Accuracy: 99.80%
Train Epoch: 74 	Average Loss: 0.005509	Accuracy: 99.80%
Train Epoch: 75 	Average Loss: 0.005899	Accuracy: 99.78%
Train Epoch: 76 	Average Loss: 0.005147	Accuracy: 99.82%
Train Epoch: 77 	Average Loss: 0.006637	Accuracy: 99.77%
Train Epoch: 78 	Average Loss: 0.005603	Accuracy: 99.81%
Train Epoch: 79 	Average Loss: 0.005901	Accuracy: 99.80%
Train Epoch: 80 	Average Loss: 0.005696	Accuracy: 99.80%
```
