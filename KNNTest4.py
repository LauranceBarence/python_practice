import pandas
import matplotlib
import matplotlib.pyplot as plt
import numpy
import seaborn
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

df = pandas.read_csv('./file/data.csv')
# print(df)

df_colors = df['Color'].str.get_dummies().add_prefix('Color: ')

df_type = df['Type'].apply(str).str.get_dummies().add_prefix('Type: ')

df = pandas.concat([df, df_colors, df_type], axis=1)

df = df.drop(['Brand', 'Type', 'Color'], axis=1)

# print(df)

# matrix = df.corr()
# f, ax = plt.subplots(figsize=(8, 6))
# seaborn.heatmap(matrix, square=True)
# plt.title('Car Price Variables')
# seaborn.pairplot(df[['Construction Year', 'Days Until MOT', 'Odometer', 'Ask Price']], height=2)
# plt.show()

X = df[['Construction Year', 'Days Until MOT', 'Odometer']]
y = df['Ask Price'].values.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=41)
X_normalizer = StandardScaler()
X_train = X_normalizer.fit_transform(X_train)
X_test = X_normalizer.transform(X_test)

y_nomalizer = StandardScaler()
y_train = y_nomalizer.fit_transform(y_train)
y_test = y_nomalizer.transform(y_test)

knn = KNeighborsRegressor(n_neighbors=2)
knn.fit(X_train, y_train.ravel())

y_pred = knn.predict(X_test)
y_pred_inv = y_nomalizer.inverse_transform(y_pred)
y_test_inv = y_nomalizer.inverse_transform(y_test)

plt.scatter(y_pred_inv, y_test_inv)
plt.xlabel('Prediction')
plt.ylabel('Real Value')

diagonal = numpy.linspace(500, 1500, 100)
plt.plot(diagonal, diagonal, '-r')
plt.xlabel('Predicted ask Price')
plt.ylabel('Ask Price')
plt.show()
