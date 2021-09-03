

import pandas as pd
import numpy as np


users=pd.read_table("D:\\movies-project\\users.dat",engine='python',sep='::')
ratings=pd.read_table("D:\\movies-project\\ratings.dat",engine='python',sep='::')
movies=pd.read_csv("D:\\movies-project\\movies.dat",sep='::', engine='python')






users.head() 

ratings.head()

movies.head()  
users1=pd.DataFrame(data=users,columns=['UserID','Gender','Age','Occupation','Zip-code'])
users1





d={'col1':[1,2,3,4] ,'col2':['a','s','c','d']}
df=pd.DataFrame(data=d)
df











