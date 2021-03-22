
# Deep Learning
import numpy as np
from tensorflow.keras.models import load_model

# Flask
import flask
from flask import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# 학습 모델 불러오기
model = load_model('final_model.h5')

from flask_cors import CORS
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
