#newfile
#importing modules
import pandas as pd
#linking df to our dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.describe(include='all')




