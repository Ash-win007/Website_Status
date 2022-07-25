import streamlit as st
import check_status as cs
import pandas as pd
import hydralit_components as hc
import time


st.markdown("<h1 style='text-align: center; color: red;'>Website up or down status</br></h1>", unsafe_allow_html=True)
input_url=st.text_input("Enter the website's URL","")
previous=""

if input_url != previous:
    previous=input_url
    with hc.HyLoader('',hc.Loaders.standard_loaders,index=5):
        time.sleep(2)


try:
    status,time_taken,header=cs.check(input_url)
    data=[['Status code',status],['Loading time',time_taken],['Server',header['server']],
            ['Link',input_url],['Content-Type',header['Content-Type']]]
    df=pd.DataFrame(data)
    st.write(df)

    if status=="200":
        st.info("Server is running")
    else:
        st.error("Server is down")

    if input_url:
        st.markdown(f'Click here to visit the website: {input_url}')

except:
    if input_url:
        st.error("The entered url is invalid")