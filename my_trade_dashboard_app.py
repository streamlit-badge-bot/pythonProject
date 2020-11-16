import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()
import base64

main_bg = "pink.jpg"
main_bg_ext = "jpg"

side_bg = "pink.jpg"
side_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.write(""" # Malaysia Trade Dashboard Application """)
st.write("Visualisation of Malaysia Trade datasets with only few clicks")

raw_df = pd.read_csv('trade.csv')
df = raw_df.dropna()


def single_graph_bar(column,sort):
    fig, ax = plt.subplots(1, 1)
    if (column == 'COUNTRY') or (column == 'SITC 2 DIGIT'):
        k = st.slider('Top:', 1, df[column].nunique(), 10, key='22')
        df.groupby(column).agg({'IMPORT (RM)': 'sum', 'EXPORT (RM)': 'sum'}).sort_values(by=sort, ascending=False).iloc[:k].plot(kind='bar', ax=ax)
    else:
        df.groupby(column).agg({'IMPORT (RM)': 'sum', 'EXPORT (RM)': 'sum'}).sort_values(by=sort, ascending=False).plot(kind='bar', ax=ax)
    st.pyplot(fig)

def single_graph_barh(column,sort):
    fig, ax = plt.subplots(1, 1)
    if (column == 'COUNTRY') or (column == 'SITC 2 DIGIT'):
        k = st.slider('Top:', 1,df[column].nunique(),10, key = '19' )
        df.groupby(column).agg({'IMPORT (RM)': 'sum' , 'EXPORT (RM)': 'sum'}).sort_values(by = sort, ascending = False).iloc[:k].sort_values(by = sort).plot(kind = 'barh',  ax = ax)
    else:
        df.groupby(column).agg({'IMPORT (RM)': 'sum', 'EXPORT (RM)': 'sum'}).sort_values(by=sort, ascending=False).sort_values(by=sort).plot(kind='barh', ax=ax)
    st.pyplot(fig)

def single_graph_line():
    fig, ax = plt.subplots(1, 1)
    df.groupby('YEAR').agg({'IMPORT (RM)': 'sum' , 'EXPORT (RM)': 'sum'}).iloc[:20].plot( ax = ax)
    st.pyplot(fig)

def bi_graph_bar(column_1, column_2, i, sort):
    fig, ax = plt.subplots(1, 1)
    if (column_1 == 'COUNTRY') or (column_1 == 'SITC 2 DIGIT'):
        k = st.slider('Top:', 1, df[column_1].nunique(), 10, key='23')
        df[df[column_2] == i].groupby(column_1).agg({'IMPORT (RM)': 'sum', 'EXPORT (RM)': 'sum'}).sort_values(by=sort, ascending=False).iloc[:k].plot(kind='bar', ax=ax, title=column_2 + ': ' + str(i));
    else:
        df[df[column_2] == i].groupby(column_1).agg({'IMPORT (RM)': 'sum', 'EXPORT (RM)': 'sum'}).sort_values(by=sort, ascending=False).plot(kind='bar', ax=ax, title=column_2 + ': ' + str(i));
    st.pyplot(fig)

def bi_graph_barh(column_1, column_2, i, sort):
    fig, ax = plt.subplots(1, 1)
    if (column_1 == 'COUNTRY') or (column_1 == 'SITC 2 DIGIT'):
        k = st.slider('Top:', 1,df[column_1].nunique(),10, key = '20' )
        df[df[column_2] == i].groupby(column_1).agg({'IMPORT (RM)':'sum','EXPORT (RM)':'sum'}).sort_values(by = sort, ascending = False).iloc[:k].sort_values(by = sort).plot(kind = 'barh', ax = ax, title = column_2 + ': ' + str(i));
    else:
        df[df[column_2] == i].groupby(column_1).agg({'IMPORT (RM)': 'sum', 'EXPORT (RM)': 'sum'}).sort_values(by=sort,ascending=False).sort_values(by = sort).plot(kind='barh', ax=ax, title=column_2 + ': ' + str(i));
    st.pyplot(fig)

def bi_graph_line(column, i):
    fig, ax = plt.subplots(1, 1)
    df[df[column] == i].groupby('YEAR').agg({'IMPORT (RM)':'sum','EXPORT (RM)':'sum'}).iloc[:20].plot( ax = ax, title = column + ': ' + str(i));
    st.pyplot(fig)

def multiple_graph_bar(column_1, column_2, i, column_3, j, sort):
    fig, ax = plt.subplots(1, 1)
    if (column_1 == 'COUNTRY') or (column_1 == 'SITC 2 DIGIT'):
        k = st.slider('Top:', 1, df[column_1].nunique(), 10, key='24')
        df[(df[column_2] == i) & (df[column_3] == j)].groupby(column_1).agg({'IMPORT (RM)': 'sum', 'EXPORT (RM)': 'sum'}).sort_values(by=sort, ascending=False).iloc[:k].plot(kind='bar', ax=ax, title=column_2 + ': ' + str(i) + ' and ' + column_3 + ': ' + str(j));
    else:
        df[(df[column_2] == i) & (df[column_3] == j)].groupby(column_1).agg({'IMPORT (RM)': 'sum', 'EXPORT (RM)': 'sum'}).sort_values(by=sort, ascending=False).plot(kind='bar', ax=ax, title=column_2 + ': ' + str(i) + ' and ' + column_3 + ': ' + str(j));
    st.pyplot(fig)

def multiple_graph_barh(column_1, column_2, i, column_3, j, sort):
    fig, ax = plt.subplots(1, 1)
    if (column_1 == 'COUNTRY') or (column_1 == 'SITC 2 DIGIT'):
        k = st.slider('Top:', 1,df[column_1].nunique(),10, key = '21' )
        df[(df[column_2] == i) & (df[column_3] == j)].groupby(column_1).agg({'IMPORT (RM)':'sum','EXPORT (RM)':'sum'}).sort_values(by = sort, ascending = False).iloc[:k].sort_values(by = sort).plot(kind = 'barh', ax = ax, title = column_2 + ': ' + str(i) + ' and ' + column_3 + ': '+ str(j));
    else:
        df[(df[column_2] == i) & (df[column_3] == j)].groupby(column_1).agg({'IMPORT (RM)': 'sum', 'EXPORT (RM)': 'sum'}).sort_values(by=sort, ascending=False).sort_values(by = sort).plot(kind='barh', ax=ax, title=column_2 + ': ' + str(i) + ' and ' + column_3 + ': ' + str(j));
    st.pyplot(fig)

def multiple_graph_line(column_1, i, column_2, j):
    fig, ax = plt.subplots(1, 1)
    df[(df[column_1] == i) & (df[column_2] == j)].groupby('YEAR').agg({'IMPORT (RM)':'sum','EXPORT (RM)':'sum'}).iloc[:20].plot( ax = ax, title = column_1 + ': ' + str(i) + ' and ' + column_2 + ': '+ str(j));
    st.pyplot(fig)

def bar_graph():
    columns = []
    columns = st.multiselect('Feature(s):', ['YEAR', 'COUNTRY', 'SITC 1 DIGIT', 'SITC 2 DIGIT'], default = ['YEAR'], key = '1')
    try:
        if ('SITC 1 DIGIT' in columns) & ('SITC 2 DIGIT' in columns):
            st.write("You may only choose either one of SITC 1 DIGIT and SITC 2 DIGIT")
        else:
            if len(columns) == 1:
                sort = st.selectbox('Sort by:', ['IMPORT (RM)', 'EXPORT (RM)'], key='2')
                single_graph_bar(columns[0], sort)
            elif len(columns) == 2:
                i = st.selectbox(columns[1] + ':', np.sort(df[columns[1]].unique()), key='3')
                sort = st.selectbox('Sort by:', ['IMPORT (RM)', 'EXPORT (RM)'], key='4')
                bi_graph_bar(columns[0], columns[1], i, sort)
            elif len(columns) == 3:
                i = st.selectbox(columns[1] + ':', np.sort(df[columns[1]]).unique(), key='5')
                j = st.selectbox(columns[2] + ':', np.sort(df[columns[2]].unique()), key='6')
                sort = st.selectbox('Sort by:', ['IMPORT (RM)', 'EXPORT (RM)'], key='7')
                multiple_graph_bar(columns[0], columns[1], i, columns[2], j, sort)
    except IndexError:
        st.error('No data available')


def line_graph():
    columns = []
    columns = st.multiselect('Feature(s):', ['COUNTRY', 'SITC 1 DIGIT', 'SITC 2 DIGIT'],  key = '8')
    try:
        if ('SITC 1 DIGIT' in columns) & ('SITC 2 DIGIT' in columns):
            st.write("You may only choose either one of SITC 1 DIGIT and SITC 2 DIGIT")
        else:
            if len(columns) == 1:
                i = st.selectbox(columns[0] + ':', np.sort(df[columns[0]].unique()), key='9')
                bi_graph_line(columns[0], i,)
            elif len(columns) == 2:
                i = st.selectbox(columns[0] + ':', np.sort(df[columns[0]].unique()), key='10')
                j = st.selectbox(columns[1] + ':', np.sort(df[columns[1]].unique()), key='11')
                multiple_graph_line(columns[0], i, columns[1], j)
            else:
                single_graph_line()
    except IndexError:
        st.error('No data available')


def barh_graph():
    columns = []
    columns = st.multiselect('Feature(s):', ['YEAR', 'COUNTRY', 'SITC 1 DIGIT', 'SITC 2 DIGIT'], default = ['YEAR'], key ='12')
    try:
        if ('SITC 1 DIGIT' in columns) & ('SITC 2 DIGIT' in columns):
            st.write("You may only choose either one of SITC 1 DIGIT and SITC 2 DIGIT")
        else:
            if len(columns) == 1:
                sort = st.selectbox('Sort by:', ['IMPORT (RM)', 'EXPORT (RM)'], key='13')
                single_graph_barh(columns[0], sort)
            elif len(columns) == 2:
                i = st.selectbox(columns[1] + ':', np.sort(df[columns[1]].unique()), key='14')
                sort = st.selectbox('Sort by:', ['IMPORT (RM)', 'EXPORT (RM)'], key='15')
                bi_graph_barh(columns[0], columns[1], i, sort)
            elif len(columns) == 3:
                i = st.selectbox(columns[1] + ':', np.sort(df[columns[1]].unique()), key='16')
                j = st.selectbox(columns[2] + ':', np.sort(df[columns[2]].unique()), key='17')
                sort = st.selectbox('Sort by:', ['IMPORT (RM)', 'EXPORT (RM)'], key='18')
                multiple_graph_barh(columns[0], columns[1], i, columns[2], j, sort)
    except IndexError:
        st.error('No data available')


def plot_graph():
    graph = st.selectbox('Type of graph:', ['Time-Series', 'Bar-Vertical', 'Bar-Horizontal'])
    if graph == 'Bar-Vertical':
        bar_graph()
    elif graph == 'Bar-Horizontal':
        barh_graph()
    else:
        line_graph()

plot_graph()