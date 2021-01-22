from tensorflow.keras.models import load_model
import numpy as np

def handler(event, context): 
    # Load your pre-trained model:
    filepath = 'saved_model.h5'
    loaded_model = load_model(
        filepath,
        custom_objects=None,
        compile=True
    )
    # Convert your test data from a dict to numpy array:
    sample_input_array = np.array(event['test_data'])
    # Make a prediction:
    predictions = loaded_model.predict(sample_input_array)
    prediction = np.argmax(predictions[0])
    # Log your prediction for debuging:
    print(prediction)
    # Return json formatted response, to return your prediction:
    response = {
        'prediction': str(prediction)
    }
    return response