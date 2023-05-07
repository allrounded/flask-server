from flask import Flask, render_template, jsonify, request
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, REGION_NAME, BUCKET_NAME
# from flask_cors import CORS
from tables_result import tables_final_result
from one_table_processing import one_table_processing
import boto3
import json

from PIL import Image
import numpy as np
import io

app = Flask(__name__)
# CORS(app)


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
            return jsonify({'message': "이미지 검증 성공", 'data': 'true'}), 200
        return jsonify({'message': "이미지 검증 실패", 'data': 'false'}), 200

    except Exception as e:
        return jsonify({'message': '이미지 검증 오류', 'error': str(e)}), 400



# Image Processing
@app.route('/teams/<int:teamId>', methods=['POST'])
def img_processing(teamId):
    try:
        # 1. 데이터 받기 (teamID 내에 있는 url들)
        urls = []
        response = request.get_json()
        for obj in response.get('images', []):
            file_key = obj.get('url')
            urls.append(file_key)


        # 2. 프로세싱 적용
        frames = []
        time_list = []
        for image in enumerate(urls):
            one_table_result = one_table_processing.img_to_dataframe(image[1])
            frames.append(one_table_result)
        final_result = tables_final_result.get_final_result(frames) # 결과 데이터프레임
        
        # API에 보낼 데이터 리스트 만들기
        for key in list(final_result.keys()):
            times = final_result.index[final_result[key]==1].tolist()
            for time in times:
                dict = {"dayOfWeek": key, "time": time}
                time_list.append(dict)


        # 3. 이미지 만들기
        # 3-1. S3 url에 이미지 업로드
        # image_upload = requests.put(presigned_url, data=result)
        
        return jsonify({'resultImageUrl': response['resultImageUrl'],
                        'timeResponses': {
                            "divisorMinutes" : 30,
                            "times" : time_list
                        }}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
