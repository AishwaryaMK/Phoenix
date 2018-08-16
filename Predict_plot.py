import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns
import statsmodels.api as sm
from sklearn import linear_model
agri = sns.load_dataset("agriculture_dataset")
agri.head()
sns.pairplot(agri, hue="Location")
plt.show()
sns.pairplot(agri, hue="Crops")
plt.show()
sns.lmplot(x="Production", y="Yield", data=agri)
plt.show()
X = agri[["Production"]]
y = agri["Yield"]
model = linear_model.LinearRegression()
results = model.fit(X, y)
print (results.intercept_, results.coef_)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())
