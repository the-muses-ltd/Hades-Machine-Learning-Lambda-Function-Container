# Introducing Hades Machine Learning Lambda Container
Hades invests a lot of time figuring out how to distribute Machine Learning Models on the cloud, we are making all our DevOps and MLOps work open source so you don't have to. Use this custom Image to server your Machine Learning Models on AWS Lambda.

## How to use this custom container setup:

## How to use your own saved models:
All you need to do is swap out your saved model with the one saved in the app folder and you're good to go, it really is that easy! 

Things to note:
1. We suggest saving your model in .h5 format to ensure compatibility.

## Prerequisites:
To use this contianer you'll need:
1. Docker Desktop Installed https://www.docker.com/products/docker-desktop
2. The Docker CLI installed on your local machine.
3. Your model will need to be trained with Tensorflow 2 or above and ideally saved with Keras.