from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

request_presigned_url = {}

class Teams(Resource):

    def get(self, teamID):
        team = {'teamID':teamID}
        if team['teamID'] == teamID:
            return {'resultImageUrl':request_presigned_url[teamID]}
        else:
            return "Error", 404
    
    def post(self, teamID):
        team = {'teamID':teamID}
        req_data = request.get_json()
        preSignedUrl = req_data["resultImageUrl"]
        resultImageUrl = preSignedUrl.split("?")[0]
        request_presigned_url[teamID] = resultImageUrl
        return team
    
    def delete(self, teamID):
        for ind,team in enumerate(request_presigned_url):
            if team['teamID'] == teamID:
                deleted_team = request_presigned_url.pop(ind)
                return {'note':'delete success'}

api.add_resource(Teams,'/teams/<int:teamID>')

if __name__ == '__main__':
    app.run(debug=True)
