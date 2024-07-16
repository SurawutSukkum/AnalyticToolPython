# importing packages
import pandas as pd
from ydata_profiling import ProfileReport

#linking df to our dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
report = ProfileReport(df)
report.to_notebook_iframe()
