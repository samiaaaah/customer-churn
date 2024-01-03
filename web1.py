# streamlit_app.py
import numpy as np
import streamlit as st
import pandas as pd
import joblib

#model
rf_model = joblib.load('random_forest_model.pkl')



# Use HTML to add white color to the title
st.markdown("<h1 style='color: white;'>Customer Churn Prediction App</h1>", unsafe_allow_html=True)

CreditScore=st.number_input('CreditScore', min_value=350, max_value=850)
Age=st.number_input('Age', min_value=0, max_value=100)
Tenure=st.number_input('Tenure',step=1.,format="%.0f")
Balance=st.number_input('Balance')
NumOfProducts=st.number_input('NumOfProducts',min_value=0.,step=1.,format="%.0f")
HasCrCard=st.selectbox('HasCrCard',[0,1])
IsActiveMember=st.selectbox('IsActiveMember',[0,1])
EstimatedSalary=st.number_input('EstimatedSalary',min_value=0)
Gender=st.selectbox('Gender',['Male','Female'])
Geography=st.selectbox('Geography',['Germany','Spain','France'])

if st.button('Predict'):
    girl=0
    if Gender=='Female':
        girl=1
    geogermany=0
    geospain=0
    if Geography=='Germany':
        geogermany=1
    elif Geography=='Spain':
        geospain=1
    query = np.array([CreditScore,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,girl,geogermany,geospain])
    query = query.reshape(1, 11)
    s=None
    if int(rf_model.predict(query)[0])==0:
        s='Customer will  not exit'
    else:
        s='Customer will  exit'
    result=f"<div class='title'> predicted : \n{s}</div>"
    # st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))
    st.markdown(result, unsafe_allow_html=True)
    




def set_background_image(image_url):
    # Apply custom CSS to set the background image
    page_bg_img = '''
    <style>
    .stApp {
        background-position: top;
        background-image: url(%s);
        background-size: cover;
    }

    @media (max-width: 768px) {
        /* Adjust background size for mobile devices /
        .stApp {
            background-position: top;
            background-size: contain;
            background-repeat: no-repeat;
        }
    }
    </style>
    ''' % image_url
    st.markdown(page_bg_img, unsafe_allow_html=True)


def main():
    # Set the background image URL
    background_image_url = "https://wallpapercrafter.com/sizes/3840x2160/241714-cafe-bar-counter-with-customers-in-the-background_.jpg"



    # Set the background image
    set_background_image(background_image_url)


    custom_css = """
       <style>
       body {
           background-color: #492581;
           color: #492581;
           font-family: Arial, sans-serif;
       }
       select {
           background-color: #000000 !important; / Black background for select box /
           color: #ffffff !important; / White text within select box /
       }
       label {
           color: #ffffff !important; / White color for select box label */
       }
       </style>
       """
    st.markdown(custom_css, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
