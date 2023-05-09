from flask import Flask, render_template, jsonify, request
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, REGION_NAME, BUCKET_NAME
from img_table_processing import one_table_processing
from img_final_result import result_timetable
from flask_cors import CORS
import boto3


app = Flask(__name__)
CORS(app)

s3 = boto3.client(
    "s3",
    endpoint_url=None,
    region_name=REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
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
        req_data = request.get_json()
        resultImageUrl = req_data["resultImageUrl"]
        resultImage = req_data['timeResponses']["times"]
        
        final_result_filename = result_timetable.data_to_img(resultImage)
        key = "image/sample_5.JPG"
        
        with open(final_result_filename, 'rb') as f:
            s3.put_object(
                    Bucket=BUCKET_NAME,
                    Body=f,
                    Key=key,
                    ContentType='image/jpeg'
                )

        return jsonify({'resultImageUrl': resultImageUrl}), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 400



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
