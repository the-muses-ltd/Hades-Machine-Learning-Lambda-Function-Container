# Once your container is running. Use this file to test the lambda function!
# What does this test do? It will pick an image from the MNIST dataset, encode it as JSON and make a post request to your locally running lambda function.
# You should receive a response with your models prediction!
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.datasets import mnist
import os
import requests
import json
from json import JSONEncoder

# Class for encoding your numpy arrays into JSON
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

# Load MNIST dataset
(input_train, target_train), (input_test, target_test) = mnist.load_data()
img_width, img_height = 28, 28

# Reshape data    
input_test = input_test.reshape((input_test.shape[0], img_width, img_height, 1))
input_shape = (img_width, img_height, 1)

# Cast input to float32
input_test = input_test.astype('float32')

# Normalize data
input_test = input_test / 255

# Generate a prediction with loaded model
sample_index = 788
sample_input, sample_target = input_test[sample_index], target_test[sample_index]
sample_input_array = np.array([sample_input])

lists = sample_input_array.tolist()
json_str = json.dumps(lists)

# Converting test data to a dict
data = {
    'test_data': sample_input_array
}
# Converting test data to JSON
encodedNumpyData = json.dumps(data, cls=NumpyArrayEncoder)  

# Post locally to our lambda function to check if it is working:
response = requests.post('http://localhost:9000/2015-03-31/functions/function/invocations', data=encodedNumpyData)
print(response.json()['prediction'])