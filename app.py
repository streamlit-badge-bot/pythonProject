import streamlit as st
import numpy as np
import pandas as pd

st.write(""""
## Datasets
""")
df = pd.read_csv('bank.csv')
st.dataframe(df)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

st.write(""""
## Distribution of Target data
""")
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
