import streamlit as st 
from joblib import dump, load
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

def main():
    st.title('Anemia Detection App') 
    
    chapters = ['Introduction', 'Detect Anemia']
    chapter_choice = st.sidebar.selectbox("Choose", chapters)

    if chapter_choice == 'Introduction':
        show_introduction()
    elif chapter_choice == 'Detect Anemia':
        show_chapter1()

def show_introduction():
    st.write("""
         This app helps you to find out weather you have anemia or not. You provide the values of your Gender, 
         RBC counnt, PCV, MCH, MCHC, and RDW value of your blood and the app will detect if you have mild, moderate or severe 
         type of anemia
    """)


def show_chapter1():
    st.subheader('Please provide the values carefully')
    sex = st.slider('sex', 0.0, 1.0, 0.0)
    rbc = st.slider('rbc', 1.36, 6.9, 1.36)
    pcv = st.slider('pcv', 13.1, 56.9, 13.1)
    mch = st.slider('mch', 14.7, 41.4, 14.7)
    mchc = st.slider('mchc', 23.6, 50.2, 23.6)
    rdw = st.slider('rdw', 10.6, 29.2, 10.6)
    

    if st.button('Predict'): 

        scaler = load('/root/capsule/tutorial/Scaler.pickle') 

        input_data = np.array([[sex, rbc, pcv,0, mch, mchc, rdw, 0, 0, 0, 0, 0]])
        input_data_scaled = scaler.transform(input_data)


        inputt = np.concatenate((input_data_scaled[:, 0:3], input_data_scaled[:, 4:7]), axis=1)

        model = load('/root/capsule/tutorial/Random_Forest_Classification.pickle') 

        prediction = model.predict(inputt)

        st.subheader('Prediction')
        st.write(prediction)


if __name__ == "__main__":
    main()

# run the following comands before running the app
# pip install streamlit 
# pip install joblib
# pip install scikit-learn==1.2.2