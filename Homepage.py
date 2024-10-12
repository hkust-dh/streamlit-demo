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
                [HKUST Digital Humanities Initiative](https://digitalhumanities.hkust.edu.hk/)
                """)
    st.markdown("""
                This website serves as a demo to showcase the capabilities and functionalities of Streamlit in creating web applications. If you are interested in learning the step-by-step process of how this website was created, please refers to [our article](https://digitalhumanities.hkust.edu.hk/tutorials/learn-python-from-zero-for-absolute-beginner-3-create-website/) for detailed instructions and explanations.
                """)
    
###############################################################
# page content
###############################################################
st.caption("Personal Web")
st.title("Personal Web")

st.markdown("""
            Welcome to this website! 

            Are you interested in creating a website like this demo site? Look no further! Let's read our article below. We will walk you through the steps of creating this demo site, cover everything from setting up the development environment to deploying your website online. Get ready to bring your visualizations created in [our previous lesson](https://digitalhumanities.hkust.edu.hk/tutorials/learn-python-from-zero-for-absolute-beginner-2-data-visualization/) to life on the web!

            👉 https://digitalhumanities.hkust.edu.hk/tutorials/learn-python-from-zero-for-absolute-beginner-3-create-website/
            
            We would love to hear from you if you have followed along with the article and successfully created a website. We appreciate your efforts and would be thrilled to share and highlight your work on our website.
            """)

st.info('[Share with us!](https://forms.office.com/r/FPkLhaE2sr)', icon="💬")

st.markdown("---")

#################### read Excel file data ############################

filepath = 'data/data_dh-tutorial_rse-ChiBksBefore1949-ThreadBound.xlsx'
data = pd.read_excel(filepath, sheet_name='data')

######################################################################

# If you're looking for a detailed explanation about this part of code, please read our article : https://digitalhumanities.hkust.edu.hk/tutorials/learn-python-from-zero-for-absolute-beginner-1-data-cleaning/

st.markdown("## Data for this demo")

# two columns layout
col1, col2 = st.columns(2)
with col1:
    # calculate the sum
    sumvalue = data['number of items'].sum()
    
    # show the sum
    st.metric(label="No. of items", value=sumvalue)
    st.write(f'There are a total of {sumvalue} items in this collection online as of 4 Aug 2023.')

    # show image
    st.image('images/rse-chibk1949threadbound.png', caption='https://lbezone.hkust.edu.hk/rse/thread-bound-books')


with col2:
   # show dataframe
   st.dataframe(data)

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