import pandas
import numpy
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn
from imblearn.over_sampling import SMOTE
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import accuracy_score

plt.rc('font', size=14)
seaborn.set(style='white')
seaborn.set(style='whitegrid', color_codes=True)

# 读取数据
data = pandas.read_csv('./file/banking.csv')
data = data.dropna()
# print(data.shape)
# print(list(data.columns))

# hk型
data['education'] = numpy.where(data['education'] == 'basic.9y', 'Basic', data['education'])
data['education'] = numpy.where(data['education'] == 'basic.6y', 'Basic', data['education'])
data['education'] = numpy.where(data['education'] == 'basic.4y', 'Basic', data['education'])
# print(data['education'].unique())
# print(data['y'].value_counts())
seaborn.countplot(x='y', data=data, palette='hls')
# plt.show()
# plt.savefig('count_plot')

count_no_sub = len(data[data['y'] == 0])
count_sub = len(data[data['y'] == 1])
pct_of_no_sub = count_no_sub / (count_no_sub + count_sub)
# print('未开户的百分比：%.2f%%' % (pct_of_no_sub * 100))
pct_of_sub = count_sub / (count_sub + count_no_sub)
# print('开户的百分比：%.2f%%' % (pct_of_sub * 100))

# 根据开户情况求均值
# print(data.groupby('y').mean())

cat_vars = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome']
for var in cat_vars:
    cat_list = pandas.get_dummies(data[var], prefix=var)
    data = data.join(cat_list)

data_final = data.drop(cat_vars, axis=1)
# print(data_final.columns.values)

# 对数据进行过采样
X = data_final.loc[:, data_final.columns != 'y']
y = data_final.loc[:, data_final.columns == 'y'].values.ravel()
os = SMOTE(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
columns = X_train.columns
os_data_X, os_data_y = os.fit_sample(X_train, y_train)
os_data_X = pandas.DataFrame(data=os_data_X, columns=columns)
os_data_y = pandas.DataFrame(data=os_data_y, columns=['y'])
# print("过采样以后的数据量: ", len(os_data_X))
# print("未开户的用户数量: ", len(os_data_y[os_data_y['y'] == 0]))
# print("开户的用户数量: ", len(os_data_y[os_data_y['y'] == 1]))
# print("未开户的用户数量的百分比: ", len(os_data_y[os_data_y['y'] == 0]) / len(os_data_X))
# print("开户的用户数量的百分比: ", len(os_data_y[os_data_y['y'] == 1]) / len(os_data_X))
# 训练模型
logreg = LogisticRegression()
logreg.fit(os_data_X, os_data_y.values.reshape(-1))
y_pred = logreg.predict(X_test)
# print('在测试数据集上面的预测准确率: {:.2f}'.format(logreg.score(X_test, y_test)))
print(y_pred)
# print("准确率为 %2.3f" % accuracy_score(y_test, y_pred))
# print(classification_report(y_test, y_pred))
logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
# fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:, 1])
# plt.figure()
# plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
# plt.plot([0, 1], [0, 1], 'r--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver operating characteristic')
# plt.legend(loc='lower right')
# plt.savefig('Log_ROC')
# plt.show()
