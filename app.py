# -*- conding: utf-8 -*-

# Deep Learning
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Flask
import flask
from flask import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# load model
model = load_model('oversampling_easy.h5')
model.call = tf.function(model.call)

# main index page route
@app.route('/')
def home():
    return '<h1>API is working...!!! </h1>'

@app.route('/predict', methods=['POST'])
def predict():
    data = np.array([request.get_json()])
    prediction = model.predict(data).tolist()

    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')

