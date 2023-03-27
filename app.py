from flask import Flask, render_template, jsonify, request
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, REGION_NAME, BUCKET_NAME
# from flask_cors import CORS
# from s3 import S3Connection
import boto3
import requests

from PIL import Image
import numpy as np
import io

app = Flask(__name__)
# CORS(app)

# 모델 로드 및 예측 함수 정의
# def load_model():
#     # 모델 로드 코드 작성
#     return model

# def predict(model, image):
#     # 예측 함수 코드 작성
#     return prediction

s3 = boto3.client('s3',
                  endpoint_url=None,
                  aws_access_key_id=AWS_ACCESS_KEY,
                  aws_secret_access_key=AWS_SECRET_KEY,
                  region_name=REGION_NAME
                  )


# Image Validation
@app.route('/validate', methods=['POST'])
def img_validate():
   try:
      # S3 이미지 URL 가져오기
      s3_image_url = request.get_json()['imageValidateUrl']

      # S3 이미지 다운로드 및 PIL 이미지 객체로 변환
      filename = s3_image_url.split('/')[-2:]
      key = f'{filename[0]}/{filename[1]}'
      s3_image_object = s3.get_object(Bucket=BUCKET_NAME, Key=key)
      s3_image_data = s3_image_object['Body'].read()
      image_pil = Image.open(io.BytesIO(s3_image_data))
      image_np = np.array(image_pil)

      # 시간표 이미지 검증 함수 적용
      # validated_result = 시간표이미지검증함수(image_np)
      validated_result = True  # 임의 테스트용

      # 결과 도출
      if validated_result == True:
         return jsonify({'message': "이미지 검증 성공", 'data': True}), 200
      return jsonify({'message': "이미지 검증 실패", 'data': False}), 200

   except Exception as e:
      return jsonify({'message': '이미지 검증 오류', 'error': str(e)}), 400



# Request presigned url
def request_presigned_url():
   # S3 presigned URL 요청 API의 URL & 헤더정보 & 데이터
   api_url = "https://<spring-server-url>/image"
   headers = {
      "Content-Type": "application/json"
   }
   data = {
      "extention": ".JPG"
   }

   response = requests.post(api_url, json=data, headers=headers)

   if response.status_code == 200:
      presigned_url = response.json()["data"]["preSignedUrl"]
      filename = response.json()["data"]["filename"]
      return f"{presigned_url}/{filename}"
   else:
      response.raise_for_status()



# Image Processing
@app.route('/<int:teamID>', methods=['POST'])
def img_processing(teamID):
   try:
      # 1. 데이터 받기 (teamID 내에 있는 url들?)
      response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=teamID)
      for obj in response.get('Contents', []):
         file_key = obj.get('Key')
         print(file_key)

      # 2. presigned_url 요청
      presigned_url = request_presigned_url()

      # 2. 모델에 적용
      # model = load_model()
      # prediction = predict(model, image_np)
      result = 'result_file' # 임의 테스트용

      # 3. 결과 도출
      # 3-1. S3 url에 이미지 업로드
      image_upload = requests.put(presigned_url, data=result)

      # 3-2. return -> 결과 이미지 url과 30분 단위로 쪼갠 텍스트 뭉치 보내기
      return jsonify({'message': "팀 결과 생성에 성공했습니다",
                     'data': {
                        "times": [{
                              "dayOfWeek": "MON",
                              "time": "09:00~09:30"
                        }, {
                              "dayOfWeek": "MON",
                              "time": "09:30~10:00"
                        }, {
                              "dayOfWeek": "SUN",
                              "time": "09:00~09:30"
                        }]}}), 200

   except Exception as e:
      return jsonify({'message': str(e)}), 400


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
