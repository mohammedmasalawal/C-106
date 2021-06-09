import csv
import numpy as np

def getDataSource(data_path):
    marks=[]
    days_present=[]
    with open (data_path) as csv_file:
        csv_reader=csv.DictReader (csv_file)
      
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    
    return {"x":marks,"y":days_present}
def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between the marks and time days present:\n",correlation[0,1])
def setUp ():
    data_path="students_marks_attendance.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
setUp()