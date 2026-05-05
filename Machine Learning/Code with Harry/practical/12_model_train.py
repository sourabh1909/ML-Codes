import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import root_mean_squared_error,accuracy_score
from sklearn.model_selection import cross_val_score

housing = pd.read_csv('housing.csv')


housing['income_cat'] = pd.cut(housing['median_income'],
                               bins=[0.0,1.5,3.0,4.5,6.0,np.inf],
                               labels = [1,2,3,4,5])

split = StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)


for train_index,test_index in split.split(housing,housing['income_cat']):
    strat_train_set = housing.loc[train_index].drop('income_cat',axis=1)
    strat_test_set = housing.loc[test_index].drop('income_cat',axis=1)


housing = strat_train_set.copy()


housing_label = housing['median_house_value'].copy()
housing = housing.drop('median_house_value',axis=1)

print(housing,housing_label)

num_attri = housing.drop('ocean_proximity',axis = 1).columns.tolist()
cat_attri = ['ocean_proximity']


num_pipeline = Pipeline([
    ('imputer',SimpleImputer(strategy='median')),
    ('scalar' ,StandardScaler())
])

cat_pipeline = Pipeline([
    ('onehot',OneHotEncoder(handle_unknown='ignore'))
])

# construct the full pipeline
full_pipeline = ColumnTransformer([
    ('num',num_pipeline,num_attri),
    ('cat',cat_pipeline,cat_attri)
])
# mhanje num_attri ahet tyamadhe num_pipeline lav
# mhanje cat_attri ahet tyamadhe cat_pipeline lav

# 7. transform the data
housing_prep = full_pipeline.fit_transform(housing)
print(housing_prep.shape)


# ---------------------------------------------------

# model banao
# linear reg
lin_reg = LinearRegression()
lin_reg.fit(housing_prep,housing_label)
# a linear regression lines fit on housing_prep
lin_pred = lin_reg.predict(housing_prep)
lin_rese = root_mean_squared_error(housing_label,lin_pred)

print(f"The root mean square error is for linear regression: {lin_rese}")

# desicion tree
des_reg = DecisionTreeRegressor()
des_reg.fit(housing_prep,housing_label)
# a linear regression lines fit on housing_prep
des_pred = des_reg.predict(housing_prep)
# des_rese = root_mean_squared_error(housing_label,des_pred)
tree_rese = cross_val_score(dec_reg,housing_prep,housing_label,scoring="")

print(f"The root mean square error is for decision tree: {des_rese}")

# random forest
ran_reg = RandomForestRegressor()
ran_reg.fit(housing_prep,housing_label)
# a linear regression lines fit on housing_prep
ran_pred = ran_reg.predict(housing_prep)
ran_rese = root_mean_squared_error(housing_label,ran_pred)

print(f"The root mean square error is for random forest: {ran_rese}")