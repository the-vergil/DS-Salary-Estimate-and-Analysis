import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pickle

df = pd.read_csv("data/clean_eda_salary_data.csv")

df.columns

#select columns
df_model = df[['Rating', 'Location', 'Size', 'Type of ownership', 'Sector', 'Revenue', 'Employer Provided Salary', 'Salary Per Hour', 
               'age', 'mathematics', 'python', ' r ', 'machine learning', 'aws', 'cloud','excel', 'Senior/Junior', 'Role', 
               'No of competitors', 'Loc==HQ', 'mean salary']]

df_model.rename(columns = {" r ": "R", 'mean salary': 'Avg Salary'}, inplace = True)

#dummy creation
df_dummies = pd.get_dummies(df_model)

#train-test-split
X = df_dummies.drop('Avg Salary', axis=1)
y = df_dummies['Avg Salary'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#model
x_train = sm.add_constant(X_train)
ols_model = sm.OLS(y_train, x_train)
results = ols_model.fit()
results.summary()

#linear regression model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
cross_val_score(lr_model, X_train, y_train, scoring='neg_mean_absolute_error', cv=5)

#lasso 
l_model = Lasso()
l_model.fit(X_train, y_train)
cross_val_score(l_model, X_train, y_train, scoring='neg_mean_absolute_error', cv=5)

alpha = []
error = []
for i in range(1,100) :
    alp = i/100
    alpha.append(alp)
    lml = Lasso(alpha=alp)
    error.append(np.mean(cross_val_score(lml, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))
    
plt.plot(alpha, error)

err = tuple(zip(alpha, error))
err_df = pd.DataFrame(err, columns=['alpha', 'error'])
err_df[err_df.error == max(err_df.error)]

#random forest regressor
rf_model = RandomForestRegressor()
np.mean(cross_val_score(rf_model, X_train, y_train, scoring='neg_mean_absolute_error', cv=3))

#grid search cv
parameters = {'n_estimators' : range(1,150, 10), 'criterion' : ('mae', 'mse'), 'max_features' : ('sqrt', 'log2')}
clf = GridSearchCV(rf_model, parameters)
clf.fit(X_train, y_train)

clf.best_estimator_
clf.best_score_

#score
y_pred = clf.predict(X_test)

mean_absolute_error(y_test, y_pred)
clf.score(X_test, y_test)

#save model
file = open('RFregressor', 'wb')
pickle.dump(clf, file)
file.close()