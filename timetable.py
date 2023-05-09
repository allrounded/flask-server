import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Mon":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Tue":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    "Wed":[0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
    "Thu":[1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
    "Fri":[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
    "Sat":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "Sun":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
}

df = pd.DataFrame(data)

timeSegment = ["9:00",
               "9:30",
               "10:00",
               "10:30",
               "11:00",
               "11:30",
               "12:00",
               "12:30",
               "13:00",
               "13:30",
               "14:00",
               "14:30",
               "15:00",
               "15:30",
               "16:00",
               "16:30",
               "17:00",
               "17:30",
               "18:00",
               "18:30",
               "19:00",
               "19:30",
               "20:00",
               "20:30",
               "21:00",
               "21:30",
               "22:00",
               "22:30",
               "23:00",
               "23:30"]

fig, ax = plt.subplots(figsize=(7,10))
plt.subplots_adjust(left=0.25)
plt.rcParams['text.color']='black'

timetable = plt.table(cellText=df.values,
                      cellLoc='center',
                      colLabels=list(data.keys()),
                      rowLabels=timeSegment[0:len(df.values)],
                      rowLoc='center',
                      loc='center',
                      bbox=(0,0,1,1))
ax.axis(xmax=1.4, ymax=31)
ax.axis('off')

#data cells
for i in range(1,len(df.values)+1):
    for j in range(0,len(data.keys())):
        cell = timetable[i,j]
        cell.set_height(0.1)
        cell.get_text().set_visible(False)
        cell_value = cell.get_text().get_text()
        cell.set_edgecolor('black')
        if cell_value == "0":
            cell.set_facecolor('orange')
        elif cell_value == "1":
            cell.set_facecolor('white')

#col headers
for i in range(0, len(data.keys())):
        cell = timetable[0,i]
        cell.set_height(0.1)
        cell.set_edgecolor('black')
        cell.visible_edges = 'vertical'
        
#row headers
for j in range(1, len(df.values)+1):
    cell = timetable[j,-1]
    cell.set_height(0.1)
    cell.set_edgecolor('black')
    cell.visible_edges = 'horizontal'


plt.savefig("test_table.jpg",bbox_inches='tight')
plt.show()
