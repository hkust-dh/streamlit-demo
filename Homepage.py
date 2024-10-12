#####################
##   Homepage.py   ##
#####################

# https://digitalhumanities.hkust.edu.hk/tutorials/learn-python-from-zero-for-absolute-beginner-3-create-website/


###############################################################
# import python libraries
###############################################################
import streamlit as st
import pandas as pd
import plotly.express as px

###############################################################
# page info
###############################################################
st.set_page_config(
    page_title="DU Heng| Personal Website",
    page_icon="👋",
)

###############################################################
# sidebar
###############################################################
with st.sidebar:
    st.markdown("""
                (https://duhengweb.streamlit.app/)
                """)
    st.markdown("""
                This website serves as a personal through introduction about me
                """)
    
###############################################################
# page content
###############################################################
st.caption("Personal Web")
st.title("Welcome DU Heng's Personal Web")

st.markdown("""
            Thank you for taking the time to visit my personal website! It is been quite a journey, and I am glad you are here. While I may not have grand offerings or thrilling tales, I want to share a glimpse into my life and experiences. Join me as I explore the ordinary moments that shape who I am. Let’s connect over the little things that make life interesting!
            """)

st.info('[Connect with me!](https://www.linkedin.com/in/heng-du-016bba215/)', icon="👋")

st.markdown("---")

#################### read Excel file data ############################



######################################################################

# If you're looking for a detailed explanation about this part of code, please read our article : https://digitalhumanities.hkust.edu.hk/tutorials/learn-python-from-zero-for-absolute-beginner-1-data-cleaning/

st.markdown("## Do not Worry! It is just me ")

# two columns layout

    # show image
st.image('images/生活照.jpg')




st.markdown('---')
   
# Data pre-processing



################### Data Visualization #######################
