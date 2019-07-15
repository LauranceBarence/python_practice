import numpy
import pandas
import matplotlib.pyplot as plt
from datetime import datetime
# from plotly import tools
# from plotly.graph_objs import *
# from plotly.offline import init_notebook_mode, iplot, iplot_mpl
# init_notebook_mode()
# import  plotly.plotly as py
# import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing

# 读取数据
df = pandas.read_csv('./file/000001.csv')
# print(numpy.shape(df))
# print(df.head())
# 复写日期列并根据日期升序排序
df['date'] = pandas.to_datetime(df['date'])
df = df.set_index('date')
df.sort_values(by=['date'], inplace=True, ascending=True)
# print(df.tail())
# 检查是否有缺失的值
df.dropna(axis=0, inplace=True)
# print(df.isna().sum())

min_date = df.index.min()
max_date = df.index.max()

# plotly绘制k线图
# trace = go.Ohlc(x=df.index, open=df['open'], high=df['high'], low=df['low'], close=df['close'])
# data = [trace]
# iplot(data, filename='simple_ohlc')

# 线性回归
num = 5
df['label'] = df['close'].shift(-num)
# print(df.shape)

data = df.drop(['label', 'price_change', 'p_change'], axis=1)
# print(data.tail())
X = data.values
X = preprocessing.scale(X)
X = X[:-num]

df.dropna(inplace=True)
target = df.label
y = target.values

# print(numpy.shape(X), numpy.shape(y))

X_train, y_train = X[0:550, :], y[0:550]
X_test, y_test = X[550:, -51:], y[550:]
# print(X_train.shape)
# print(y_train.shape)
# print(X_test.shape)
# print(y_test.shape)

lr = LinearRegression()
lr.fit(X_train, y_train)
# print(lr.score(X_test, y_test))

trange = pandas.date_range('2019-05-13', periods=num, freq='d')
# print(trange)

X_predict = X[-num:]
forecast = lr.predict(X_predict)

predict_df = pandas.DataFrame(forecast, index=trange)
predict_df.columns = ['forecast']
# print(predict_df)

df = pandas.read_csv('./file/000001.csv')
df['date'] = pandas.to_datetime(df['date'])
df = df.set_index('date')

df.sort_values(by=['date'], inplace=True, ascending=True)
df_concat = pandas.concat([df, predict_df], axis=1)
df_concat = df_concat[df_concat.index.isin(predict_df.index)]
# print(df_concat.tail(num))

df_concat['close'].plot(color='green', linewidth=1)
df_concat['forecast'].plot(color='orange', linewidth=3)
plt.xlabel('Time')
plt.ylabel('Price')
plt.show()
