# -*- conding: utf-8 -*-

# Deep Learning
import numpy as np
from tensorflow.keras.models import load_model

# Flask
import flask
from flask import *
from flask_cors import CORS

def create_app():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    # load model
    model = load_model('final_model.h5')
    model.call = tf.function(model.call)

    CORS(app)

    # main index page route
    @app.route('/')
    def home():
        return '<h1>API is working... </h1>'

    @app.route('/predict', methods=['POST'])
    def predict():
        data = np.array([request.get_json()])
<<<<<<< HEAD
        prediction = np.array2string(model.predict_classes(data)).tolist()
=======
        prediction = model.predict_classes(data).tolist()
>>>>>>> 3a0bf3e25a29b6dfa6fb2cd693fc570a88d4d1c5

        return jsonify(prediction)

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')

    return app
