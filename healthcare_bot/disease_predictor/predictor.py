# disease_predictor/predictor.py
from keras.models import load_model
import os

class DiseasePredictor:
    model = None

    @classmethod
    def load_model(cls):
        if cls.model is None:
            # Provide the absolute path to the .h5 file
            model_path = '/Users/ChrisPowell/Desktop/Software Engineer Projects/ADVANCE/AI-Healthcare-Bot-System-using-Python/healthcare_bot/disease_prediction_model.h5'
            cls.model = load_model(model_path)

    @classmethod
    def predict(cls, input_data):
        return cls.model.predict(input_data)
