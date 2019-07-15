import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pandas.read_csv('./file/Advertising.csv')

x = data['TV'].values.reshape(-1, 1)
y = data['sales'].values.reshape(-1, 1)
reg = LinearRegression()
reg.fit(x, y)

# print('k={}'.format(reg.coef_[0][0]))
# print('b={}'.format(reg.intercept_[0]))
#
# print('y = {0}x+{1}'.format(reg.coef_[0][0], reg.intercept_[0]))

predictions = reg.predict(X=x)
plt.figure(figsize=(16, 8))
plt.scatter(data['TV'], data['sales'], c='black')
plt.plot(data['TV'], predictions, c='blue', linewidth=2)
plt.xlabel('TV')
plt.ylabel('salse')
plt.show()

result = reg.predict([[300]])
print('300W是{}'.format(result[0][0]))
