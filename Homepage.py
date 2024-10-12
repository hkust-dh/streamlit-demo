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

st.markdown("## Pic")

# two columns layout

    # show image
    st.image('images/生活照.jpg', caption='https://lbezone.hkust.edu.hk/rse/thread-bound-books')




st.markdown('---')
   
# Data pre-processing
data2 = data.copy()
data2.rename(columns={'year published':'year'}, inplace=True)
data2['Period'] = ['16th century' if 1501 <= year <= 1600 else '17th century' if 1601 <= year <= 1700 else '18th century' if 1701 <= year <= 1800 else '19th century' if 1801 <= year <= 1900 else '20th century' if 1901 <= year <= 2000 else "Ungrouped" for year in data2['year']]


################### Data Visualization #######################

# If you're looking for a detailed explanation about this part of code, please read our article : https://digitalhumanities.hkust.edu.hk/tutorials/learn-python-from-zero-for-absolute-beginner-2-data-visualization/


plotly_chart1 = px.histogram(data2, x='Period', y='number of items')

plotly_chart1.update_layout(
    title = 'Number of Items by Century',
    yaxis_title='Number of items',
    xaxis_title='Century',
)

st.markdown("# Plotly chart example")

# show the plotly chart
st.plotly_chart(plotly_chart1, use_container_width=True)

###############################################################

# another plotly chart 
plotly_chart3 = px.bar(data2, x='year', y='number of items',
            color='Period',
            color_discrete_sequence=["#ffb7b2", "#ffdac0", "#e3f0cb", "#b5ead9", "#c7cee9"])

plotly_chart3.update_layout(
    title = 'Number of Items by Year',
    yaxis_title='Number of items',
    xaxis_title='Year',
    paper_bgcolor = 'white', 
    plot_bgcolor = 'white', 

    xaxis = dict(
        showline = True,
        linecolor = 'rgb(102, 102, 102)',
        tickfont_color = 'rgb(102, 102, 102)',
        showticklabels = True,
        dtick = 10,
        ticks = 'outside',
        tickcolor = 'rgb(102, 102, 102)',
    ),
    yaxis = dict(
        showline = True,
        linecolor = 'rgb(102, 102, 102)',
        tickfont_color = 'rgb(102, 102, 102)',
        showticklabels = True,
        dtick = 5, 
        ticks = 'outside',
        tickcolor = 'rgb(102, 102, 102)',
    ),
)

plotly_chart3.add_hline(y = data2['number of items'].mean(), annotation_text = 'average line', line_width = 1, line_color = '#edc982')

plotly_chart3.update_layout(hovermode='x unified')

st.markdown("# Another Plotly chart example")

# show the plotly chart
st.plotly_chart(plotly_chart3, use_container_width=True)

# year that have the max number of items
yearMaxItems = data.loc[data['number of items'].idxmax()]
st.write(f'Maximum: In this collection, there are {yearMaxItems[1]} items that were published in {yearMaxItems[0]}.')

###############################################################

st.markdown("# Streamlit chart example")

# show code
code = '''st.line_chart(data2, x='year', y='number of items')'''
st.code(code, language='python')

# streamlit charts
st.line_chart(data2, x='year', y='number of items')