# importing packages
import pandas as pd
from ydata_profiling import ProfileReport

#linking df to our dataset
df = pd.read_csv("D:/Automation/AnalyticToolPython-2/test.csv")
report = ProfileReport(df)
report.to_notebook_iframe()
report.to_file('file_name')
report.to_html()
