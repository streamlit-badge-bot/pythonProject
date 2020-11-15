import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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

def single_graph(column,sort):
    fig, ax = plt.subplots(1, 1)
    df.groupby(column).agg({'IMPORT (RM)': 'sum' , 'EXPORT (RM)': 'sum'}).sort_values(by = sort, ascending = False).iloc[:20].plot(kind = 'bar', ax = ax)
    st.pyplot(fig)

def bi_graph(column_1, column_2, i, sort):
    fig, ax = plt.subplots(1, 1)
    df[df[column_2] == i].groupby(column_1).agg({'IMPORT (RM)':'sum','EXPORT (RM)':'sum'}).sort_values(by = sort, ascending = False).iloc[:20].plot(kind = 'bar', ax = ax, title = column_2 + ': ' + str(i));
    st.pyplot(fig)

def multiple_graph(column_1, column_2, i, column_3, j, sort):
    fig, ax = plt.subplots(1, 1)
    df[(df[column_2] == i) & (df[column_3] == j)].groupby(column_1).agg({'IMPORT (RM)':'sum','EXPORT (RM)':'sum'}).sort_values(by = sort, ascending = False).iloc[:20].plot(kind = 'bar', ax = ax, title = column_2 + ': ' + str(i) + ' and ' + column_3 + ': '+ str(j));
    st.pyplot(fig)

def get_user_input():
    columns = []
    columns = st.multiselect('Feature(s):', ['YEAR', 'COUNTRY', 'SITC 1 DIGIT', 'SITC 2 DIGIT'], default = ['YEAR'], key = '1')
    if  ('SITC 1 DIGIT' in columns) & ('SITC 2 DIGIT' in columns):
        st.write("You may only choose either one of SITC 1 DIGIT and SITC 2 DIGIT")
    else:
        if len(columns) == 1:
            sort = st.selectbox('Sort by:', ['IMPORT (RM)', 'EXPORT (RM)'], key='2')
            single_graph(columns[0], sort)
        elif len(columns) == 2:
            i = st.selectbox(columns[1] + ':', df[columns[1]].unique(), key='3')
            sort = st.selectbox('Sort by:', ['IMPORT (RM)', 'EXPORT (RM)'], key='4')
            bi_graph(columns[0], columns[1], i, sort)
        elif len(columns) == 3:
            i = st.selectbox(columns[1] + ':', df[columns[1]].unique(), key='5')
            j = st.selectbox(columns[2] + ':', df[columns[2]].unique(), key='6')
            sort = st.selectbox('Sort by:', ['IMPORT (RM)', 'EXPORT (RM)'], key='7')
            multiple_graph(columns[0], columns[1], i, columns[2], j, sort)

get_user_input()

