
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

@app.route('/predict',methods=['GET'])
def predict():
    
    # 필요한 변수 명 : ['period', 'class_buy_counts', '101_counts', 'page_view_counts','page_view_kinds', 'wishlist_count', 'reward_counts']
    # 해당 변수 웹페이지에서 가져온다.
    input_variables = ['period', 'class_buy_counts', '101_counts', 'page_view_counts','page_view_kinds', 'wishlist_count', 'reward_counts']
    input_features = [int(request.form.get(i)) for i in input_variables]
    final = [np.array(input_features)].values
    
    # 모델 예측
    prediction = model.predict_classes(final)

    # 예측값 결과 : 0은 쿠폰 반응도 낮은 리스트이고 1과 2는 쿠폰 반응도 높은 리스트이므로 예측값이 1, 2 인 고객들에게 쿠폰을 제시한다.
    if prediction == 0:
        return render_template('webservice.html', pred = '쿠폰 발행 대상이 아닙니다.')
    else:
        return render_template('webservice.html', pred = '쿠폰 발행 대상입니다!!!')

if __name__ == '__main__':
    app.run(debug=True)
