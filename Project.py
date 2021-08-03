#%%

# !pip install numpy
# !pip install pandas
# !pip install matplotlib
# !pip install scikit-learn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import sklearn

##%% md
#
#Q1: Import “Cars prices” .csv file into your notebook and read it by Pandas python library.
#
##%%

data = pd.read_csv('CarPrice_Assignment.csv')

##%% md
#
#Q2: Drop rows with NaN entries.
#
##%%

data.dropna(inplace=True)

##%% md
#
#Q3: Is this supervised or unsupervised learning? Why? PDF
#
##%%

##%% md
#
#Q4: Plot whole features with Pandas.DataFrame.plot function.
#
##%%

data.plot(x='car_ID')

##%% md
#
#Q5: Write a short description about dataset distribution. PDF
#
##%%

# data.drop(columns=['car_ID']).plot(x='price')
# data.describe()
data.std()/data.mean()

##%% md
#
#Q6: Sperate engine size and price features in a new Dataframe.
#
##%%

engine_price = data[['enginesize', 'price']]
engine_price.describe()

##%% md
#
#Q7: Calculate linear regression between engine size and price features with Gradient descent method. ( Use SKlearn library )
#
##%%

from sklearn import model_selection

y = np.array(engine_price['price'])
X = np.array([engine_price['enginesize']]).T

X_train, X_test, y_train, y_test = model_selection.train_test_split(
	X, y,
	train_size=0.8,
	test_size=0.2,
	random_state=101
)

#%%

# from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# reg = LinearRegression()
reg_inner = SGDRegressor(max_iter=1000, tol=1e-3)
reg = make_pipeline(StandardScaler(), reg_inner)

reg.fit(X_train, y_train)

print("parameters:", reg_inner.coef_)
print("score on train:", reg.score(X_train, y_train))

##%% md
#
#Q8: After creating your model, test it with 20% of data.
#
##%%

print("score on test:", reg.score(X_test, y_test))

y_test_predict = reg.predict(X_test)

plt.plot(X_test, y_test, 'b^')  # red is actual data
plt.plot(X_test, y_test_predict, 'g')  # red is actual data

##%% md
#
#Q9: Plot engine size and price features with regression line (Scatter plot).
#
##%%

plt.plot(X, y, 'r.')  # red is actual data

line_x = np.array([[X.min()], [X.max()]])
line_y = reg.predict(line_x)
plt.plot(line_x, line_y, 'g')  # green is line on regression coefs

##%% md
#
#Q10: How much is this model accurate ( Use SKlearn library )
#
##%%

score = reg.score(X, y)
print(f"score on all: {score * 100}%")


##%% md
#
#Q11: Write a sample function that get engine size and returns predicted price of car.
#
##%%

def query_price(engine_size):
	return int(reg.predict([[engine_size]])[0])


print("EngSize=50 : ", query_price(50))
print("EngSize=100 : ", query_price(100))
print("EngSize=150 : ", query_price(150))
print("EngSize=200 : ", query_price(200))
print("EngSize=250 : ", query_price(250))
print("EngSize=300 : ", query_price(300))
print("EngSize=350 : ", query_price(350))

#%%


 
