import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder

# 1. load dataset
housing = pd.read_csv('housing.csv')

# 2. create a stratified test set
housing['income_cat'] = pd.cut(housing['median_income'],
                               bins=[0.0,1.5,3.0,4.5,6.0,np.inf],
                               labels = [1,2,3,4,5])

split = StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)


for train_index,test_index in split.split(housing,housing['income_cat']):
    strat_train_set = housing.loc[train_index].drop('income_cat',axis=1)
    strat_test_set = housing.loc[test_index].drop('income_cat',axis=1)
    
# 3. we are working on copy of data

housing = strat_train_set.copy()

# 4. Separate feature and labels
housing_label = housing['median_house_value'].copy()
housing = housing.drop('median_house_value',axis=1)

print(housing,housing_label)

# 5. seprate numerical and categorical values
num_attri = housing.drop('ocean_proximity',axis = 1).columns.tolist()
cat_attri = ['ocean_proximity']

# for numerical
num_pipeline = Pipeline([
    ('imputer',SimpleImputer(strategy='median')),
    ('scalar' ,StandardScaler())
])

# for categori cal
# gives 0 & 1 for string data
cat_pipeline = Pipeline([
    ('onehot',OneHotEncoder(handle_unknown='ignore'))
])

# 6.construct the full pipeline
full_pipeline = ColumnTransformer([
    ('num',num_pipeline,num_attri),
    ('cat',cat_pipeline,cat_attri)
])
# mhanje num_attri ahet tyamadhe num_pipeline lav
# mhanje cat_attri ahet tyamadhe cat_pipeline lav

# 7. transform the data
housing_prep = full_pipeline.fit_transform(housing)
print(housing_prep.shape)