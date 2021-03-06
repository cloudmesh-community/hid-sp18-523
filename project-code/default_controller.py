import connexion
import six
import os

from swagger_server.models.prediction import Prediction  
from swagger_server.models import ItemSale 
from swagger_server.models import ItemOutletSale
from swagger_server.models import ItemDetail
from swagger_server.models import DataTrain
from swagger_server.models import DataTest
from swagger_server.models import Item 
from swagger_server import util

from subprocess import Popen, PIPE
from re import split
from sys import stdout
import subprocess
import numpy as np
import pandas as pd
 
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
from flask import request, Flask
from html import HTML


def prediction_get():  
    """process_get

    Returns process information of the hosting server # noqa: E501


    :rtype: PROCESS
    """

    train = pd.read_csv('./train.csv')
    test = pd.read_csv('./test.csv')


    train['source']='train'
    test['source']='test'
    data = pd.concat([train, test],ignore_index=True)

    data.isnull().sum()

    data.apply(lambda x: len(x.unique()))

    categorical_attributes = [x for x in data.dtypes.index if data.dtypes[x]=='object']

    #Exclude ID cols and source:
    categorical_attributes = [x for x in categorical_attributes if x not in       ['Item_Identifier','Outlet_Identifier','source']]

    #for i in categorical_attributes:

    data["Item_Weight"]=data["Item_Weight"].fillna(data["Item_Weight"].mean())

    data['Outlet_Size']=data['Outlet_Size'].fillna(data['Outlet_Size'].mode().iloc[0])


    data['Item_Visibility'] = data['Item_Visibility'].mask(data['Item_Visibility'] == 0,data['Item_Visibility'].mean(skipna=True))




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



    trainr = data.loc[data['source']=="train"]
    testr = data.loc[data['source']=="test"]

    testr.drop(['Item_Outlet_Sales','source'],axis=1,inplace=True)
    trainr.drop(['source'],axis=1,inplace=True)



    # Create the train and test dataset
    Xtrain = trainr.drop(["Item_Outlet_Sales"], axis=1)
    ytrain = trainr["Item_Outlet_Sales"]



    X_train, X_test, y_train, y_test = train_test_split(Xtrain, ytrain)


    # Create a dataset without Item_Identifier

    predictors = [x for x in Xtrain.columns if x not in ['Item_Identifier']]

    r_pipeline = Pipeline([
        ('std_scaler', StandardScaler()),
        ('linear', LinearRegression())
    ])

    lm=r_pipeline.fit(X_train[predictors], y_train)
    preds = r_pipeline.predict(X_test[predictors])


    bigmartpred = []
    overallprediction=lm.predict(testr[predictors])
    bigmartpred.append(overallprediction.tolist())


    return Prediction(bigmartpred)


def item_getitemsales(Item_Id):
    d = pd.read_csv('./train.csv')
    #t = pd.DataFrame()
    t= []

    df = d.set_index("Item_Identifier", drop = False)
    
    #t.append((df.loc[Item_Id,["Item_Outlet_Sales","Outlet_Identifier"]]).to_html(index=False))

    #t.append((df.loc[Item_Id,["Item_Outlet_Sales","Outlet_Identifier"]]).to_dict(orient='list'))
    t.append((df.loc[Item_Id,["Item_Outlet_Sales","Outlet_Identifier"]]).to_dict())
    
    return ItemSale(t)

app = Flask(__name__)

@app.route('/item')
def item_getitemdetails():
    d = pd.read_csv('./train.csv')
    t = []
    item_id = request.args.get('item_id', None)
    outlet_id = request.args.get('outlet_id', None)

    df = d.set_index(["Item_Identifier","Outlet_Identifier"], drop = False)
    
    t.append((df.loc[(df["Item_Identifier"]==item_id) & (df["Outlet_Identifier"]==outlet_id),]).to_json())
    
    return ItemDetail(t)

def sale_getitemoutletsales():
    d = pd.read_csv('./train.csv')
    t = []
    item_id = request.args.get('item_id', None)
    outlet_code = request.args.get('outlet_code', None)

    df = d.set_index(["Item_Identifier","Outlet_Identifier"], drop = False)
    
    t.append((df.loc[(df["Item_Identifier"]==item_id) & (df["Outlet_Identifier"]==outlet_code),"Item_Outlet_Sales"]).tolist())
    
    return ItemOutletSale(t)

def train_uploadtrainfile():
    t = []
  
    #item_id = request.args.get('upfile', None)
    
    try:
     if request.method == 'POST':
      f = request.files['uptrainfile']
      f.save(os.path.join('.','train.csv'))
      t.append("successfull!!")
      return DataTrain(t)
    except:
     t.append("error occured!!")
     return DataTrain(t)

def test_uploadtestfile():
    t = []
    
    #item_id = request.args.get('upfile', None)

    try:
     if request.method == 'POST':
      f = request.files['uptestfile']
      f.save(os.path.join('.','test.csv'))
      #x1 = 1 / 0
      t.append("successful!!")
      return DataTest(t)
    except:
     t.append("error occured!!")
     return DataTest(t)

def item_additem():
    t = []
    t.append("successful!!")
    #item_id = request.args.get('upfile', None)

    Item_Identifier = request.args.get('Item_Identifier', None)
    Item_Weight = request.args.get('Item_Weight', None)
    Item_Fat_Content = request.args.get('Item_Fat_Content', None)
    Item_Visibility = request.args.get('Item_Visibility', None)
    Item_Type = request.args.get('Item_Type', None)
    Item_MRP = request.args.get('Item_MRP', None)
    Outlet_Identifier = request.args.get('Outlet_Identifier', None)
    Outlet_Establishment_Year = request.args.get('Outlet_Establishment_Year', None)
    Outlet_Size = request.args.get('Outlet_Size', None)
    Outlet_Location_Type = request.args.get('Outlet_Location_Type', None)
    Outlet_Type = request.args.get('Outlet_Type', None)
    Item_Outlet_Sales = request.args.get('Item_Outlet_Sales', None)
    
    df = pd.DataFrame()
    df = df.append({'Item_Identifier':Item_Identifier,'Item_Weight':Item_Weight,'Item_Fat_Content':Item_Fat_Content,'Item_Visibility': Item_Visibility,'Item_Type':Item_Type,'Item_MRP': Item_MRP,'Outlet_Identifier': Outlet_Identifier,'Outlet_Establishment_Year': Outlet_Establishment_Year,'Outlet_Size': Outlet_Size,'Outlet_Location_Type': Outlet_Location_Type,'Outlet_Type': Outlet_Type,'Item_Outlet_Sales': Item_Outlet_Sales}, ignore_index=True)
    sequence =['Item_Identifier','Item_Weight','Item_Fat_Content','Item_Visibility','Item_Type','Item_MRP','Outlet_Identifier','Outlet_Establishment_Year','Outlet_Size','Outlet_Location_Type','Outlet_Type','Item_Outlet_Sales']
    df=df.reindex(columns=sequence)
    #df.to_csv('train.csv',mode='a',header=False, index=False)
    outfile = open('train.csv',mode='a')
    df.astype(str).to_csv(outfile,header=False, index=False)
    outfile.close()
    
    return Item(t)

