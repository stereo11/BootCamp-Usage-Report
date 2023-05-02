from st_btn_select import st_btn_select
import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import openpyxl

st.set_page_config(layout = "wide",initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

page = st_btn_select(
  # The different pages
  ('Home','Overall Enrollment Trends', 'Course wise Usage Analysis'),
  # Enable navbar
  nav=False
)


if page == 'Home':
    st.image('Report.png',use_column_width=True)


if page == 'Overall Enrollment Trends':
    st.write(
    # Intro text
    '''
    ##### The scope of this analysis is the students enrolled from 31st December 2022 to 30th March 2022 in BootCamp Courses. There are 497 students enrolled during this timeframe.
    '''
    )
    
    df1 = pd.read_excel('Data/Continuous_Date_file.xlsx')
    df1 = pd.DataFrame(df1)

    trend = alt.Chart(df1, title='Enrollment Trend of the Students in the BootCamp Courses').mark_line().encode(
    alt.X('Date',title='Timestamp'),
    alt.Y('Students_enrolled',title='No. of Enrolled Students'),
    tooltip=['Date','Students_enrolled'])

    st.altair_chart(trend, use_container_width=True)

    df2 = pd.read_excel('Data/distributionOfHoursSpend.xlsx')
    df2 = pd.DataFrame(df2)

    bar = alt.Chart(df2, title='Distribution of Students and No. of Hours they Spend on BootCamp Courses').mark_bar().encode(
    alt.X('Hours_Spend_Bucket',title='No. of Hours Spend'),
    alt.Y('n',title='No. of Students'),
    tooltip=['Hours_Spend_Bucket','n'])

    st.altair_chart(bar, use_container_width=True)
    

if page == 'Course wise Usage Analysis':
    
    df3 = pd.read_excel('Data/CoursedistributionOfHoursSpend.xlsx')
    df3 = pd.DataFrame(df3)

    df4 = pd.read_excel('Data/Status.xlsx')
    df4 = pd.DataFrame(df4)

    ##List of Courses
    clist= [" "]
    clist.extend(list(df3['Course'].unique()))
    course = st.selectbox("Select a Course:",clist,index=0)

    col1, col2 = st.columns(2)

    Activity = df3[df3['Course'] == course]
    Status = df4[df4['Course'] == course]

    if(course != " "):
        bar = alt.Chart(Activity, title=f'Distribution of Students and No. of Hours they Spend on {course} BootCamp Course').mark_bar().encode(
        alt.X('Hours_Spend_Bucket',title='No. of Hours Spend'),
        alt.Y('n',title='No. of Students'),
        tooltip=['Hours_Spend_Bucket','n'])

        col1.altair_chart(bar, use_container_width=True)
        
        bar2 = alt.Chart(Status, title=f'Distribution of Students on Current Progress in {course} BootCamp Course').mark_bar().encode(
        alt.X('Status',title='Status'),
        alt.Y('count',title='No. of Students'),
        tooltip=['Status','count'])

        col2.altair_chart(bar2, use_container_width=True)