## Class101 TIPS

클래스101 팁스 과제 모델 서빙 API

### Test & Development

```bash
python app.py
```

### Docker

tips-service/values.yaml에 업데이트한 도커 이미지 태그 수정 후 Push 하기

```bash
docker build . -t 212011163676.dkr.ecr.ap-northeast-2.amazonaws.com/class101-tips:1.0.1
docker push 212011163676.dkr.ecr.ap-northeast-2.amazonaws.com/class101-tips:1.0.1
docker run -it 212011163676.dkr.ecr.ap-northeast-2.amazonaws.com/class101-tips:1.0.1
```
