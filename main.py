#newfile
#importing modules
from pandas_profiling import ProfileReport
import pandas as pd
#linking df to our dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
report = ProfileReport(df)



