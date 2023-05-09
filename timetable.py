import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, request
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)

class Result(Resource):

    def post(self, teamID):
        req_data = request.get_json()
        resultImageUrl = req_data["resultImageUrl"]
        resultImage = req_data["time"]

        #when importing json data use pd_object = pd.read_json(whatever)

        df = pd.DataFrame(resultImage)

        timeSegment = ["9:00~9:30",
               "9:30~10:00",
               "10:00~10:30",
               "10:30~11:00",
               "11:00~11:30",
               "11:30~12:00",
               "12:00~12:30",
               "12:30~13:00",
               "13:00~13:30",
               "13:30~14:00",
               "14:00~14:30",
               "14:30~15:00",
               "15:00~15:30",
               "15:30~16:00",
               "16:00~16:30",
               "16:30~17:00",
               "17:00~17:30",
               "17:30~18:00",
               "18:00~18:30",
               "18:30~19:00",
               "19:00~19:30",
               "19:30~20:00",
               "20:00~20:30",
               "20:30~21:00",
               "21:00~21:30",
               "21:30~22:00",
               "22:00~22:30",
               "22:30~23:00",
               "23:00~23:30",
               "23:30~24:00"]

        fig, ax = plt.subplots()

        timetable = ax.table(cellText=df.values, cellLoc='center', colLabels=list(resultImage.keys()), rowLabels=timeSegment[0:len(df.values)], rowLoc='center', loc='center')
        ax.axis('off')

        #change color based on value
        for i in range(0,len(df.values)+1):
            for j in range(0,len(resultImage.keys())):
                cell = timetable[i,j]
                cell_value = cell.get_text().get_text()
                if cell_value == "0":
                    cell.set_facecolor('orange')
                elif cell_value == "1":
                    cell.set_facecolor('gray')

        #change height of rows
        for i in range(0, len(resultImage.keys())):
            for j in range(1, len(df.values)+1):
                cell = timetable[j,i]
                cell.set_height(0.2)
            
        #change height of row headers
        for i in range(-1, len(resultImage.keys())):
            for j in range(1, len(df.values)+1):
                cell = timetable[j,i]
                cell.set_height(0.2)

        #hide text
        for i in range(0, len(resultImage.keys())):
            for j in range(1, len(df.values)+1):
                cell = timetable[j,i]
                cell.get_text().set_visible(False)

        #row header boundary
        for j in range(1, len(df.values)+1):
            cell = timetable[j,-1]
            cell.set_edgecolor('black')
        
        plt.savefig('tttrial.png')
        return resultImage

api.add_resource(Result,'/teams/<int:teamID>/result')

if __name__ == '__main__':
    app.run(debug=True)