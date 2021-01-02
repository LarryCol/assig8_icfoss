# checkout https://assig8-icfoss.herokuapp.com/

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

pickle_in = open('salary_decision_tree.pkl', 'rb')
dtree = pickle.load(pickle_in)

work = [' Federal-gov', ' Local-gov', ' Private', ' Self-emp-inc', ' Self-emp-not-inc', ' State-gov',
            ' Without-pay']
marital = [' Divorced', ' Married-AF-spouse', ' Married-civ-spouse', ' Married-spouse-absent', 
                'Never-married', ' Separated',' Widowed']
occu = [' Adm-clerical', ' Armed-Forces', ' Craft-repair',
        ' Exec-managerial', ' Farming-fishing', ' Handlers-cleaners',
        ' Machine-op-inspct', ' Other-service', ' Priv-house-serv',
        ' Prof-specialty', ' Protective-serv', ' Sales', ' Tech-support',
        ' Transport-moving']
rac = [' Amer-Indian-Eskimo', ' Asian-Pac-Islander', ' Black', ' Other',
        ' White']
nati = [' Cambodia', ' Canada', ' China', ' Columbia', ' Cuba',
        ' Dominican-Republic', ' Ecuador', ' El-Salvador', ' England',
        ' France', ' Germany', ' Greece', ' Guatemala', ' Haiti',
        ' Holand-Netherlands', ' Honduras', ' Hong', ' Hungary', ' India',
        ' Iran', ' Ireland', ' Italy', ' Jamaica', ' Japan', ' Laos',
        ' Mexico', ' Nicaragua', ' Outlying-US(Guam-USVI-etc)', ' Peru',
        ' Philippines', ' Poland', ' Portugal', ' Puerto-Rico',
        ' Scotland', ' South', ' Taiwan', ' Thailand', ' Trinadad&Tobago',
        ' United-States', ' Vietnam', ' Yugoslavia']        
"""
# Salary classifier based on decision tree

### Enter parameters
"""
#""" #### Work Class """
work_class = st.selectbox("Work Class", options=work, key='work_class')
#""" #### Marital Status """
marital_status = st.selectbox("Marital Status", options=marital, key='marital_status')
#""" #### Occupation """
occupation = st.selectbox('Occupation', options=occu, key='occupation')
#""" #### Race """  
race = st.selectbox('Race', options=rac, key='race')
# """ #### Sex """ 
sex = st.selectbox('Sex', options=['Female', 'Male'], key='race')
#""" #### Native Country """
native = st.selectbox('Native Country', options=nati, key='native')

age = st.slider('Age', min_value=17, max_value=90, step=1, value=25, key='age')    
education = st.slider('Education level',min_value=1, max_value=16, step=1, value=10, key='education') 
hours = st.slider('Hours per Week',min_value=1, max_value=99, step=1, value=10, key='hours')
x1 = work.index(work_class)
x2 = marital.index(marital_status)
x3 = occu.index(occupation)
x4 = rac.index(race)
x5 = ['Female', 'Male'].index(sex)
x6 = nati.index(native)

x_input = np.array([[x1, x2, x3, x4, x5, x6, age, education, hours]])

if st.button('Classify based on salary range'):
    y_pred = dtree.predict(x_input)

    if y_pred:
        st.markdown('### Salary greater than 50,000')
    else:
        st.markdown('### Salary less than than 50,000')