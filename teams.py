import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

request_presigned_url = {}
result_image_url = {}

class Teams(Resource):
    
    def post(self, teamID):
        req_data = request.get_json()
        preSignedUrl = req_data["images"]
        resultImageUrl = req_data["resultImageUrl"]
        request_presigned_url[teamID] = preSignedUrl
        result_image_url[teamID] = resultImageUrl
        response = {
  "resultImageUrl" : result_image_url[teamID],
  "timeResponses": {
    "divisorMinutes" : 30,
    "times": [
      {
        "dayOfWeek": "MON",
        "time": "09:00~09:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "09:30~10:00"
      },
      {
        "dayOfWeek": "MON",
        "time": "10:00~10:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "10:30~11:00"
      },
      {
        "dayOfWeek": "MON",
        "time": "11:00~11:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "11:30~12:00"
      },
      {
        "dayOfWeek": "MON",
        "time": "12:00~12:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "12:30~13:00"
      },
      {
        "dayOfWeek": "MON",
        "time": "13:00~13:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "13:30~14:00"
      },
      {
        "dayOfWeek": "MON",
        "time": "14:00~14:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "14:30~15:00"
      },
      {
        "dayOfWeek": "MON",
        "time": "15:00~15:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "15:30~16:00"
      },
      {
        "dayOfWeek": "MON",
        "time": "16:00~16:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "16:30~17:00"
      },
      {
        "dayOfWeek": "MON",
        "time": "17:00~17:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "17:30~18:00"
      },
      {
        "dayOfWeek": "MON",
        "time": "18:00~18:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "18:30~19:00"
      },
      {
        "dayOfWeek": "MON",
        "time": "19:00~19:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "19:30~20:00"
      },
      {
        "dayOfWeek": "MON",
        "time": "20:00~20:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "20:30~21:00"
      },
      {
        "dayOfWeek": "MON",
        "time": "21:00~21:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "21:30~22:00"
      },
      {
        "dayOfWeek": "MON",
        "time": "22:00~22:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "22:30~23:00"
      },
      {
        "dayOfWeek": "MON",
        "time": "23:00~23:30"
      },
      {
        "dayOfWeek": "MON",
        "time": "23:30~24:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "09:00~09:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "09:30~10:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "10:00~10:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "10:30~11:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "11:00~11:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "11:30~12:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "12:00~12:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "12:30~13:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "13:00~13:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "13:30~14:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "14:00~14:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "14:30~15:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "15:00~15:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "15:30~16:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "16:00~16:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "16:30~17:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "17:00~17:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "17:30~18:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "18:00~18:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "18:30~19:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "19:00~19:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "19:30~20:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "20:00~20:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "20:30~21:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "21:00~21:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "21:30~22:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "22:00~22:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "22:30~23:00"
      },
      {
        "dayOfWeek": "TUE",
        "time": "23:00~23:30"
      },
      {
        "dayOfWeek": "TUE",
        "time": "23:30~24:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "09:00~09:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "09:30~10:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "10:00~10:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "10:30~11:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "11:00~11:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "11:30~12:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "12:00~12:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "12:30~13:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "13:00~13:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "13:30~14:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "14:00~14:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "14:30~15:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "15:00~15:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "15:30~16:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "16:00~16:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "16:30~17:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "17:00~17:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "17:30~18:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "18:00~18:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "18:30~19:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "19:00~19:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "19:30~20:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "20:00~20:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "20:30~21:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "21:00~21:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "21:30~22:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "22:00~22:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "22:30~23:00"
      },
      {
        "dayOfWeek": "WED",
        "time": "23:00~23:30"
      },
      {
        "dayOfWeek": "WED",
        "time": "23:30~24:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "09:00~09:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "09:30~10:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "10:00~10:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "10:30~11:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "11:00~11:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "11:30~12:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "12:00~12:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "12:30~13:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "13:00~13:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "13:30~14:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "14:00~14:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "14:30~15:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "15:00~15:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "15:30~16:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "16:00~16:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "16:30~17:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "17:00~17:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "17:30~18:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "18:00~18:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "18:30~19:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "19:00~19:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "19:30~20:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "20:00~20:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "20:30~21:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "21:00~21:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "21:30~22:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "22:00~22:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "22:30~23:00"
      },
      {
        "dayOfWeek": "THU",
        "time": "23:00~23:30"
      },
      {
        "dayOfWeek": "THU",
        "time": "23:30~24:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "09:00~09:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "09:30~10:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "10:00~10:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "10:30~11:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "11:00~11:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "11:30~12:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "12:00~12:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "12:30~13:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "13:00~13:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "13:30~14:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "14:00~14:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "14:30~15:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "15:00~15:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "15:30~16:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "16:00~16:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "16:30~17:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "17:00~17:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "17:30~18:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "18:00~18:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "18:30~19:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "19:00~19:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "19:30~20:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "20:00~20:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "20:30~21:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "21:00~21:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "21:30~22:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "22:00~22:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "22:30~23:00"
      },
      {
        "dayOfWeek": "FRI",
        "time": "23:00~23:30"
      },
      {
        "dayOfWeek": "FRI",
        "time": "23:30~24:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "09:00~09:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "09:30~10:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "10:00~10:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "10:30~11:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "11:00~11:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "11:30~12:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "12:00~12:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "12:30~13:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "13:00~13:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "13:30~14:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "14:00~14:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "14:30~15:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "15:00~15:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "15:30~16:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "16:00~16:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "16:30~17:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "17:00~17:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "17:30~18:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "18:00~18:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "18:30~19:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "19:00~19:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "19:30~20:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "20:00~20:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "20:30~21:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "21:00~21:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "21:30~22:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "22:00~22:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "22:30~23:00"
      },
      {
        "dayOfWeek": "SAT",
        "time": "23:00~23:30"
      },
      {
        "dayOfWeek": "SAT",
        "time": "23:30~24:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "09:00~09:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "09:30~10:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "10:00~10:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "10:30~11:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "11:00~11:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "11:30~12:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "12:00~12:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "12:30~13:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "13:00~13:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "13:30~14:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "14:00~14:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "14:30~15:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "15:00~15:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "15:30~16:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "16:00~16:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "16:30~17:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "17:00~17:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "17:30~18:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "18:00~18:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "18:30~19:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "19:00~19:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "19:30~20:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "20:00~20:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "20:30~21:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "21:00~21:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "21:30~22:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "22:00~22:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "22:30~23:00"
      },
      {
        "dayOfWeek": "SUN",
        "time": "23:00~23:30"
      },
      {
        "dayOfWeek": "SUN",
        "time": "23:30~24:00"
      }]}}
        return json.dumps(response), 200

api.add_resource(Teams,'/teams/<int:teamID>')

if __name__ == '__main__':
    app.run(debug=True)
