from flask import Flask, render_template, jsonify, request
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, REGION_NAME, BUCKET_NAME
# from flask_cors import CORS
from img_tables_result import tables_final_result
from img_table_processing import one_table_processing
import boto3



app = Flask(__name__)
# CORS(app)

s3 = boto3.client('s3',
                  endpoint_url=None,
                  aws_access_key_id=AWS_ACCESS_KEY,
                  aws_secret_access_key=AWS_SECRET_KEY,
                  region_name=REGION_NAME
                  )


# Image Processing
@app.route('/teams/<int:teamId>', methods=['POST'])
def img_processing(teamId):
    try:
        response = request.get_json()
        img_url = response.get('imagesUrl')
        one_table_result = one_table_processing.img_to_dataframe(img_url)
        print(one_table_result)
        
        time_response = []
        for col in list(one_table_result.columns):
            time = {"dayOfWeek": col}
            time["time"] = one_table_result[col].values.tolist()
            time_response.append(time)
        
        return jsonify({'timeResponses': {
                            "divisorMinutes" : 30,
                            "times" :  time_response
                        }}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    
    
# Result Image 
@app.route('/result_img', methods=['POST'])
def img_result():
    try:
#         # S3 이미지 URL 가져오기
#         s3_image_url = request.get_json()['imageValidateUrl']

#         # S3 이미지 다운로드 및 PIL 이미지 객체로 변환
#         filename = s3_image_url.split('/')[-2:]
#         key = f'{filename[0]}/{filename[1]}'
#         s3_image_object = s3.get_object(Bucket=BUCKET_NAME, Key=key)
#         s3_image_data = s3_image_object['Body'].read()
#         image_pil = Image.open(io.BytesIO(s3_image_data))
#         image_np = np.array(image_pil)

#         # 시간표 이미지 검증 함수 적용
#         # validated_result = 시간표이미지검증함수(image_np)
#         validated_result = True  # 임의 테스트용

#         # 결과 도출
#         if validated_result == True:
#             return jsonify({'message': "이미지 검증 성공", 'data': 'true'}), 200
#         return jsonify({'message': "이미지 검증 실패", 'data': 'false'}), 200

#     except Exception as e:
#         return jsonify({'message': '이미지 검증 오류', 'error': str(e)}), 400



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
