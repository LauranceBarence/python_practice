import numpy
import pandas
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

plt.rc('font', size=14)
seaborn.set(style='white')
seaborn.set(style='whitegrid', color_codes=True)

# 读取数据
df = pandas.read_csv('./file/titanic_data.csv')
# print(df.head())
# print(df.shape)
# 查看缺失数据
# print(df.isnull().sum())
# print('"age" 缺失的百分比  %.2f%%' %((df['age'].isnull().sum()/df.shape[0])*100))
# 显示年龄分布直方图
# ax = df["age"].hist(bins=15, color='teal', alpha=0.6)
# ax.set(xlabel='age')
# plt.xlim(-10, 85)
# plt.show()
# print('按照登船地点分组 (C = Cherbourg, Q = Queenstown, S = Southampton):')
# print(df['embarked'].value_counts())
# 分组数据直方图
# seaborn.countplot(x='embarked', data=df, palette='Set2')
# plt.show()
# 填补部分缺失数据
data = df.copy()
data["age"].fillna(df["age"].median(skipna=True), inplace=True)
data["embarked"].fillna(df['embarked'].value_counts().idxmax(), inplace=True)
data.drop('cabin', axis=1, inplace=True)
# print(data.isnull().sum())
# print('"sex" 缺失的百分比  %.2f%%' %((df['sex'].isnull().sum()/df.shape[0])*100))
# print(df['parch'].value_counts())
# print(df["age"].median(skipna=True))
# print('"fare" 缺失的百分比  %.2f%%' %((df['fare'].isnull().sum()/df.shape[0])*100))
data["sex"].fillna(df['sex'].value_counts().idxmax(), inplace=True)
data["ticket"].fillna(df["ticket"].value_counts().idxmax(), inplace=True)
data["survived"].fillna(df["survived"].value_counts().idxmax(), inplace=True)
# data.drop('name', axis=1, inplace=True)
data["fare"].fillna(df["fare"].median(skipna=True), inplace=True)
data["pclass"].fillna(df["pclass"].value_counts().idxmax(), inplace=True)
data["sibsp"].fillna(df["sibsp"].value_counts().idxmax(), inplace=True)
data["parch"].fillna(df["parch"].value_counts().idxmax(), inplace=True)
data['TravelAlone'] = numpy.where((data["sibsp"] + data["parch"]) > 0, 0, 1)
data.drop('sibsp', axis=1, inplace=True)
data.drop('parch', axis=1, inplace=True)
final = pandas.get_dummies(data, columns=["embarked", "sex"])
final.drop('name', axis=1, inplace=True)
final.drop('ticket', axis=1, inplace=True)

# 使用如下特征做预测
cols = ["age", "fare", "TravelAlone", "pclass", "embarked_C", "embarked_S", "sex_male"]

# 创建 X (特征) 和 y (类别标签)
X = final[cols]
y = final['survived']

# 将 X 和 y 分为两个部分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# print(y_test)
# 检测 logistic regression 模型的性能
# 1.训练模型,
logreg = LogisticRegression()
# X_train = pd.DataFrame(data=X_train, columns=cols)
# y_train = pd.DataFrame(data=y_train, columns=['survived'])
logreg.fit(X_train, y_train)
# 2.根据模型, 以 X_test 为输入, 生成变量 y_pred
y_pred = logreg.predict(X_test)
print('Train/Test split results:')
print("准确率为 %2.3f" % accuracy_score(y_test, y_pred))
