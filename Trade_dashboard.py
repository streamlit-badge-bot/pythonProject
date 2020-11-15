import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.write(""""Hello World!""")

raw_df = pd.read_csv('trade.csv')
df = raw_df.dropna()
st.dataframe(df)

def single_graph(column,sort):
    fig, ax = plt.subplots(1, 1)
    df.groupby(column).agg({'IMPORT (RM)': 'sum' , 'EXPORT (RM)': 'sum'}).sort_values(by = sort, ascending = False).iloc[:20].plot(kind = 'bar', ax = ax)
    st.pyplot(fig)

def get_user_input():
    column = st.selectbox('column', ['YEAR', 'COUNTRY', 'SITC 1 DIGIT', 'SITC 2 DIGIT'], key = '1')
    sort = st.selectbox('sort', ['IMPORT (RM)', 'EXPORT (RM)'], key = '2')

    single_graph(column, sort)

get_user_input()

def bi_graph(column_1, column_2, i, sort):
    fig, ax = plt.subplots(1, 1)
    df[df[column_2] == i].groupby(column_1).agg({'IMPORT (RM)':'sum','EXPORT (RM)':'sum'}).sort_values(by = sort, ascending = False).iloc[:20].plot(kind = 'bar', ax = ax, title = column_2 + ': ' + str(i));
    st.pyplot(fig)

def get_user_input_bi():
    column_1 = st.selectbox('column_1', ['YEAR', 'COUNTRY', 'SITC 1 DIGIT', 'SITC 2 DIGIT'], key = '3')
    column_2 = st.selectbox('column_2', ['YEAR', 'COUNTRY', 'SITC 1 DIGIT', 'SITC 2 DIGIT'], key = '4')
    i = st.selectbox('i', df[column_2].unique(), key = '5')
    sort = st.selectbox('sort', ['IMPORT (RM)', 'EXPORT (RM)'], key = '6')

    bi_graph(column_1, column_2, i,sort)

get_user_input_bi()

def multiple_graph(column_1, column_2, i, column_3, j, sort):
    fig, ax = plt.subplots(1, 1)
    df[(df[column_2] == i) & (df[column_3] == j)].groupby(column_1).agg({'IMPORT (RM)':'sum','EXPORT (RM)':'sum'}).sort_values(by = sort, ascending = False).iloc[:20].plot(kind = 'bar', ax = ax, title = column_2 + ': ' + str(i) + ' and ' + column_3 + ': '+ str(j));
    st.pyplot(fig)

def get_user_input_multiple():
    column_1 = st.selectbox('column_1', ['YEAR', 'COUNTRY', 'SITC 1 DIGIT', 'SITC 2 DIGIT'], key = '7')
    column_2 = st.selectbox('column_2', ['YEAR', 'COUNTRY', 'SITC 1 DIGIT', 'SITC 2 DIGIT'], key = '8')
    i = st.selectbox('i', df[column_2].unique(), key = '9')
    column_3 = st.selectbox('column_3', ['YEAR', 'COUNTRY', 'SITC 1 DIGIT', 'SITC 2 DIGIT'], key = '10')
    j = st.selectbox('i', df[column_3].unique(), key = '11')
    sort = st.selectbox('sort', ['IMPORT (RM)', 'EXPORT (RM)'], key = '12')

    multiple_graph(column_1, column_2, i, column_3, j, sort)

get_user_input_multiple()

def get_user_input_try():
    columns = []
    columns = st.multiselect('Feature(s):', ['YEAR', 'COUNTRY', 'SITC 1 DIGIT', 'SITC 2 DIGIT'], default = ['YEAR'], key = '13')
    if len(columns) == 1:
        sort = st.selectbox('Sorted by:', ['IMPORT (RM)', 'EXPORT (RM)'], key='15')
        single_graph(columns[0], sort)
    elif len(columns) == 2:
        i = st.selectbox(columns[1]+':', df[columns[1]].unique(), key='18')
        sort = st.selectbox('Sorted by:', ['IMPORT (RM)', 'EXPORT (RM)'], key='19')
        bi_graph(columns[0], columns[1], i, sort)
    elif len(columns) == 3:
        i = st.selectbox(columns[1]+':', df[columns[1]].unique(), key='22')
        j = st.selectbox(columns[2]+':', df[columns[2]].unique(), key='24')
        sort = st.selectbox('Sorted by:', ['IMPORT (RM)', 'EXPORT (RM)'], key='25')
        multiple_graph(columns[0], columns[1], i, column[2], j, sort)
get_user_input_try()