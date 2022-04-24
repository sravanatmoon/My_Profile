import streamlit as st
import pandas as pd
import numpy as np
import time


st.set_page_config(page_title='Sravan Singireddy', page_icon='🌋', layout="wide", initial_sidebar_state="auto", 
menu_items={'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"})

with st.sidebar:
    '''
    # Sravan Singireddy
    '''
    # with st.spinner("Loading..."):
    #     time.sleep(5)
    # st.success("Done!")

# Draw a title and some text to the app:
'''     
### Summary
I have a strong passion towards Artificial
Intelligence. I am of the view that AI leverage
can enable us, humans, to see a limitless world
beyond our conventional limits. Most
sophisticated applications of the day are just the
starting points for the same.'''

'''
## WORK EXPERIENCE
### Data Scientist 
#### Aureus Tech Systems, Hyderabad (07/2021 - 04/2022)'''
with st.expander("Details"):
   ''' 
    Aureus creates new solutions, fit for today's world, that enables companies to achieve these key drivers.

    1. Developed an AI-based Assistant almost end to end which can query the Database in Natural language and give the results to create an intuitive report. 
    2. Developed a feature framework which can classify Huge documents For the product Anvesa. 
    3. Responsible for exploring new opportunities in the field of AI, In the domain where Organization's operations are present. 

    '''

'''### Manager AI (Data Scientist )
   #### Kaaval Security Systems, Kottayam, Kerala (10/2017 - 07/2021)
'''

with st.expander("Details"):
    '''
    KSS is a smart security systems solutions provider for highly secured infrastructures like embassies, govt offices in and around Kuwait (Gulf Nations)

    * Lead the R&D team on AI, which designed a Computer Vision (an Application of AI ) -based application for Automatic attendance & time management using facial recognition. 
    * Engagements with Clients and Worked on Artificially Intelligent applications for NLP tasks based on client requirements. 
    * Worked on LSTM, self-Attention, Transformers by Hugging Face, variants of BERT, NLTK, etc. while working for NLP Projects. 

'''

'''
### Assist Manager
#### MAHINDRA & MAHINDRA LTD'''
with st.expander("Details"):
    '''
    * Problem solving in virtual designs of Physical products (Automobiles). 
    * Responsible for delivery of the designs to suppliers, and final development of the products. 
    * Responsible for troubleshooting issues of Export models (Cabin tractors) specific to my dept.

    '''


'''### ACHIEVEMENTS
* Placement coordinator for NIT Kurukshetra for the academic year 2013-14
* Captain of Chess Wing ( gold medal in chess @IIT Jodhpur)'''

'''### Skills
'''
with st.expander("Skills"):
    st.button('Artificial Intelligence')
    st.button('Machine Learning : Regression & Classifications')
    st.button('Deep Learning : NLP, Computer Vision')
    st.button('RNNs-Transformers')
    st.button('Tensorflow')
    st.button('scikit-learn')
    st.button('Python')

'''### EDUCATION
#### B.Tech | Mechanical Engineering
#### National Institute of Technology, Kurukshetra
06/2010 - 06/2014, CGPA : 7.8/10 '''

'''
### ORGANIZATIONS
#### SAEINDIA NIT Kurukshetra Collegiate Club
Designed a full working model of All-Terrain Vehicle (ATV), which got all
India 9th position in the competition BAJA’13 in Feb 2013.'''

'''### LANGUAGES
#### English 
    - Native or Bilingual Proficiency
#### Telugu 
    - Native or Bilingual Proficiency'''