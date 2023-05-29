import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, request
from flask_restful import Resource, Api
import matplotlib.image as image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


app=Flask(__name__)
api=Api(app)

class Result(Resource):

    def post(self, teamID):
        req_data = request.get_json()
        resultImageUrl = req_data["resultImageUrl"]
        resultImage = req_data["time"]

        #when importing json data use pd_object = pd.read_json(whatever)

        df = pd.DataFrame(resultImage)
        df.insert(0, "null", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], True)
        fig, ax = plt.subplots(figsize=(15,18))
        plt.subplots_adjust()
        plt.rcParams['text.color']='none'
        kl = len(df.keys())
        vl = len(df.values)

        timetable = plt.table(cellText=df.values,
                      cellLoc='center',
                      colLabels=df.keys(),
                      loc='center',
                      zorder=2,
                      bbox=(0,0,1,1))
        
        ax.axis(xmax=kl, ymax=vl+4)
        ax.axis('off')

        #data cells
        for i in range(1,vl+1):
            for j in range(0,kl):
                cell = timetable[i,j]
                cell.set_height(0.1)
                cell.get_text().set_visible(False)
                cell_value = cell.get_text().get_text()
                if cell_value == "1":
                    cell.set_facecolor('#FF9836')
                    cell.set_edgecolor('#FF9836')
                elif cell_value == "0":
                    cell.set_facecolor('white')
                    cell.set_edgecolor('white')

        #col headers
        for i in range(0, kl):
                cell = timetable[0,i]
                cell.set_height(0.4)
                cell.visible_edges = 'open'

        #column lines
        for x in range(0, kl+1):
            ax.plot([x,x], [0, vl+2], lw=1.15, color='#C5C5C5', zorder=3, marker='')

        #row header lines
        for x in range(0,vl+2):
            if x%2 == 0:
                ax.plot([0,kl+1], [x,x], lw=1, color='#C5C5C5', zorder=3, marker='')

        #column header row lines
        ax.plot([0,9], [32,32], lw=1, color='#C5C5C5', zorder=3, marker='')

        #bottom row
        ax.plot([0,9],[0,0], lw=1.5, color='#C5C5C5', zorder=3, marker='')
            
        #white halfline
        for i in range(0,vl):
            for j in range(1,kl):
                cell = timetable[i,j]
                cell_value = cell.get_text().get_text()
                cell1 = timetable[i+1,j]
                cell_value1 = cell1.get_text().get_text()
                if cell_value != cell_value1:
                    ax.plot([j,j+1], [30-i,30-i], lw=1, color='#C5C5C5', zorder=3, marker='')
                    
        #blank column
        for x in range(0, vl+1):
            cell = timetable[x,0]
            cell.visible_edges = 'open'

        #end borders
            
        #monday image
        file = 'monday.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.3)
        ab = AnnotationBbox(imagebox, (1.5,31), frameon = False)
        ax.add_artist(ab)

        #tuesday image
        file = 'tuesday.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.3)
        ab = AnnotationBbox(imagebox, (2.5,31), frameon = False)
        ax.add_artist(ab)

        #wednesday image
        file = 'wednesday.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.3)
        ab = AnnotationBbox(imagebox, (3.5,31), frameon = False)
        ax.add_artist(ab)

        #thursday image
        file = 'thursday.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.3)
        ab = AnnotationBbox(imagebox, (4.5,31), frameon = False)
        ax.add_artist(ab)

        #friday image
        file = 'friday.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.3)
        ab = AnnotationBbox(imagebox, (5.5,31), frameon = False)
        ax.add_artist(ab)

        #saturday image
        file = 'saturday.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.3)
        ab = AnnotationBbox(imagebox, (6.5,31.03), frameon = False)
        ax.add_artist(ab)

        #sunday image
        file = 'sunday.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.3)
        ab = AnnotationBbox(imagebox, (7.5,31), frameon = False)
        ax.add_artist(ab)

        #9am image
        file = 'nine.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,29), frameon = False)
        ax.add_artist(ab)

        #10am image
        file = 'ten.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,27), frameon = False)
        ax.add_artist(ab)

        #11am image
        file = 'eleven.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,25), frameon = False)
        ax.add_artist(ab)

        #12pm image
        file = 'twelve.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,23), frameon = False)
        ax.add_artist(ab)

        #1pm image
        file = 'one.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,21), frameon = False)
        ax.add_artist(ab)

        #2pm image
        file = 'two.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,19), frameon = False)
        ax.add_artist(ab)

        #3pm image
        file = 'three.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,17), frameon = False)
        ax.add_artist(ab)

        #4pm image
        file = 'four.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,15), frameon = False)
        ax.add_artist(ab)

        #5pm image
        file = 'five.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,13), frameon = False)
        ax.add_artist(ab)

        #6pm image
        file = 'six.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,11), frameon = False)
        ax.add_artist(ab)

        #7pm image
        file = 'seven.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,9), frameon = False)
        ax.add_artist(ab)

        #8pm image
        file = 'eight.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,7), frameon = False)
        ax.add_artist(ab)

        #9pm image
        file = 'nine.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,5), frameon = False)
        ax.add_artist(ab)

        #10pm image
        file = 'ten.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,3), frameon = False)
        ax.add_artist(ab)

        #11pm image
        file = 'eleven.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.2)
        ab = AnnotationBbox(imagebox, (0.5,1), frameon = False)
        ax.add_artist(ab)

        #logo image
        file = 'logo.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.6)
        ab = AnnotationBbox(imagebox, (1.25,33.5), frameon = False)
        ax.add_artist(ab)

        #caption image
        file = 'caption.png'
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom = 0.3)
        ab = AnnotationBbox(imagebox, (4.1,33.3), frameon = False)
        ax.add_artist(ab)

        plt.savefig("result_image.jpg",bbox_inches='tight')

api.add_resource(Result,'/teams/<int:teamID>/results')

if __name__ == '__main__':
    app.run(debug=True)