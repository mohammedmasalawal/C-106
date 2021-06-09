import csv
import numpy as np

def getDataSource(data_path):
    size_of_tv=[]
    time_spent=[]
    with open (data_path) as csv_file:
        csv_reader=csv.DictReader (csv_file)
      
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            time_spent.append(float(row["Average time spent watching TV in a week (hours)"]))
    
    return {"x":size_of_tv,"y":time_spent}
def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between the size of TV and time spent:\n",correlation[0,1])
def setUp ():
    data_path="size_of_tv_vs_watching_tv.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
setUp()