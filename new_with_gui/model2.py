import pandas as pd
from sklearn.preprocessing import StandardScaler,Normalizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

df=pd.read_csv("final.csv")

x=df.iloc[:,0:16]

obj=StandardScaler()
x1=obj.fit_transform(x)
# obj=Normalizer()
# x1=obj.fit_transform(x)


y=df['Name']

sv=LinearSVC()
sv.fit(x,y)

Xnew = pd.read_csv("points_test1.csv")

ynew = sv.predict(Xnew)

import numpy
from collections import Counter

array = numpy.array(ynew)
result = Counter(array.flat).most_common(1)

print(result)

