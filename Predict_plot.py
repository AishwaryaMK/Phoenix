#Step 1:
#import pakckages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns
import statsmodels.api as sm
from sklearn import linear_model
#Step 2:
#Read the dataset
agri = sns.load_dataset("agriculture_dataset")
agri.head()
#Step 3:
#Plot
sns.pairplot(agri, hue="Location")
plt.show()
#Plot
sns.pairplot(agri, hue="crop")
plt.show()
#Step 4
#Plot 2 variables
sns.lmplot(x="Production", y="Yield", data=agri)
plt.show()
#Step 5
X = agri[["Production"]]
y = agri["Yield"]
model = linear_model.LinearRegression()
results = model.fit(X, y)
print (results.intercept_, results.coef_)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())
