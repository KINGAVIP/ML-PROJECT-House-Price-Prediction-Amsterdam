import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image
model=pickle.load(open('ML projects/model1.pkl','rb'))
st.title("House price prediction-Amsterdam by KING")
img=Image.open('ML projects/download.jfif')
st.image(img,use_column_width=False )
area=st.number_input("area",10,1000)
room=st.number_input("rooms",1,10)
lon=st.slider("Longitude",0.00,6.00)
lat=st.slider("Latitude",0.00,100.00)
if st.button("Submit"):
    price=model.predict([[area,room,lon,lat]])
    p=float(price)
    # price=np.array(price)
    # price=price.astype(int)
    p=round(p,2)
    if p>0:
        st.success(f" ### The price is: {p}%s"%(u"\N{euro sign}"))

    else:
        st.error("Please re-enter")

    # st.write("Your Price will be",model.predict([[area,room,lon,lat]]))

