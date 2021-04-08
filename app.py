# -*- conding: utf-8 -*-

# Deep Learning
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Flask
import flask
from flask import *


def create_app():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = False

    # load model
    model = load_model('tips_model_1.h5')
    model.call = tf.function(model.call)

    # main index page route
    @app.route('/')
    def home():
        return '<h1>API is working...!!! </h1>'

    @app.route('/predict', methods=['POST'])
    def predict():
        data = np.array([request.get_json()])
        prediction = model.predict_classes(data).tolist()
        print('\n')
        print('!!!!!!!!!!!!!!!data input success!!!!!!!!!!!!!!!')
        print('\n')
        return jsonify(prediction)

    if __name__ == '__main__':
        app.run(debug=False, host='0.0.0.0', port='5000')
    
    return app
