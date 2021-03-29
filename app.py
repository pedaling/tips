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

    CORS(app)

    # main index page route
    @app.route('/')
    def home():
        return '<h1>API is working... </h1>'

    @app.route('/predict', methods=['GET'])
    def predict():
        data = request.get_json()
        prediction = np.array2string(model.predict(data))

        return jsonify(prediction)

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')

    return app
