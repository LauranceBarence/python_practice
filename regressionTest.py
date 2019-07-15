import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pandas.read_csv('./file/height.vs.temperature.csv')

x = data['height'].values.reshape(-1, 1)
y = data['temperature'].values.reshape(-1, 1)
reg = LinearRegression()
reg.fit(x, y)

print('k={}'.format(reg.coef_[0][0]))
print('b={}'.format(reg.intercept_[0]))

print('y = {0}x+{1}'.format(reg.coef_[0][0], reg.intercept_[0]))

predictions = reg.predict(X=x)
plt.figure(figsize=(16, 8))
plt.scatter(data['height'], data['temperature'], c='black')
plt.plot(data['height'], predictions, c='blue', linewidth=2)
plt.xlabel('height')
plt.ylabel('temperature')
plt.show()

result = reg.predict([[8000]])
print('8000米高度的预计温度是{:.5}℃'.format(result[0][0]))
