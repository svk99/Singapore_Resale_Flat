import streamlit as st
import joblib

town_mapping = {
    'ANG MO KIO': 1,'BEDOK': 2,'BISHAN': 3,'BUKIT BATOK': 4,'BUKIT MERAH': 5,'BUKIT TIMAH': 6,
    'CENTRAL AREA': 7,'CHOA CHU KANG': 8,'CLEMENTI': 9,'GEYLANG': 10,'HOUGANG': 11,'JURONG EAST': 12,
    'JURONG WEST': 13,'KALLANG/WHAMPOA': 14,'MARINE PARADE': 15,'QUEENSTOWN': 16,'SENGKANG': 17,
    'SERANGOON': 18,'TAMPINES': 19,'TOA PAYOH': 20,'WOODLANDS': 21,'YISHUN': 22,'LIM CHU KANG': 23,
    'SEMBAWANG': 24,'BUKIT PANJANG': 25,'PASIR RIS': 26,'PUNGGOL': 27
}

flat_model_mapping = {
    'improved':1, 'new generation':2, 'model a':3, 'standard':4, 'simplified':5,
       'model a-maisonette':6, 'apartment':7, 'maisonette':8, 'terrace':9,
       '2-room':10, 'improved-maisonette':11, 'multi generation':12,
       'premium apartment':13, 'adjoined flat':14, 'premium maisonette':15,
       'model a2':16, 'dbss':17, 'type s1':18, 'type s2':19, 'premium apartment loft':20,
       '3gen':21
}

flat_type_mapping = {
    '1 ROOM': 1,'2 ROOM': 2,'3 ROOM': 3,'4 ROOM': 4,'5 ROOM': 5,
    'EXECUTIVE': 6,'MULTI GENERATION': 7
}

st.subheader('Real Estate Price Prediction')
month=st.number_input('Month', min_value=1, max_value=12)
year=st.number_input('Year', min_value=1990, max_value=2023)
storey_lower=st.number_input('Storey Lower', min_value=1, max_value=49)
storey_upper=st.number_input('Storey Upper', min_value=3, max_value=51)
lease_year=st.number_input('Lease Commence Year', min_value=1966, max_value=2022)
floor_area=st.number_input('Floor Area (sq.m)',step=0.01)
town_key=st.selectbox('Select Town',town_mapping.keys())
flat_type_key=st.selectbox('Select Flat Type',flat_type_mapping.keys())
flat_model_key=st.selectbox('Select Flat Model',flat_model_mapping.keys())

town_value=town_mapping[town_key]
flat_type_value=flat_type_mapping[flat_type_key]
flat_model_value=flat_model_mapping[flat_model_key]

if st.button('Submit'):
    model=joblib.load('.../real_estate.joblib')

    independent_variables=[month,town_value,flat_type_value,floor_area,flat_model_value,lease_year,year,storey_lower,storey_upper]
    price_prediction=model.predict([independent_variables])
    price=price_prediction[0]
    st.write(f'Predicted Resale Price: {price:.2f}')