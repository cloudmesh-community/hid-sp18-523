import connexion
import six

from swagger_server.models.prediction import PREDICTION  # noqa: E501
from swagger_server import util

from subprocess import Popen, PIPE
from re import split
from sys import stdout
import subprocess
import numpy as np
import pandas as pd
#import seaborn as sns
 
from statsmodels.nonparametric.kde import KDEUnivariate
from statsmodels.nonparametric import smoothers_lowess
from pandas import Series, DataFrame
from patsy import dmatrices
from sklearn import datasets, svm
from sklearn import grid_search
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC,LinearSVC
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier,GradientBoostingClassifier

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from azureml import Workspace
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Imputer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import cross_validation,metrics
from flask import jsonify


def prediction_get():  # noqa: E501
    """process_get

    Returns process information of the hosting server # noqa: E501


    :rtype: PROCESS
    """

    #import matplotlib.pyplot as plt
    #get_ipython().magic(u'matplotlib inline')



    # # Read data from BigMart datasets for Train and Test

    # In[7]:





    train = pd.read_csv('./train.csv')
    test = pd.read_csv('./test.csv')


    train['source']='train'
    test['source']='test'
    data = pd.concat([train, test],ignore_index=True)


    train.head(10)

    test.head(10)
    print(train.describe())

    print(test.describe())

    print(data.describe())
    data.isnull().sum()

    data.apply(lambda x: len(x.unique()))

    categorical_attributes = [x for x in data.dtypes.index if data.dtypes[x]=='object']

    #Exclude ID cols and source:
    categorical_attributes = [x for x in categorical_attributes if x not in       ['Item_Identifier','Outlet_Identifier','source']]

    #for i in categorical_attributes:

    data["Item_Weight"]=data["Item_Weight"].fillna(data["Item_Weight"].mean())

    data['Outlet_Size']=data['Outlet_Size'].fillna(data['Outlet_Size'].mode().iloc[0])


    data['Item_Visibility'] = data['Item_Visibility'].mask(data['Item_Visibility'] == 0,data['Item_Visibility'].mean(skipna=True))

    data.head(10)


    data['Item_Identifier'].value_counts()
    data['Item_Type_Combined'] = data['Item_Identifier'].apply(lambda x: x[0:2])
    data['Item_Type_Combined'] = data['Item_Type_Combined'].map({'FD':'Food',
                                                             'NC':'Non-Consumable',
                                                             'DR':'Drinks'})
    data['Item_Type_Combined'].value_counts()


    data['Outlet_Years'] = 2018 - data['Outlet_Establishment_Year']
    data['Outlet_Years'].describe()

    data['Item_Fat_Content'] = data['Item_Fat_Content'].replace({'LF':'Low Fat',
                                                             'reg':'Regular',
                                                             'low fat':'Low Fat'})

    data.loc[data['Item_Type_Combined']=="Non-Consumable",'Item_Fat_Content'] = "Non-Edible"
    data['Item_Fat_Content'].value_counts()


    le = LabelEncoder()

    data['Outlet'] = le.fit_transform(data['Outlet_Identifier'])
    var_mod = ['Item_Fat_Content','Outlet_Location_Type','Outlet_Size','Item_Type_Combined','Outlet_Type','Outlet']
    le = LabelEncoder()
    for i in var_mod:
        data[i] = le.fit_transform(data[i])

    data = pd.get_dummies(data, columns=['Item_Fat_Content','Outlet_Location_Type','Outlet_Size','Outlet_Type',
                              'Item_Type_Combined','Outlet_Identifier'])

    name_of_attribs = list(data)
    data.apply(lambda x: len(x.unique()))



    class DataFrameSelector(BaseEstimator, TransformerMixin):
        def __init__(self, attribute_names):
            self.attribute_names = attribute_names
        def fit(self, X, y=None):
            return self
        def transform(self, X):
            return X[self.attribute_names].values

    num_attribs = data[['Item_Weight','Item_Visibility']]



    num_pipeline = Pipeline([
        ('selector', DataFrameSelector(num_attribs)),
        ('std_scaler', StandardScaler()),
    ])


    data.drop(['Item_Type','Outlet_Establishment_Year'],axis=1,inplace=True)


    data.head()

    trainr = data.loc[data['source']=="train"]
    testr = data.loc[data['source']=="test"]

    testr.drop(['Item_Outlet_Sales','source'],axis=1,inplace=True)
    trainr.drop(['source'],axis=1,inplace=True)



    # Create the train and test dataset
    Xtrain = trainr.drop(["Item_Outlet_Sales"], axis=1)
    ytrain = trainr["Item_Outlet_Sales"]



    X_train, X_test, y_train, y_test = train_test_split(Xtrain, ytrain)
    #print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


    # In[45]:


    # Create a dataset without Item_Identifier

    predictors = [x for x in Xtrain.columns if x not in ['Item_Identifier']]

    r_pipeline = Pipeline([
        ('std_scaler', StandardScaler()),
        ('linear', LinearRegression())
    ])

    r_pipeline.fit(X_train[predictors], y_train)
    preds = r_pipeline.predict(X_test[predictors])



    cv_score = cross_validation.cross_val_score(r_pipeline, X_train[predictors], y_train, cv=20, 
                                            scoring='mean_squared_error')
    cv_score = np.sqrt(np.abs(cv_score))
    RMSE = cv_score.mean()


    RMSEd = mean_squared_error(preds, y_test)
    RMSEsd=np.sqrt(RMSEd)



    pipedesc = Pipeline([('std_scaler', StandardScaler()),
                     ('grboostregmodel', GradientBoostingRegressor(n_estimators=100, learning_rate=0.1,
                                                                   max_depth=1, random_state=0, loss='ls'))])

    dscrmol = pipedesc.fit(X_train[predictors], y_train)
    #print(dscrmol.get_params())
    preddesctree = dscrmol.predict(X_test[predictors])


    cv_scoredesc = cross_validation.cross_val_score(pipedesc, X_train[predictors], y_train, cv=20, 
                                            scoring='mean_squared_error')
    cv_scoredesct = np.sqrt(np.abs(cv_scoredesc))
    RMSEdesc = cv_scoredesct.mean()


    gb_grid_params = {'learning_rate': [0.1, 0.05]
              #'max_depth': [4, 6, 8]
              #'min_samples_leaf': [20, 50,100,150],
              #'max_features': [1.0, 0.3, 0.1] 
              }

    gb_gs = GradientBoostingRegressor(n_estimators = 60)
    clfgrd = grid_search.GridSearchCV(gb_gs,
                               gb_grid_params,
                               cv=20, 
                               n_jobs=10)
    clfgrdmof=clfgrd.fit(X_train[predictors], y_train)


    clfpred = clfgrdmof.predict(X_test[predictors])


    cvgd_scoredesc = cross_validation.cross_val_score(clfgrd, X_train[predictors], y_train, cv=20, 
                                            scoring='mean_squared_error')
    cvgd_scoredesct = np.sqrt(np.abs(cvgd_scoredesc))
    RMSEdescgd = cvgd_scoredesct.mean()
    #print('RMSE is ', RMSEdescgd)


    results = pd.DataFrame(columns=["Description", "RMSE"])
    results.loc[len(results)] = ["LinearModel", RMSE]
    results.loc[len(results)] = ["GradientBoost", RMSEdesc]
    results.loc[len(results)] = ["HypertunedGradientBoost", RMSEdescgd]
    results

    bigmartpred = []
    overallprediction=clfgrdmof.predict(testr[predictors])
    bigmartpred.append(overallprediction.tolist())

    #print(overallprediction)

    #import pickle
    #filename = 'finalized_model.pkl'
    #pickle.dump(clfgrdmof, open(filename, 'wb'))

    #loaded_model = pickle.load(open(filename, 'rb'))
    #Test1 = loaded_model.predict(testr[predictors])
    return PREDICTION(bigmartpred)
