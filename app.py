from flask import Flask, jsonify, request, abort
#from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, REGION_NAME, BUCKET_NAME
from img_table_processing import one_table_processing
from img_final_result import result_timetable
from werkzeug.exceptions import BadRequest
from flask_cors import CORS
import boto3


app = Flask(__name__)
CORS(app)

# s3 = boto3.client(
#     "s3",
#     endpoint_url=None,
#     region_name=REGION_NAME,
#     aws_access_key_id=AWS_ACCESS_KEY,
#     aws_secret_access_key=AWS_SECRET_KEY
# )
s3 = boto3.client("s3")


# Image Processing
@app.route('/teams/<int:teamId>/members/<int:memberId>', methods=['POST'])
def img_processing(teamId, memberId):
    try:
        response = request.get_json()
        img_url = response.get('imageUrl')
        
        one_table_result = one_table_processing.img_to_dataframe(img_url)
        print(one_table_result)
        
        time_response = []
        for col in list(one_table_result.columns):
            time = {"dayOfWeek": col}
            time["time"] = one_table_result[col].values.tolist()
            time_response.append(time)
        
        return jsonify({
            'code': 200,
            'timeResponses': {
                            "divisorMinutes" : 30,
                            "times" :  time_response
                        }}), 200
    except BadRequest:
        return jsonify({'message': 'Bad request', "code": 400}), 400
    except Exception as e:
        return jsonify({'message': str(e), "code": 500}), 500
    
    
    
# Result Image 
@app.route('/teams/<int:teamId>/results', methods=['POST'])
def img_result(teamId):
    try:
        req_data = request.get_json()
        resultImageUrl = req_data["resultImageUrl"]
        resultImage = req_data['timeResponses']["times"]
        
        final_result_filename = result_timetable.data_to_img(resultImage)
        key = "image/sample_5.JPG"
        
        with open(final_result_filename, 'rb') as f:
            s3.put_object(
                    Bucket="mogong",
                    Body=f,
                    Key=key,
                    ContentType='image/jpeg'
                )

        return jsonify({
            'code': 200,
            'resultImageUrl': resultImageUrl
            }), 200

    except BadRequest:
        return jsonify({'message': 'Bad request', "code": 400}), 400
    except Exception as e:
        return jsonify({'message': str(e), "code": 500}), 500





if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
