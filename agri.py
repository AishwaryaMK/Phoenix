import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
names = ['Location','Crop','Year','Season','Area','Production','Yield','Crop']
agri = sns.load_dataset("agriculture_dataset")
agri.head()
x = np.array(agri.iloc[:,0:20])
y = np.array(agri['class'])
x_train, x_test, y_train, t_test = train_test_split(x,y,test_size = 0.33, random_state = 42)
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(x_train,y_train)
pred = knn.predict(x_test)
print(pred)
print(accuracy_score(y_test, pred))
