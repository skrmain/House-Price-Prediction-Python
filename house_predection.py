
import numpy
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv('kc_house_data.csv')


labels = data['price']
conv_dates = [1 if values == 2014 else 0 for values in data.date ]
data['date'] = conv_dates
train1 = data.drop(['id', 'price'],axis=1)


from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(train1 , labels , test_size = 0.10,random_state =2)

model = LinearRegression().fit(x_tr ain,y_train)


import pickle

with open("house_prediction.model", "wb") as f:
    pickle.dump(model, f)


with open("house_prediction.model", "rb") as f:
    mp = pickle.load(f)


model.score(x_test,y_test)

from sklearn import ensemble
clf = ensemble.GradientBoostingRegressor(n_estimators = 400, max_depth = 5, min_samples_split = 2,
          learning_rate = 0.1, loss = 'ls')


clf.fit(x_train, y_train)
clf.score(x_test,y_test)




# Date, Bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_above, sqft_basement, yr_built, yr_renovated, zipcode, lat, long, sqft_livings15, sqft_lot15
x_new = np.array([2014, 2, 2, 1500, 2, 0, 0, 5, 5, 10, 2000, 500, 2000, 0, 98008, 47.6, -122.99, 3000, 1400]).reshape(1, -1)
y_new = model.predict(x_new)



# Bedrooms
# Bathrooms
# Living Area
# lot - ?
# Condition - 1
# Year Built
# 