from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
import warnings 
warnings.filterwarnings('ignore')
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
print(df.head())
from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
df['BusinessTravel'] = LE.fit_transform(df['BusinessTravel'])
df['Department'] = LE.fit_transform(df['Department'])
df['Gender'] = LE.fit_transform(df['Gender'])
df['JobRole'] = LE.fit_transform(df['JobRole'])
df['MaritalStatus'] = LE.fit_transform(df['MaritalStatus'])
df['Over18'] = LE.fit_transform(df['Over18'])
df['OverTime'] = LE.fit_transform(df['OverTime'])
df['Attrition'] = LE.fit_transform(df['Attrition'])
df['EducationField'] = LE.fit_transform(df['EducationField'])
y = df['Attrition']
print(y.head())
x = df.drop(columns=['Over18', 'Attrition', 'EmployeeCount', 'EmployeeNumber',
                     'YearsAtCompany', 'JobLevel', 'PerformanceRating', 
                     'YearsWithCurrManager', 'StandardHours', 'MonthlyRate/Income'
                    ], axis='columns')
print(x.head())
xt, xtt, yt, ytt = train_test_split(x, y, test_size=0.2, random_state=69)
model=RandomForestClassifier(criterion='gini', max_depth=10, max_leaf_nodes=9,
                            min_impurity_decrease=0.0, n_estimators=5)
model.fit(xt, yt)
from sklearn.model_selection import cross_val_score
results = cross_val_score(model, x, y)
print(results)
import pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)