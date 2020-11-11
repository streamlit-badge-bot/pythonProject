
# Import Libraries
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report, roc_curve
import shap


st.write(""""
# Bank's Save Deposit Prediction
""")

df = pd.read_csv('C:\\Users\\Muhammad Hazim\\PycharmProjects\\pythonProject\\bank.csv')

st.write(""" Datasets """)
st.dataframe(df)


fig = plt.figure()
sns.countplot(df['deposit'])
st.pyplot(fig)

cat_feat = []
num_feat = []

for column in df.drop('deposit', axis = 1).columns.values:
    if df[column].nunique() < 20:
        cat_feat.append(column)
    else:
        num_feat.append(column)

def distribution_num_feat(column):
    fig, ax = plt.subplots(1, 3, figsize = (20,5))

    sns.distplot(df[column], ax = ax[0])
    sns.boxplot(df[column], ax = ax[1])
    sns.boxplot(df['deposit'], df[column], ax = ax[2])
    st.pyplot(fig)

for column in num_feat:
    distribution_num_feat(column)

df.deposit = df.deposit.map({'yes':1, 'no':0})

def distribution_cat_feat(column):
    fig, ax = plt.subplots(1, 2, figsize = (15,5))

    sns.countplot(df[column], ax = ax[0])
    df[[column, 'deposit']].groupby(column).mean().sort_values(by = 'deposit', ascending = False).plot(kind = 'bar', ax = ax[1])
    st.pyplot(fig)

for column in cat_feat:
    distribution_cat_feat(column)


df.pdays = df.pdays.replace(-1,0)
df.duration = df.duration/60

x = df.drop("deposit", axis=1)
y = df["deposit"]

categorical_features = np.where(x.dtypes != np.float)[0]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42, stratify = y)

def score(model):
    df1 = pd.DataFrame(index = ['Accuracy', 'Precision', 'Recall', 'ROC AUC'] )
    df1['Train Score'] = [accuracy_score(y_train, model.predict(x_train)), precision_score(y_train, model.predict(x_train)), recall_score(y_train, model.predict(x_train)), roc_auc_score(y_train, model.predict_proba(x_train)[:,1])]
    df1['Test Score'] = [accuracy_score(y_test, model.predict(x_test)), precision_score(y_test, model.predict(x_test)), recall_score(y_test, model.predict(x_test)), roc_auc_score(y_test, model.predict_proba(x_test)[:,1])]
    return df1

cb=CatBoostClassifier(learning_rate=0.001, eval_metric='AUC')
cb.fit(x_train, y_train, cat_features = categorical_features, eval_set=(x_test, y_test),verbose = False)


st.dataframe(score(cb))

shap_values = shap.TreeExplainer(cb).shap_values(x_test)

fig = plt.figure()
shap.summary_plot(shap_values, x_test, plot_type = 'bar')
st.pyplot(fig)

fig = plt.figure()
shap.summary_plot(shap_values, x_test)
st.pyplot(fig)


def get_user_input():
    age = st.sidebar.slider('age',18,95,25)
    balance = st.sidebar.slider('balance',-10000, 90000, 0)
    day = st.sidebar.slider('day',1,31,15)
    duration = st.sidebar.slider('duration',0, 40000,100)
    campaign = st.sidebar.slider('campaign', 1,63,15)
    pdays = st.sidebar.slider('pdays',0,854,5)
    previous = st.sidebar.slider('previous',0,58,20)
    job = st.sidebar.selectbox('job', ['admin.', 'technician', 'services', 'management', 'retired',
       'blue-collar', 'unemployed', 'entrepreneur', 'housemaid',
       'unknown', 'self-employed', 'student'], key='1')
    education = st.sidebar.selectbox('education', ['secondary', 'tertiary', 'primary', 'unknown'], key='1')

    user_data = {'age':age, 'balance' : balance, 'day' :day, 'duration' : duration,
                 'campaign' : campaign, 'pdays': pdays, 'previous': previous, 'job': job,
                 'education': education }

    features = pd.DataFrame(user_data, index = [0])
    features = pd.get_dummies(features, drop_first = True)
    return features

user_input = get_user_input()



