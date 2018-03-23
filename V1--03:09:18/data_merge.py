import glob
import pandas as pd

# get data file names
path =r'/Users/yishi/Desktop/Capstone Project/Raw_Data' 
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)

frame.to_csv('merged_data.csv')