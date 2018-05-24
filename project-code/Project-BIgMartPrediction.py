
# coding: utf-8

# # Load all the Libraries

# ### Loading all the Libraries for executing the below Python code and functions# 

# In[61]:


# Import Libraries
import matplotlib.pyplot as plt
#get_ipython().magic(u'matplotlib inline')
import numpy as np
import pandas as pd
import seaborn as sns
 
from statsmodels.nonparametric.kde import KDEUnivariate
from statsmodels.nonparametric import smoothers_lowess
from pandas import Series, DataFrame
from patsy import dmatrices
from sklearn import datasets, svm
from sklearn import grid_search
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier, GradientBoostingClassifier

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV


# # Read data from BigMart datasets for Train and Test

# In[7]:


from azureml import Workspace

#ws = Workspace()
#ds = ws.datasets['train.csv']
#train = ds.to_dataframe()

#ds1 = ws.datasets['test.csv']
#test = ds1.to_dataframe()

train = pd.read_csv('train.csv')

test = pd.read_csv('test.csv')

# # Dimension of dataset and combine the Test and Train data

# ### Summary of the overall dataset - The data set has total of 14204 rows with 13 attributes. 
# ### Train has 8523 and 5681 in test dataset

# In[8]:


train['source']='train'
test['source']='test'
data = pd.concat([train, test],ignore_index=True)
print (train.shape, test.shape, data.shape)


# # First Ten Records of Train

# In[9]:


train.head(10)


# # First 10 Records for Test Set

# In[10]:


test.head(10)


# In[11]:


#Describe the Train data
print(train.describe())


# In[12]:


#Describe the Test data
print(test.describe())


# # Describe the Combinded data set

# In[13]:


#Describe the Full data (Train + Test)
print(data.describe())


# # Data Exploration and Visualization

# In[14]:


# We can see the columns with Null instances
data.isnull().sum()


# In[15]:


# Unique values with in Attributes -
data.apply(lambda x: len(x.unique()))


# # Explore the Categorical Attributes from Combined dataset

# In[16]:


#Filter categorical variables
categorical_attributes = [x for x in data.dtypes.index if data.dtypes[x]=='object']

#Exclude ID cols and source:
categorical_attributes = [x for x in categorical_attributes if x not in ['Item_Identifier','Outlet_Identifier','source']]

#Print frequency of categories
for i in categorical_attributes:
    print ('\nFrequency of Categories for attributes %s'%i)
    print (data[i].value_counts())


# In[17]:


# Distribution of Weight Attributes
data.Item_Weight.plot(kind='hist', color='blue', edgecolor='black', figsize=(10,6), 
                      title='Histogram of Item_Weight')


# In[18]:


#Check the mean sales by type:
#data.pivot_table(values='Item_Outlet_Sales',index='Outlet_Type')


# In[19]:


# Distrubtion of Target Variable - Item_Outlet_Sales
#import pylab 
#import scipy.stats as stats
#stats.probplot(data.Item_Outlet_Sales, dist="uniform", plot=pylab)
#pylab.show()


# # Plotting the histogram on Combined dataset

# In[20]:


#get_ipython().magic(u'matplotlib inline')
#import matplotlib.pyplot as plt
#data.hist(bins=50, figsize=(20,15))
#plt.show()


# # Correlation Plot

# In[21]:


#import seaborn as sns
#f, ax = plt.subplots(figsize=[8,6])
#sns.heatmap((data).corr(),
#            annot=True)
#ax.set_title("Correlation of Attributes")
#plt.show()


# # Replace Null values - Numerical Attributes

# In[22]:


print (data['Item_Weight'].isnull().sum())
data["Item_Weight"] = data["Item_Weight"].fillna(data["Item_Weight"].mean())
print(data['Item_Weight'].isnull().sum())

print (data['Outlet_Size'].isnull().sum())
data['Outlet_Size'] = data['Outlet_Size'].fillna(data['Outlet_Size'].mode().iloc[0])
print (data['Outlet_Size'].isnull().sum())


# In[23]:


#Impute for attribute with 0 value for Visibility

print ('Number of Records with Visibility = 0 is ', (data['Item_Visibility'] == 0).sum())
data['Item_Visibility'] = data['Item_Visibility'].mask(data['Item_Visibility'] == 0,data['Item_Visibility'].mean(skipna=True))
print ('Number of Records with Visibility = 0 is ', data['Item_Visibility'].isnull().sum())


# In[24]:


# Head 10 records from Combined data
data.head(10)


# # Handling Categorical Values

# In[25]:


#Item type combine:
data['Item_Identifier'].value_counts()
data['Item_Type_Combined'] = data['Item_Identifier'].apply(lambda x: x[0:2])
data['Item_Type_Combined'] = data['Item_Type_Combined'].map({'FD':'Food',
                                                             'NC':'Non-Consumable',
                                                             'DR':'Drinks'})
data['Item_Type_Combined'].value_counts()


# In[26]:


#Years:
data['Outlet_Years'] = 2018 - data['Outlet_Establishment_Year']
data['Outlet_Years'].describe()


# In[27]:


#Change categories of low fat:
print ('Original Categories:')
print (data['Item_Fat_Content'].value_counts())

data['Item_Fat_Content'] = data['Item_Fat_Content'].replace({'LF':'Low Fat',
                                                             'reg':'Regular',
                                                             'low fat':'Low Fat'})
print (data['Item_Fat_Content'].value_counts())


# In[28]:


# Create Non Edible category:
data.loc[data['Item_Type_Combined']=="Non-Consumable",'Item_Fat_Content'] = "Non-Edible"
data['Item_Fat_Content'].value_counts()


# # Encoding Categorical Attributes

# In[29]:


#Import library:
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
#New variable for outlet
data['Outlet'] = le.fit_transform(data['Outlet_Identifier'])
var_mod = ['Item_Fat_Content','Outlet_Location_Type','Outlet_Size','Item_Type_Combined','Outlet_Type','Outlet']
le = LabelEncoder()
for i in var_mod:
    data[i] = le.fit_transform(data[i])


# In[30]:


#One_Hot_Coding on the different catergories of dataset
data = pd.get_dummies(data, columns=['Item_Fat_Content','Outlet_Location_Type','Outlet_Size','Outlet_Type',
                              'Item_Type_Combined','Outlet_Identifier'])


# In[31]:


# Display the combined dataset after encoding- 
name_of_attribs = list(data)
data.apply(lambda x: len(x.unique()))


# # Implementation of Pipeline -

# In[32]:


from sklearn.base import BaseEstimator, TransformerMixin

# Create a class to select numerical or categorical columns 
# since Scikit-Learn doesn't handle DataFrames yet
class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values


# In[33]:


num_attribs = data[['Item_Weight','Item_Visibility']]


# In[34]:


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Imputer
num_pipeline = Pipeline([
        ('selector', DataFrameSelector(num_attribs)),
        ('std_scaler', StandardScaler()),
    ])


# # Completing the Combined data Imputation and drop attributes

# In[35]:


data.drop(['Item_Type','Outlet_Establishment_Year'],axis=1,inplace=True)


# In[36]:


data.head()


# # Create Training and Test dataset from Combined dataset

# In[37]:


#Divide into test and train:
trainr = data.loc[data['source']=="train"]
testr = data.loc[data['source']=="test"]


# In[38]:


# Display the record count in each dataset
print (trainr.shape, testr.shape, data.shape)


# In[39]:


#Drop Target from Test and manual identifier column:
testr.drop(['Item_Outlet_Sales','source'],axis=1,inplace=True)
trainr.drop(['source'],axis=1,inplace=True)


# In[40]:


trainr.head()


# In[41]:


trainr.describe()


# In[42]:


trainr.info()


# In[43]:


testr.describe()


# In[44]:


# Create the train and test dataset
Xtrain = trainr.drop(["Item_Outlet_Sales"], axis=1)
ytrain = trainr["Item_Outlet_Sales"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(Xtrain, ytrain)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


# In[45]:


# Create a dataset without Item_Identifier
from sklearn.metrics import accuracy_score
predictors = [x for x in Xtrain.columns if x not in ['Item_Identifier']]
print(predictors)


# # Linear Regression

# In[46]:


r_pipeline = Pipeline([
        ('std_scaler', StandardScaler()),
        ('linear', LinearRegression())
    ])

r_pipeline.fit(X_train[predictors], y_train)
preds = r_pipeline.predict(X_test[predictors])


# In[47]:


from sklearn import cross_validation, metrics
cv_score = cross_validation.cross_val_score(r_pipeline, X_train[predictors], y_train, cv=20, 
                                            scoring='mean_squared_error')
cv_score = np.sqrt(np.abs(cv_score))
RMSE = cv_score.mean()
print('RMSE is ', RMSE)


# In[48]:


from sklearn.metrics import mean_squared_error
RMSEd = mean_squared_error(preds, y_test)
RMSEsd=np.sqrt(RMSEd)
print('RMSE is ', RMSEsd)


# ## GradientBoostingRegressor Tree Implementation

# In[56]:


from sklearn.ensemble import GradientBoostingRegressor

pipedesc = Pipeline([('std_scaler', StandardScaler()),
                     ('grboostregmodel', GradientBoostingRegressor(n_estimators=100, learning_rate=0.1,
                                                                   max_depth=1, random_state=0, loss='ls'))])


# In[57]:


dscrmol = pipedesc.fit(X_train[predictors], y_train)
#print(dscrmol.get_params())
preddesctree = dscrmol.predict(X_test[predictors])


# In[58]:


from sklearn import cross_validation, metrics
cv_scoredesc = cross_validation.cross_val_score(pipedesc, X_train[predictors], y_train, cv=20, 
                                            scoring='mean_squared_error')
cv_scoredesct = np.sqrt(np.abs(cv_scoredesc))
RMSEdesc = cv_scoredesct.mean()
print('RMSE is ', RMSEdesc)


# ## HyperTune Gradient Boosting Regressor

# In[66]:


from sklearn.ensemble import GradientBoostingRegressor

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


# In[67]:


clfpred = clfgrdmof.predict(X_test[predictors])


# In[68]:


from sklearn import cross_validation, metrics
cvgd_scoredesc = cross_validation.cross_val_score(clfgrd, X_train[predictors], y_train, cv=20, 
                                            scoring='mean_squared_error')
cvgd_scoredesct = np.sqrt(np.abs(cvgd_scoredesc))
RMSEdescgd = cvgd_scoredesct.mean()
print('RMSE is ', RMSEdescgd)


# In[69]:


results = pd.DataFrame(columns=["Description", "RMSE"])
results.loc[len(results)] = ["LinearModel", RMSE]
results.loc[len(results)] = ["GradientBoost", RMSEdesc]
results.loc[len(results)] = ["HypertunedGradientBoost", RMSEdescgd]
results


# # Predict on original Test Set using Random forest model with Hypertune

# In[71]:

overallprediction=clfgrdmof.predict(testr[predictors])


# In[72]:


print(overallprediction)


# In[74]:


# save the model to disk
import pickle
filename = 'finalized_model.pkl'
pickle.dump(clfgrdmof, open(filename, 'wb'))

 
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
Test1 = loaded_model.predict(testr[predictors])

# save the model to disk
import pickle
filenamepb = 'finalized_model.pb'
pickle.dump(clfgrdmof, open(filenamepb, 'wb'))

 
# load the model from disk
loaded_modelpb = pickle.load(open(filenamepb, 'rb'))
Test2 = loaded_modelpb.predict(testr[predictors])

# In[75]:


print(Test1)

print(Test2)

# # Overall Summary - 

# Overall dataset - Initially, with Bigmart dataset, it has total of (14204, 13) records and was speratly provided 
# with train(8523, 13) and test (5681, 12) dataset. It has 13 attributes with numerical and catagorical values. 
# 
# Below are the details on how we have processed and cleaned the data provided - data cleaning and preprocessing 
# activities is performed on combined dataset with addition column added as "Source" to differentiate the data later
# for splitting the data.
# 
# * **Data Exploration** – Analysed and plotted the categorical and continuous feature summaries to see which feature 
# is closly related with target variable. This helped us with deciding which feature are influcing the prediction.
# 
# * **Data Cleaning and Feature engineering** – Encoding and imputing missing values in the data and checking for 
# outliers with 
# replacing with mean values and relabeling the values in categorical columns as to bring consistencies. 
# Also, added additional columns for effective feature engineering.
# 
# * **Model Experiment** – Experiment has started with Linear Regression as Base model, with implementation of Gradient Boost Regressor and Hypertuned Gradient Boost Regressor.
# 
# * **Model tunning** - GridsearchCV has been used tunning model and calculated the root mean 
# square error.
# 
# * **Model Evaluation** - After all the experiments and results captured in Table, it is clear the results are better 
# with Hypertuned Gradient Boost Regressor.
# 
# Below are the outcome of each model -
#     - LinearModel (RMSE - 1129.379095)
#     - GradientBoost - 1134.281348)
#     - Hypertuned Gradient Boost (RMSE - 1116.983860)
# 
# 

# # Team Members - 

# ### - Arijit Sinha
# ### - Ritesh Tandon
